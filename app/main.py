# encoding: utf8
import os
import platform

from flask import Flask, render_template, jsonify

app = Flask(__name__)


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


class Explorer:
    def __init__(self, path):
        self.path = path

    def go(self, directory):
        self.path += [directory]

    def up(self):
        if len(self.path) == 1:
            raise TypeError('can not go up')
        del self.path[-1]

    def getPath(self):
        raise NotImplementedError


class ExplorerLinux(Explorer):
    def __init__(self):
        Explorer.__init__(self, filter(lambda d: len(d) > 0, os.path.dirname(os.getcwd()).split('/')))

    def getPath(self):
        return ('/{}' * len(self.path)).format(*self.path)


class ExplorerWindows(Explorer):
    def __init__(self):
        Explorer.__init__(self, filter(lambda d: len(d) > 0, os.path.dirname(os.getcwd()).split('\\')))

    def getPath(self):
        return ('{}\\' * (len(self.path))).format(*self.path)


explorer = ExplorerWindows() if platform.system() == 'Windows' else ExplorerLinux()


@app.route('/explore/<go_to>', methods=['POST'])
def explore(go_to):
    try:
        if go_to == 'up':
            explorer.up()
        elif go_to != 'current':
            explorer.go(go_to)
        return jsonify({'content': ['up'] + os.listdir(explorer.getPath())})
    except BaseException, e:
        print str(e)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
