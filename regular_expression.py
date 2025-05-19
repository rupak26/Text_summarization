import os , string , re
import nltk 
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def read_chat_log(file):
    with open(file , 'r') as f:
        return f.readlines()

def parse_chat(lines):
    user_msgs = []
    ai_msgs = []
    for line in lines:
        if line.startswith('User:'):
            user_msgs.append(line[len('User:'):].strip())
        elif line.startswith('AI:'):
            ai_msgs.append(line[len('AI:'):].strip())
    return user_msgs, ai_msgs

def tfidf_keywords(messages, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(messages)
    scores = X.sum(axis=0).A1
    terms = vectorizer.get_feature_names_out()
    ranked_terms = sorted(zip(terms, scores), key=lambda x: x[1], reverse=True)
    return ranked_terms[:top_n]

def generate_summary(user_msgs, ai_msgs, use_tfidf=True):
    total_msgs = len(user_msgs) + len(ai_msgs)
    combined = user_msgs + ai_msgs
    if use_tfidf:
       keywords = tfidf_keywords(combined)
    

def process_chat_file(use_tfidf=True):
    lines = read_chat_log('text.txt')
    user_msgs, ai_msgs = parse_chat(lines)
    summary = generate_summary(user_msgs , ai_msgs , use_tfidf=use_tfidf)
    print(user_msgs , ai_msgs)


def main():
    process_chat_file()

if __name__ == "__main__":
    main()