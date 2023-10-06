
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
