#Using textblob library to analyze the sentiment of a sentence

from textblob import TextBlob, Word
blob = TextBlob("I hate python")
print(blob.sentiment)

for b in blob.sentences:
    print(b.sentiment)