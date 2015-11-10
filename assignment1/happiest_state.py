import sys
import json

DEBUG = 0

STATES = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def main():

    if DEBUG:
        sent_file = open('AFINN-111.txt')
        tweet_file = open('three_minutes_tweets.json')
    else:
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])
        
    state_scores = {}
    sent_scores = {}
    for line in sent_file.readlines():
        term, score = line.split("\t")
        sent_scores[term] = int(score)
        
    for line in tweet_file.readlines():
        try:
            score = 0
            state = None
            tweet = json.loads(line.strip())

            place = tweet.get("place", False)

            if place and place["country_code"] == u"US":
                first_name, last_name = place["full_name"].split(", ")

                if place["place_type"] == u"city":
                    if last_name in STATES:
                        state = last_name

                elif place["place_type"] == u"admin":
                    for abbr, name in STATES.iteritems():
                        if name.lower() == first_name.lower():
                            state = abbr

                if state:
                    for term in tweet.get('text', '').strip().split(' '):
                        term = ''.join(filter(lambda x: x.isalpha(),term))
                        if not term:
                            continue
                        score += sent_scores.get(term, 0)
            
                    state_scores[state] = score + state_scores.get(state, 0)

        except:
            pass

    state_scores = [(v, k) for k, v in state_scores.iteritems()]
    print sorted(state_scores, reverse=True)[0][1]

if __name__ == '__main__':
    main()