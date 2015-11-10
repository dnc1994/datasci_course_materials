import sys
import json

DEBUG = 0


def main():
    if DEBUG:
        tweet_file = open('three_minutes_tweets.json')
    else:
        tweet_file = open(sys.argv[1])
        
    hashtag_count = {}
        
    for line in tweet_file.readlines():
        try:
            tweet = json.loads(line.strip())

            hashtags = tweet['entities']['hashtags']
            for hashtag in hashtags:
                hashtag = hashtag['text']
                hashtag_count[hashtag] = 1 + hashtag_count.get(hashtag, 0)

        except:
            pass

    hashtag_count = [(v, k) for k, v in hashtag_count.iteritems()]
    hashtag_count = sorted(hashtag_count, reverse=True)
    
    for count, hashtag in hashtag_count[:10]:
        print hashtag, count
        

if __name__ == '__main__':
    main()