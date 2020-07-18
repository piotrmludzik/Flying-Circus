# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                         routes handling
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

from flask import Flask, redirect, render_template, request, session
import data
import user


app = Flask(__name__)
app.secret_key = b'%f4H&sT59hk!D76*'


# ------------------------------------------ main route -------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------------- login, logout routes --------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # 'POST': login a user
    username = request.form['username']
    password = request.form['password']

    if not user.valid_login(username, password):
        return redirect('/login')

    session['username'] = username
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


# ------------------------------------------ test route -------------------------------------------

@app.route('/test')
def test():
    return 'test page'


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
