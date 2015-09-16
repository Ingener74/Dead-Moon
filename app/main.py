# encoding: utf8
import platform

import os
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


class Explorer:
    def __init__(self, *args, **kwargs):
        self.template = kwargs['template']
        self.path = filter(lambda d: len(d) > 0, os.path.dirname(os.getcwd()).split(kwargs['separator']))

    def go(self, directory):
        self.path += [directory]

    def up(self):
        if len(self.path) == 1:
            raise TypeError('can not go up')
        del self.path[-1]

    def getPath(self):
        return (self.template * len(self.path)).format(*self.path)


class ExplorerLinux(Explorer):
    def __init__(self):
        Explorer.__init__(self, separator='/', template='/{}')


class ExplorerWindows(Explorer):
    def __init__(self):
        Explorer.__init__(self, separator='\\', template='{}\\')


explorer = ExplorerWindows() if platform.system() == 'Windows' else ExplorerLinux()


@app.route('/test/<place>', methods=['POST'])
def test(place):
    t.inc()
    if place == 'button':
        return jsonify({'title': 'button {}'.format(t.get_index())})
    return jsonify({"title": "test ajax title {ind}".format(ind=t.get_index())})


@app.route('/explore/<go_to>', methods=['POST'])
def explore(go_to):
    try:
        if go_to == 'up':
            explorer.up()
        elif go_to != 'current':
            explorer.go(go_to)
        return jsonify({'content': ['up'] + os.listdir(explorer.getPath())})
    except BaseException, e:
        return jsonify({'error': str(e)})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
