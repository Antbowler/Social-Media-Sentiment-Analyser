# Basic Social Media Sentiment Analyser
Basic python scripts to gather tweets on a certain topic and then conduct sentiment analysis on them to determine number of postive, negative and netural tweets.

## Requirements
- ntscraper: https://github.com/bocchilorenzo/ntscraper
- vaderSentiment: https://github.com/cjhutto/vaderSentiment
- numpy: https://github.com/numpy/numpy
- matplotlib: https://github.com/matplotlib/matplotlib

## Usage
Edit datamining.py and change search_term to what you want to search, additionally can edit num_tweets to change limit on number of tweets to be retrieved at once.

Run datamining.py and it will produce a textfile {search_term}.txt containing the text body of all the tweets retrieved. If you are getting rate limited may need to run script regularly at different points in time.

Running datamining.py multiple times may cause the text files to get filled with duplicate tweets so run cleanup.py "{search_term}.txt" to remove duplicate tweets.

Once you have gathered enough tweets and have cleaned up your text file run sentiment_analyser.py "{search_term}.txt".
