import json
import operator
import sys

def main():
  tfile = open(sys.argv[1])
  total = 0
  ht = {}
  
  for line in tfile:
    tweet = json.loads(line)
    if "entities" in tweet and "hashtags" in tweet["entities"]:
      hashtags = tweet["entities"]["hashtags"]
      for hashtag in hashtags:
        if ("text" in hashtag):
          tag = hashtag["text"].lower()
          if (tag):
            total += 1
            freq = ht[tag] if tag in ht else 0
            ht[tag] = freq + 1

  sorted_ht = sorted(ht.items(), key=operator.itemgetter(1), reverse = True)[0:10]
  for (k, v) in sorted_ht:
    print k, v

if __name__ == '__main__':
    main()
