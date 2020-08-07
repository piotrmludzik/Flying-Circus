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
        data.close_test()
        flash('You were successfully logged out!')

    return redirect('/')


# ------------------------------------------ test route -------------------------------------------

@app.route('/test')
def test():
    if not user.is_logged():
        flash('The user is not logged! ')
        return redirect('/')

    # first run of test
    if c.SV_QUESTIONS_ORDER not in session:
        data.setup_test()

    question = session[c.SV_QUESTIONS_ORDER][session[c.SV_ACTUAL_QUESTION_NUMBER]]
    answers = list(data.exercises[question].keys())
    return render_template('test.html', question=question, answers=answers)


@app.route('/test', methods=['POST'])
def test_data_process():
    data.exercise_finished(request.form['answer'])

    # goes on to the next question if it is not the last question
    if session[c.SV_ACTUAL_QUESTION_NUMBER] < len(session[c.SV_QUESTIONS_ORDER]):
        return redirect('/test')

    return redirect('/result')


@app.route('/result')
def test_result():
    if not user.is_logged() or c.SV_QUESTIONS_ORDER not in session:
        flash('The user is not logged or the test has not been started. ')
        return redirect('/')

    if session[c.SV_ACTUAL_QUESTION_NUMBER] < len(session[c.SV_QUESTIONS_ORDER]):
        flash('The test has not been completed.')
        return redirect('/test')

    data.close_test()

    return render_template(
        'result.html',
        exercises_data=data.exercises,
        test_data=session[c.SV_TEST_DATA],
        correct_answers_number=data.get_correct_answers_number(session[c.SV_TEST_DATA])
    )


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
