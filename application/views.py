from flask import Blueprint
import requests


base_bp = Blueprint('base_bp', __name__)

@base_bp.route("/")
def index():

    send_message()

    return "Success"


def send_message():

    chat_id = '792670289'
    message = 'Hello'

    url = "https://api.telegram.org/bot1770514264:AAFfu4-CEYiXi1vHPdtGihN2O-mGb_rcY40"
    base_url = f"{url}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(base_url)

    return response

