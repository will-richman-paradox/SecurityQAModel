# import nltk
from transformers import pipeline

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


# Sentiment Analysis on Yes/No Questions
def yes_no_determination(question, answer):
    # Boolean to determine Yes/No
    yes_answer = False

    # Important Sentiment Analyser form Transformers
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Formatting Question and Answer to be put in the pipeline
    data = [question, answer]

    # Sentiment Analysis on data
    sentiment = sentiment_pipeline(data)

    # Accessing POSITIVE/NEGATIVE label from the Sentiment Analysis
    question_label = sentiment[0]['label']
    answer_label = sentiment[0]['label']

    # If POSITIVE/POSITIVE OR NEGATIVE/NEGATIVE change yes_answer to True
    if question_label == answer_label:
        yes_answer = True

    return yes_answer
