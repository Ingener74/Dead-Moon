# encoding: utf8
import os

from flask import Flask, render_template, jsonify

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
    def __init__(self, windows=False):
        self.windows = windows
        self.path = [''] if self.windows else ['.']

    def go(self, directory):
        self.path += [directory]

    def up(self):
        if len(self.path) == 1:
            raise TypeError('can not go up')
        del self.path[-1]

    def getPath(self):
        if self.windows:
            return ('{}/' * (len(self.path) - 1)).format(*self.path[1:])
        else:
            return ('{}/' * len(self.path)).format(*self.path)


explorer = ExplorePath(windows=True)


@app.route('/explore/<go_to>', methods=['POST'])
def explore(go_to):
    if go_to == 'current':
        return jsonify({'content': ['up'] + os.listdir('.')})
    elif go_to == 'up':
        explorer.up()
        return jsonify({'content': ['up'] + os.listdir(explorer.getPath())})
    else:
        explorer.go(go_to)
        return jsonify({'content': ['up'] + os.listdir(explorer.getPath())})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
