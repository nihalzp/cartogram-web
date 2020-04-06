import bcrypt
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import secrets
import string
import base64

def generate_captcha():

    alphabet = "12345679abcdeghijkmnopqrtuvwxyz"
    text = ''.join(secrets.choice(alphabet) for i in range(5))

    image = ImageCaptcha()
    audio = AudioCaptcha(voicedir='audiocaptcha')

    img_data = image.generate(text)

    img_str = base64.b64encode(img_data.getvalue())
    img_base64 = "data:image/png;base64," + img_str.decode("utf-8")

    audio_data = audio.generate(text)

    audio_str = base64.b64encode(audio_data)
    audio_base64 = "data:audio/wav;base64," + audio_str.decode("utf-8")

    captcha_hash = bcrypt.hashpw(text, bcrypt.gensalt( 12 ))

    return {"captcha_image": img_base64, "captcha_audio": audio_base64, "captcha_hashed": captcha_hash}

def validate_captcha(captcha, captcha_hashed):

    return bcrypt.checkpw(captcha, captcha_hashed)
