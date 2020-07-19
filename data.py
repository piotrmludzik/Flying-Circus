# -------------------------------------------------------------------------------------------------
#                                          Flying circus
#                                          program data
#                                              v 1.0
# -------------------------------------------------------------------------------------------------

import const as c


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

        random_questions = []
        while questions_list:
            question = random.choice(questions_list)
            random_questions.append(question)
            questions_list.remove(question)

        return random_questions

    return get_random_questions(get_questions_list())
