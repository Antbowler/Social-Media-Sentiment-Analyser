import sys
import os.path
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt

def get_scores():
    fname = sys.argv[1]
    if(not os.path.isfile(fname)):
        print(f"Err: file {fname} doesn't exist")
        return
    
    file = open(fname, "r", encoding="utf-8")
    posts = file.readlines()
    file.close()

    while(posts.count("\n")):
        posts.remove("\n")

    analyzer = SentimentIntensityAnalyzer()
    compound_scores = []
    for i, post in enumerate(posts):
        vs = analyzer.polarity_scores(post)
        compound_scores.append(vs['compound'])
    
    return compound_scores

def split_scores(scores):
    positive_scores = []
    neutral_scores = []
    negative_scores = []

    for score in scores:
        if score >= 0.05:
            positive_scores.append(score)
        if score > -0.05 and score < 0.05:
            neutral_scores.append(score)
        if score <= -0.05:
            negative_scores.append(score)
    
    return positive_scores, neutral_scores, negative_scores
    


def display_stats(scores, positive_scores, neutral_scores, negative_scores):
    topic = sys.argv[1].replace(".txt", "")

    total_scores = len(scores)
    num_of_pos_scores = len(positive_scores)
    num_of_neu_scores = len(neutral_scores)
    num_of_neg_scores = len(negative_scores)

    average_score = np.mean(scores)

    overall_rating = ""
    if average_score >= 0.05:
        overall_rating = "Positive"
    if average_score > -0.05 and average_score < 0.05:
        overall_rating = "Neutral"
    if average_score <= -0.05:
        overall_rating = "Negative"



    print(f"\nTopic: {topic.title()}")
    print("-"*50)
    print(
        f"Total posts: {total_scores}\n\n" \
        f"Average score for all posts: {average_score} ({overall_rating})\n\n" \
        f"Positive posts: {num_of_pos_scores}\n\n" \
        f"Neutral posts: {num_of_neu_scores}\n\n" \
        f"Negative posts: {num_of_neg_scores}\n")
    
    bar_x = np.array(["Positive Posts", "Neutral Posts", "Negative Posts"])
    bar_y = np.array([num_of_pos_scores, num_of_neu_scores, num_of_neg_scores])
    
    plt.bar(bar_x, bar_y)
    plt.show()

    pie_labels = np.array(["Positive Posts", "Neutral Posts", "Negative Posts"])
    pie_y = np.array([num_of_pos_scores, num_of_neu_scores, num_of_neg_scores])

    plt.pie(pie_y, labels=pie_labels)
    plt.show()


def main():
    if(len(sys.argv) != 2):
        print("Usage: python sentiment_analyser.py {filename}.txt")
        return
    
    scores = get_scores()
    positive_scores, neutral_scores, negative_scores = split_scores(scores)

    display_stats(scores, positive_scores, neutral_scores, negative_scores)


    
if __name__ == "__main__":
    main()