import json
import string
import sys

def lines(fp):
    print str(len(fp.readlines()))

def loadAfinn(sentFilePath):
  afinnfile = open(sentFilePath)
  scores = {}  # initialize an empty dictionary
  for line in afinnfile:
    term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  
  return scores  

def loadTweets(tweetsFilePath):
  tfile = open(tweetsFilePath)
  tweets = [];
  allowed = set(string.letters + string.whitespace + '-')
  
  for line in tfile:
    tweet = json.loads(line)
    if "text" in tweet:
      txt = tweet["text"].lower()
      words = []
      for word in string.split(txt):
        if (allowed.issuperset(set(word))):
          words.append(word)
      tweets.append(words)
    else:
      tweets.append(list())
  
  return tweets

def findNewTerms(tweets, scores, newTermsScores):
  changed = False
  for tweet in tweets:
    if (findNewTermsInTweet(tweet, scores, newTermsScores)):
      changed = True
      
  return changed

def findNewTermsInTweet(tweet, scores, newTermsScores):
  changed = False
  
  for (i, term) in enumerate(tweet):
    if len(term) > 2 and not (term in scores):
      leftScore = 0
      if (i > 0 and tweet[i - 1] in scores):
        leftScore = scores[tweet[i - 1]]
         
      rightScore = 0  
      if (i < (len(tweet) - 1) and tweet[i + 1] in scores):
        rightScore = scores[tweet[i + 1]]
      
      if (leftScore != 0 or rightScore != 0):
        score = 0
        if leftScore == 0 and rightScore != 0:
          score = rightScore
        else:
          if leftScore != 0 and rightScore == 0:
            score = leftScore
          else:
            score = float(leftScore + rightScore) / 2
        
        newTermsScores[term] = score
        changed = True
      
  return changed

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    scores = loadAfinn(sent_file)
    tweets = loadTweets(tweet_file)

    newTermsScores = {}
    while (findNewTerms(tweets, scores, newTermsScores)):
      pass
    
    for (term, score) in newTermsScores.items():
      print term, score

if __name__ == '__main__':
    main()
