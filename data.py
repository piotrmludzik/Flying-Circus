# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                      program data functions
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

from flask import session
import const as c


# Exercises data: questions, answers and which is correct.
exercises = {
    "I ______ bus on Mondays.": {
        "a. 'm going to work with": False,
        "b. 'm going to work by": False,
        "c. go to work with": False,
        "d. go to work by": True
    },
    "Sorry, but this chair is ______.": {
        "a. me": False,
        "b. mine": True,
        "c. my": False,
        "d. our": False
    },
    "A: 'How old ______?'   B: 'I ______ .'": {
        "a. are you / am 20 years old.": True,
        "b. have you / have 20 years old.": False,
        "c. are you / am 20 years.": False,
        "d. do you have / have 20 years.": False
    },
    "I ______ to the cinema.": {
        "a. usually don't go": False,
        "b. don't usually go": True,
        "c. don't go usually": False,
        "d. do not go usually": False
    },
    "Where ______ ?": {
        "a. your sister works": False,
        "b. your sister work": False,
        "c. does your sister work": True,
        "d. do your sister work": False
    }
}


# ---------------------------------- english learning functions -----------------------------------

def setup_test():
    """ Prepare test exercises. """
    def get_questions() -> list:
        """ Prepares a list of randomly ordered questions. """
        def get_questions_list() -> list:
            """ Gets a list of questions form exercises dictionary. """
            questions_list = []
            for question in exercises.keys():
                questions_list.append(question)

            return questions_list

        def get_random_questions(questions_list: list) -> list:
            """ Generates the randomly ordered list of questions. """
            import random

            random_questions_list = []
            while questions_list:
                question = random.choice(questions_list)
                random_questions_list.append(question)
                questions_list.remove(question)

            return random_questions_list

        # ---------- get_questions() main code ----------
        return get_random_questions(get_questions_list())

    # ---------- setup_exercises() main code ----------
    session[c.SV_QUESTIONS_ORDER] = get_questions()
    session[c.SV_ACTUAL_QUESTION_NUMBER] = 0
    session[c.SV_TEST_DATA] = {}


def exercise_finished(user_answer: str):
    """ Finishes the exercise (user clicked the submit button). """
    question = session[c.SV_QUESTIONS_ORDER][session[c.SV_ACTUAL_QUESTION_NUMBER]]
    session[c.SV_TEST_DATA][question] = user_answer

    session[c.SV_ACTUAL_QUESTION_NUMBER] += 1


# def get_correct_answers_number():
#     """ Gets the number of correct answers. """
#     correct_answers_number = 0
#     for question in session[c.SV_QUESTIONS_ORDER]:
#         pass
