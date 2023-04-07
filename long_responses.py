import random

R_DUMB = "I am a programmed bot I only respond what I know."


def unknown():
    response = ['Could you please re-phrase that?',
                "I dont understand, repeat please",
                "..."][random.randrange(4)]
    return response
