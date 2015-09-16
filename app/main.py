# encoding: utf8
import os
import platform

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
        print 'Windows' if windows else 'Not Windows'
        self.windows = windows
        self.path = filter(lambda d: len(d) > 0, os.path.dirname(os.getcwd()).split('/'))
        print self.path

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
            return ('/{}' * len(self.path)).format(*self.path)


explorer = ExplorePath(windows=platform.system() == 'Windows')


@app.route('/explore/<go_to>', methods=['POST'])
def explore(go_to):
    if go_to == 'current':
        return jsonify({'content': ['up'] + os.listdir(explorer.getPath())})
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
