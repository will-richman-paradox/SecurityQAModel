from transformers import pipeline


def compare_answers(kb_question, kb_answer, kb_score, pol_question, pol_answer, pol_score):

    # Initializing Variables
    best_answer = ""
    best_score = 0.0

    # Testing if KB Answer has confidence score > .50
    if kb_score > .5:
        best_answer = kb_answer
        best_score = kb_score
        print("\n\nPolicy Answer: " + pol_answer)
        print("Policy Score: " + str(pol_score) + "\n\n")
    else:
        if kb_score > pol_score:
            best_answer = kb_answer
            best_score = kb_score
            print("\n\nPolicy Answer: " + pol_answer)
            print("Policy Score: " + str(pol_score) + "\n\n")
        else:
            best_answer = pol_answer
            best_score = pol_score
            print("\n\nKB Answer: " + kb_answer)
            print("KB Score: " + str(kb_score) + "\n\n")

    return best_answer, best_score


# Sentiment Analysis on Yes/No Questions
def yes_no_determination(question, answer):
    # Boolean to determine Yes/No
    yes_answer = False

    # Important Sentiment Analyser form Transformers
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    # Formatting Question and Answer to be put in the pipeline
    data = [question, answer]

    # Sentiment Analysis on data
    sentiment = sentiment_pipeline(data)

    print(sentiment + '\n')

    # Accessing POSITIVE/NEGATIVE label from the Sentiment Analysis
    question_label = sentiment[0]['label']
    answer_label = sentiment[1]['label']

    # If POSITIVE/POSITIVE OR NEGATIVE/NEGATIVE change yes_answer to True
    if question_label == answer_label:
        yes_answer = True

    return yes_answer


def yes_no_check_threshold(score):

    # Boolean to see what to print | False = str | True = Yes/No
    yes_no_answer = False

    # Check to see if confidence score is over .5
    if score > .5:
        yes_no_answer = True

    # Return False/True
    return yes_no_answer
