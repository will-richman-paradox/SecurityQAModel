from knowledgeBaseQuestionSimilairty import *
from policySearchAnswerer import *
from answerComparer import *
from questionFormatter import *


def main():

    # Question Prompt and Gathering Question
    question = input("\nWhat is your data security question for Paradox?\n")

    # Determining yes/no question
    yes_no_question = question_determiner(question)

    # Calling questionFormatter.py to format question
    question = format_question(question)

    # Calling answerComparer.py to compare question to Knowledge Base Question/Topic
    similarity_results = get_answer(question)

    # Calling knowledgeBaseQuestionSimilarity.py to search through Security Policies
    policy_results = policy_search(question)

    # Organizing answerComparer.py returns into organized variables
    knowledge_base_question = similarity_results[0]
    knowledge_base_answer = similarity_results[1]
    knowledge_base_score = similarity_results[2]

    # Organizing knowledgeBaseQuestionSimilarity.py returns into organized variables
    policy_question = policy_results[0]
    policy_answer = policy_results[1]
    policy_score = policy_results[2]

    # Calling answerComparer.py to get the best answer to return
    best_answer = compare_answers(knowledge_base_question, knowledge_base_answer, knowledge_base_score,
                                  policy_question, policy_answer, policy_score)

    # Separate return variables in best_answer
    final_answer = best_answer[0]
    final_score = best_answer[1]

    # Handling Yes/No Answer Questions
    if yes_no_question:
        yes_answer = yes_no_determination(question, final_answer)
        if yes_answer:
            print("Final Answer: Yes")
            print("Final Score: " + str(final_score))
        else:
            print("Final Answer: No")
            print("Final Score: " + str(final_score))

    # Handling Short Answer Questions
    else:
        # Print final answer
        print("Final Answer: " + final_answer)
        print("Final Score: " + str(final_score))


main()
