from modal import Image, Stub, wsgi_app
from twitter_bot import TwitterBot

stub = Stub()
image = Image.debian_slim().pip_install("flask")

@stub.function(secret=modal.Secret.from_name("my-openai-secret"))
def complete_text(prompt):


@stub.function(image=image)
@wsgi_app()
def flask_app():
    from flask import Flask, request

    web_app = Flask(__name__)

    @web_app.get("/")
    def home():
        return "Hello Flask World!"

    @web_app.post("/foo")
    def foo():
        return request.json

    @web_app.get("/dissent")
    def home():
        bot = TwitterBot()
        return bot.job()
        # TODO: flesh out input output of this

    return web_app
