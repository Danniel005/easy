sentence1 = "I will walk 500 miles and I would walk 500 more. Just to be the man who walks " + \
            "a thousand miles to fall down at your door!"
sentence2 = "I played the play playfully as the players were playing in the play with playfullness"

from nltk import word_tokenize, sent_tokenize

print('Tokenized words:', word_tokenize(sentence1))
print("\n")

print('Tokenized sentences:', sent_tokenize(sentence1))
print("\n")

from nltk import pos_tag
print("---------POS Tagging------------")
token = word_tokenize(sentence1) + word_tokenize(sentence2)
print('POS tagged:', pos_tag(token))
print("\n")

print("---------Stop-Words Removal------------")
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
token = word_tokenize(sentence1)
cleaned_token = []
for word in token:
    if word not in stop_words:
        cleaned_token.append(word)
print("Unclean version:", token)
print("\n")
print("Cleaned version:", cleaned_token)
print("\n")

print("---------Stemming------------")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
token = word_tokenize(sentence2)
stemmed = [stemmer.stem(word) for word in token]  
print("Stemmed words:", stemmed)
print("\n")

print("---------Lemmatization------------")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
token = word_tokenize(sentence2)
lemmatized = [lemmatizer.lemmatize(word) for word in token]
print("Lemmatized words:", lemmatized)
print("\n")