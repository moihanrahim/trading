from flask import Flask, request, abort
from algo_trading import algo

app = Flask(__name__)


@app.route('/')
def root():
    return 'online'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = eval(request.get_data(as_text=True))
        print(data)
        algo(option=data["option"], strategy=data["strategy"], quantity=data["quantity"],normal_order=data["entry"])
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    # scheduler run
    app.run()
