import sys
import json

DEBUG = 0


def main():
    if DEBUG:
        tweet_file = open('handin-1.json')
    else:
        tweet_file = open(sys.argv[1])
            
    total_count = 0
    term_count = {}
        
    for line in tweet_file.readlines():
        
        tweet = json.loads(line.strip())
        
        for term in tweet.get('text', '').strip().split(' '):
            term = ''.join(filter(lambda x: x.isalpha(),term))
            if not term:
                continue
            
            total_count += 1
            term_count[term] = 1 + term_count.get(term, 0)
            
    for term, count in term_count.iteritems():
        print term, (float(count) / total_count)
        
        
if __name__ == '__main__':
    main()