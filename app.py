# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                         routes handling
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

from flask import Flask, flash, redirect, render_template, request, session
import const as c
import data
import user

app = Flask(__name__)
app.secret_key = b'%f4H&sT59hk!D76*'


# ------------------------------------------ main route -------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------------- login, logout routes --------------------------------------

@app.route('/login')
def login():
    if user.is_logged():
        return redirect('/')

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_data_process():
    username = request.form['username']
    password = request.form['password']

    if not user.valid_login(username, password):
        flash('Invalid username or password!')
        return redirect('/login')

    session['username'] = username
    flash('You were successfully logged in!')

    return redirect('/')


@app.route('/logout')
def logout_data_process():
    if user.is_logged():
        session.pop('username', None)
        flash('You were successfully logged out!')

    return redirect('/')


# ------------------------------------------ test route -------------------------------------------

@app.route('/test')
def test():
    if not user.is_logged():
        return redirect('/')

    # first run of test (first question)
    if 'questions_list' not in session:
        data.setup_exercises()

    data.get_next_exercise()
    return render_template('test.html')


@app.route('/test', methods=['POST'])
def test_data_process():
    data.finish_exercise(request.form['answer'])

    # if the questions list is not empty goes to next question
    if session['questions_list']:
        return redirect('/test')

    return ", ".join(session['user_answers'])


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
