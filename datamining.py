from ntscraper import Nitter

##add search term in here
search_term = "" 
##limit of tweets to be retrieved
num_tweets = 100

scraper = Nitter(log_level=1, skip_instance_check=False)

def fetch_tweets():
    tweets_dict = scraper.get_tweets(search_term, number=num_tweets)
    tweets = []

    for tweet in tweets_dict['tweets']:
        if tweet["text"] != None and tweet["text"] != "":
            tweets.append(tweet["text"])
    
    return tweets

def main():
    tweets = fetch_tweets()

    fname = f"{search_term}.txt"
    f = open(fname.lower(), "a", encoding="utf-8")

    for tweet in tweets:
        f.write(f"{tweet}\n\n")

    f.close()

if __name__ == "__main__":
    main()
