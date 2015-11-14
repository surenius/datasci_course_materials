import json
import string
import sys

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
    if "text" in tweet:
      cleartext = ''.join(ch for ch in tweet["text"].lower() if ch in allowed)
      tweets.append(string.split(cleartext))
    else:
      tweets.append(list())
  
  return tweets

def deriveSentiments(tweets, scores):
  tweetScores = []
  for tweet in tweets:
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

    tweetScores.append(score)
    
  for v in tweetScores:
    print v

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    scores = loadAfinn(sent_file)
    tweets = loadTweets(tweet_file)

    deriveSentiments(tweets, scores)

if __name__ == '__main__':
    main()
