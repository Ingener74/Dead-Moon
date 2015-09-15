# encoding: utf8
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

req_index = 0


class Test:
    def __init__(self):
        self.index = 0

    def get_index(self):
        return self.index

    def inc(self):
        self.index += 1


t = Test()


@app.route('/test/<place>', methods=['POST'])
def test(place):
    t.inc()
    if place == 'button':
        return jsonify({'title': 'button {}'.format(t.get_index())})
    return jsonify({"title": "test ajax title {ind}".format(ind=t.get_index())})


class ExplorePath:
    def __init__(self):
        self.path = ['.']

    def go(self, directory):
        self.path += [directory]

    def up(self):
        del self.path[-1]

    def getPath(self):
        return '*{}'.format(self.path)


@app.route('/explore/<go_to>', methods=['POST'])
def explore(go_to):
    if go_to == 'current':
        current_dir = ['up'] + os.listdir('.')
        return jsonify({'content': current_dir})
    if go_to == 'up':
        return jsonify({'content': []})
    return jsonify({'content': ['foo', 'bar']})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
