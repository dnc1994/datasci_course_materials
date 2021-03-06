import sys
import json

DEBUG = 0


def main():
    if DEBUG:
        sent_file = open('AFINN-111.txt')
        tweet_file = open('handin-1.json')
    else:
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])
            
    scores = {}
    for line in sent_file.readlines():
        term, score = line.split('\t')
        scores[term] = int(score)

    for line in tweet_file.readlines():
        tweet = json.loads(line.strip())
        score = 0
        for term in tweet.get('text', '').strip().split(' '):
            term = ''.join(filter(lambda x: x.isalpha(),term))
            if not term:
                continue
            score += scores.get(term, 0)
        print score 

        
if __name__ == '__main__':
    main()
