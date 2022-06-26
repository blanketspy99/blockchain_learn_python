from flask_classful import FlaskView, route

from flask import Flask

class NodeAPI(FlaskView);

    def __init__(self) -> None:
        self.app = Flask(__name__)

    def start(self);
        NodeAPI.register(self.app, route_base='/')
        self.app.run(host='localhost')

    @route('/info', methods=['GET'])
    def info(self):
        pass

    

