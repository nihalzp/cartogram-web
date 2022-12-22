from constants import *
import shutil
import sys


def updatewebpy(map_name):
    print("Backing up web.py...")
    
    shutil.copy(INTERNAL_DIR + "/web.py", INTERNAL_DIR + "/web.py.bak")
    
    try:
        with open(INTERNAL_DIR + "/web.py", "r") as web_py_file:    
            web_py_contents = web_py_file.read()
            web_py_lines = web_py_contents.split("\n")
    except Exception as e:
        raise e
    
    web_py_new_lines = []
    found_header = False
    found_body = False
    for line in web_py_lines:

        if line.strip() == "# ---addmap.py header marker---":

            web_py_new_lines.append("from handlers import {}".format(map_name))
            web_py_new_lines.append("# ---addmap.py header marker---")
            found_header = True
        elif line.strip() == "# ---addmap.py body marker---":

            web_py_new_lines.append("'{0}': {0}.CartogramHandler(),".format(map_name))
            web_py_new_lines.append("# ---addmap.py body marker---")
            found_body = True
        else:
            web_py_new_lines.append(line)
    
    if not found_header or not found_body:
        print("I was not able to find the appropriate markers that allow me to modify the web.py file.")
        sys.exit()
    
    with open(INTERNAL_DIR + "/web.py", "w") as web_py_file:
            web_py_file.write("\n".join(web_py_new_lines))
            
    return