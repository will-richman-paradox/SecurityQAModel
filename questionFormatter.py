# import nltk



def format_question(question):
    # Words to remove from sentence
    words_to_remove = ["paradox"]

    # Remove words/phrases that will screw up the model
    question_test_list = question.lower().split()
    i = 0
    index_list_words_remove = []

    # Loop through the words in question_test_list
    for word in question_test_list:
        for term in words_to_remove:
            if word == term:
                question_test_list.remove(word)
                index_list_words_remove.append(i)
        i += 1

    # Splitting question into a list of words
    question = question.split()

    # Removing identified words from question
    for it in index_list_words_remove:
        del question[it]

    question = ' '. join(question)
    return question


# For Determining Yes/No question
def question_determiner(question):
    # AUX verb + subject + main verb or
    yes_no_question = False

    # Verbs indicating yes/no questions
    aux_verbs = ['has', 'have', 'had', 'is', 'am', 'are', 'been', 'being', 'was', 'were',
                 'does', 'do', 'did', 'will', 'would', 'shall', 'should', 'may', 'might',
                 'must', 'can', 'could']

    # Formatting question to be able to check the first word
    question_words = question.lower().split()

    # Checking first word of question against the aux_verb list
    for word in aux_verbs:
        if word == question_words[0]:
            yes_no_question = True

    return yes_no_question



