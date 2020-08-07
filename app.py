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

    session[c.SV_USERNAME] = username
    flash('You were successfully logged in!')

    return redirect('/')


@app.route('/logout')
def logout_data_process():
    if user.is_logged():
        session.pop(c.SV_USERNAME, None)
        flash('You were successfully logged out!')

    return redirect('/')


# ------------------------------------------ test route -------------------------------------------

@app.route('/test')
def test():
    if not user.is_logged():
        return redirect('/')

    # first run of test (first question)
    if c.SV_QUESTION_LIST not in session:
        data.setup_exercises()

    data.get_next_exercise()
    return render_template('test.html')


@app.route('/test', methods=['POST'])
def test_data_process():
    data.finish_exercise(request.form['answer'])

    # if the questions list is not empty goes to next question
    if session[c.SV_ACTUAL_QUESTION_NUMBER] < session[c.SV_QUESTION_MAX_NUMBER]:
        return redirect('/test')

    return redirect('/result')


@app.route('/result')
def test_result():
    if not user.is_logged():
        return redirect('/')

    return render_template(
        'result.html',
        question_data=data.exercises,
        correct_answers_number=data.get_correct_answers_number()
    )


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
