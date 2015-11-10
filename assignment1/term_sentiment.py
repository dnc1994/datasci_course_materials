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
    new_scores = {}
    for line in sent_file.readlines():
        term, score = line.split('\t')
        scores[term] = int(score)

    for line in tweet_file.readlines():
        new_terms = []
        tweet = json.loads(line.strip())
        score = 0
        for term in tweet.get('text', '').strip().split(' '):
            term = ''.join(filter(lambda x: x.isalpha(),term))
            if not term:
                continue
            if term in scores.keys():
                score += scores.get(term, 0)
            elif term not in new_terms:
                new_terms.append(term)                       
            
        # update new term scores based on current tweet score    
        for term in new_terms:
            new_scores[term] = score + new_scores.get(term, 0)
      
    for term, score in new_scores.iteritems():
        print term, score
        

if __name__ == '__main__':
    main()
