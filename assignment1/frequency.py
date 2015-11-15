import json
import string
import sys

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

def calcFreq(tweets):
  termFreqs = {}
  total = 0
  stopwords = set() # set(["the", "aux", "des", "pre", "out", "off"])  
  
  for tweet in tweets:
    for word  in tweet:
      if len(word) > 2 and not (word in stopwords):
        total += 1
        freq = termFreqs[word] if word in termFreqs else 0
        termFreqs[word] = freq + 1

  for (word, freq) in termFreqs.items():
    print word, float(freq) / float(total)

def main():
    tweet_file = sys.argv[1]
    
    tweets = loadTweets(tweet_file)

    calcFreq(tweets)

if __name__ == '__main__':
    main()
