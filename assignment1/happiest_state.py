import json
import string
import sys

us_state_abbrev = {
    'ALABAMA': 'AL',
    'ALASKA': 'AK',
    'ARIZONA': 'AZ',
    'ARKANSAS': 'AR',
    'CALIFORNIA': 'CA',
    'COLORADO': 'CO',
    'CONNECTICUT': 'CT',
    'DELAWARE': 'DE',
    'FLORIDA': 'FL',
    'GEORGIA': 'GA',
    'HAWAII': 'HI',
    'IDAHO': 'ID',
    'ILLINOIS': 'IL',
    'INDIANA': 'IN',
    'IOWA': 'IA',
    'KANSAS': 'KS',
    'KENTUCKY': 'KY',
    'LOUISIANA': 'LA',
    'MAINE': 'ME',
    'MARYLAND': 'MD',
    'MASSACHUSETTS': 'MA',
    'MICHIGAN': 'MI',
    'MINNESOTA': 'MN',
    'MISSISSIPPI': 'MS',
    'MISSOURI': 'MO',
    'MONTANA': 'MT',
    'NEBRASKA': 'NE',
    'NEVADA': 'NV',
    'NEW HAMPSHIRE': 'NH',
    'NEW JERSEY': 'NJ',
    'NEW MEXICO': 'NM',
    'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC',
    'NORTH DAKOTA': 'ND',
    'OHIO': 'OH',
    'OKLAHOMA': 'OK',
    'OREGON': 'OR',
    'PENNSYLVANIA': 'PA',
    'RHODE ISLAND': 'RI',
    'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD',
    'TENNESSEE': 'TN',
    'TEXAS': 'TX',
    'UTAH': 'UT',
    'VERMONT': 'VT',
    'VIRGINIA': 'VA',
    'WASHINGTON': 'WA',
    'WEST VIRGINIA': 'WV',
    'WISCONSIN': 'WI',
    'WYOMING': 'WY',
}

def lines(fp):
    print str(len(fp.readlines()))

def loadAfinn(sentFilePath):
  afinnfile = open(sentFilePath)
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  
  return scores  

def loadTweets(tweetsFilePath):
  tfile = open(tweetsFilePath)
  tweets = [];
  allowed = set(string.letters + string.whitespace + '-')
  
  for line in tfile:
    tweet = json.loads(line)
    state = identifyState(tweet)
    if "text" in tweet and state:
      cleartext = ''.join(ch for ch in tweet["text"].lower() if ch in allowed)
      tweets.append((state, string.split(cleartext)))
  
  return tweets

def identifyState(tweet):
  state = stateByPlace(tweet)
  if not state:
    user = tweet.get("user")
    if user:
      state = isState(user["location"])
      
    if not state:
      state = stateByPlace(tweet.get("retweeted_status"))
           
  return state

def stateByPlace(container):
  if container:
    place = container.get("place")
    if place:
      countryCode = place.get("country_code")
      if countryCode and (countryCode.upper() == "US"):
        name = isState(place.get("name"))
        if (name):
          return name
        
        name = isState( place.get("full_name"))
        if (name):
          return name

  return ""

def isState(s):
  global us_state_abbrev
  if s:
    for name in s.split():
      name = name.strip(string.punctuation).upper()
      if name in us_state_abbrev:
        return us_state_abbrev[name]
      
      if name in us_state_abbrev.values():
        return name
  
  return ""   

def deriveSentiments(tweets, scores):
  stateScores = {}
  for (state, tweet) in tweets:
    score = 0
    # search for three-word phrases, then for two-word, then just words
    skipwords = set()
    if tweet:
      for l in [3, 2, 1]:
        for i in xrange(len(tweet) - l + 1):
          words = tweet[i:i+l]
          term = string.join(words, ' ')
          if term in scores and not term in skipwords:
            skipwords.update(words)
            score += scores[term]

    scorevals = stateScores[state] if state in stateScores else []
    scorevals.append(score) 
    stateScores[state] = scorevals
  
  maxstate = ""
  maxv = -9999  
  for (state, scorevals) in stateScores.items():
    stateAvg = float(sum(scorevals))/len(scorevals)
    if (stateAvg > maxv):
      maxv = stateAvg
      maxstate = state

  print maxstate

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    scores = loadAfinn(sent_file)
    tweets = loadTweets(tweet_file)

    deriveSentiments(tweets, scores)

if __name__ == '__main__':
    main()
