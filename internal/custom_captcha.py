import bcrypt
from captcha.image import ImageCaptcha
import secrets
import string
import base64

def generate_captcha():

    alphabet = "123456789abcdefghijkmnopqrstuvwxyz"
    text = ''.join(secrets.choice(alphabet) for i in range(5))

    image = ImageCaptcha()

    data = image.generate(text)

    img_str = base64.b64encode(data.getvalue())
    img_base64 = "data:image/png;base64," + img_str.decode("utf-8")

    captcha_hash = bcrypt.hashpw(text, bcrypt.gensalt( 12 ))

    return {"captcha_image": img_base64, "captcha_hashed": captcha_hash}

def validate_captcha(captcha, captcha_hashed):

    return bcrypt.checkpw(captcha, captcha_hashed)
