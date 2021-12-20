import awslambda
import settings
import threading
import json
import queue
import geojson_extrema
import cartwrap
import redis
import random
import string

def get_random_string(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length))

def serverless_generate(area_data, map_handler):

    redis_conn = redis.Redis(host=settings.CARTOGRAM_REDIS_HOST, port=settings.CARTOGRAM_REDIS_PORT, db=0)
    q = queue.Queue()
    unique_key = get_random_string(50)

    def downloader_worker():
        lambda_result = awslambda.generate_cartogram(map_handler.gen_area_data(area_data),
                                        map_handler.get_gen_file(), settings.CARTOGRAM_LAMBDA_URL,
                                        settings.CARTOGRAM_LAMDA_API_KEY, unique_key)

        cartogram_gen_output = lambda_result['stdout']

        q.put(cartogram_gen_output)

    threading.Thread(target=downloader_worker(), daemon=True).start()

    current_stderr = ""
    current_progress_level = None
    gen_output = ""

    while True:
        current_progress = redis_conn.get("cartprogress-{}".format(unique_key))

        if current_progress == None:
            pass
        else:
            current_progress = json.loads(current_progress.decode())
            if current_progress['progress'] != current_progress_level:
                to_print = current_progress['stderr'].replace(current_stderr, "")
                for line in to_print.split("\n"):
                    print("Generating population map: {}".format(line), flush=True)
                current_stderr = current_progress['stderr']
                current_progress_level = current_progress['progress']

        try:
            gen_output = q.get(False, timeout=0.1)
            break
        except queue.Empty:
            pass

    current_progress = redis_conn.get("cartprogress-{}".format(unique_key))

    if current_progress == None:
        pass
    else:
        current_progress = json.loads(current_progress.decode())
        if current_progress['progress'] != current_progress_level:
            to_print = current_progress['stderr'].replace(current_stderr, "")
            for line in to_print.split("\n"):
                print("Generating population map: {}".format(line), flush=True)
    return json.loads(gen_output)

def self_generate(area_data, map_handler):

    gen_output_lines = []

    for source, line in cartwrap.generate_cartogram(map_handler.gen_area_data(area_data), map_handler.get_gen_file(), os.environ["CARTOGRAM_EXE"]):

        if source == "stdout":
            gen_output_lines.append(line.decode().strip())
        else:
            print("Generating population map: {}".format(line.decode().strip()))

    gen_output = "\n".join(gen_output_lines)
    return json.loads(gen_output)


