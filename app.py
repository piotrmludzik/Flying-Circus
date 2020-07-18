# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                         routes handling
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

from flask import Flask, redirect, render_template, request
import data

app = Flask(__name__)


# ------------------------------------------ main route -------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------------------ else routes -------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # 'POST'
    return redirect('/')


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7000,
        debug=True
    )
