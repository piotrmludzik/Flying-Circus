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

    if 'questions_list' not in session:
        session['questions_list'] = data.get_questions()  # sets a random list of questions

    # gets completly exercise of the first question from the questions list
    question = session['questions_list'][c.FIRST_QUESTION]
    session['question'] = question
    session['answers'] = data.exercises[question]

    return render_template('test.html')


@app.route('/test', methods=['POST'])
def test_data_process():
    return 'it\'s!'


# ------------------------------------------- main code -------------------------------------------

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
