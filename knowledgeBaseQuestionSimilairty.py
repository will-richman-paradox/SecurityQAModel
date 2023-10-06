import json
import pandas as pd
import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"

# Create a DataFrame of the Paradox Security Knowledge Base
df = pd.read_csv("/Users/will.richman/Downloads/ParadoxSecurityKnowledgeBase.csv", usecols=['Question / Topic', 'Answer'])

# Questions Preparation
df.dropna(subset=['Question / Topic'], inplace=True)
questions = df['Question / Topic'].tolist()


# Answers Preparation
df.dropna(subset=['Answer'], inplace=True)
answers = df['Answer'].tolist()


def query(payload):

    response = requests.post(API_URL, json=payload)
    return response.json()


def get_answer(user_question):
    data = query(
        {
            "inputs": {
                "source_sentence": user_question,
                "sentences": questions
            }
        })

    max_score = 0.0
    iterator = 0
    index = 0
    for num in data:
        if num > max_score:
            max_score = num
            index = iterator
        iterator += 1

    return questions[index], answers[index], max_score
