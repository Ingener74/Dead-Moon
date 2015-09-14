# encoding: utf8


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
    print 'place ', place
    t.inc()
    if place == 'button':
        print 'button'
        return jsonify({'title': 'button {}'.format(t.get_index())})
    return jsonify({"title": "test ajax title {ind}".format(ind=t.get_index())})


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5003)
