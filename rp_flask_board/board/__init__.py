from flask import Flask

from board import pages
# Initial creat app function based on the reading

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    return app