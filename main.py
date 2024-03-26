from knowledgeBaseQuestionSimilairty import *
from policySearchAnswerer import *
from answerComparer import *
from questionFormatter import *
from keywordSearcher import *

    # Idea put substitue words in parenthesis to be then later processed by the
    # algorithm in another method

def main():

    # start()

    # Question Prompt and Gathering Question
    question = input("\nWhat is your data security question for Paradox?\n\n")
    print("\n\n... Compiling Answer ...\n\n")

    # Determining yes/no question
    #  yes_no_question = question_determiner(question)

    # Calling questionFormatter.py to format question
    question = format_question(question)

    # Calling knowledgeBaseQuestionSimilarity.py to compare question to Knowledge Base Question/Topic
    similarity_results = get_answer(question)

    # Calling knowledgeBaseQuestionSimilarity.py to search through Security Policies
    policy_results = policy_search(question)

    # Organizing answerComparer.py returns into organized variables
    knowledge_base_question = similarity_results[0]
    knowledge_base_answer = similarity_results[1]
    knowledge_base_score = similarity_results[2]

    # Organizing knowledgeBaseQuestionSimilarity.py returns into organized variables
    # policy_question = policy_results[0]
    # policy_answer = policy_results[1]
    # policy_score = policy_results[2]

    # Calling answerComparer.py to get the best answer to return
    # best_answer = compare_answers(knowledge_base_question, knowledge_base_answer, knowledge_base_score,
    #                              policy_question, policy_answer, policy_score)

    # Separate return variables in best_answer
    final_answer = knowledge_base_answer
    final_score = knowledge_base_score

    # Handling Yes/No Answer Questions
    '''
    if yes_no_question:

        # Checking that score is over .5 threshold
        if yes_no_check_threshold(final_score):

            # Determination of Yes or No
            yes_answer = yes_no_determination(question, final_answer)

            # Yes Use Case
            if yes_answer:
                print("Final Answer: Yes")
                print("Final Score: " + str(final_score))

                print("\n")

                print("Original Answer: " + final_answer)

            # No Use Case
            else:
                print("Final Answer: No")
                print("Final Score: " + str(final_score))

                print("\n")

                print("Original Answer: " + final_answer)

        # Printing short answer question
        else:
            # Print final answer
            print("Final Answer: " + final_answer)
            print("Final Score: " + str(final_score))
    '''
    # Handling Short Answer Questions
    # else:
        # Print final answer
    print("Final Answer: " + final_answer)

    percentage = round(final_score * 100, 2)
    print("Final Score: " + str(percentage) + "%")


main()
