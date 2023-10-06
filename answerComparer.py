

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
        best_answer = pol_answer
        best_score = pol_score
        print("\n\nKB Answer: " + kb_answer)
        print("KB Score: " + str(kb_score) + "\n\n")

    return best_answer, best_score
