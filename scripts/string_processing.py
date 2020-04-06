import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

NoAlphaNumWhiteSpacePattern = re.compile('([^\s\w]|_)+')
NoAlphaWhiteSpacePattern = re.compile('([^\sa-zA-Z])+')

lemmatizer = WordNetLemmatizer()
stopwords_set = set(stopwords.words())

def process_text(text):
	# text = NoAlphaNumWhiteSpacePattern.sub('', text)
	text = NoAlphaWhiteSpacePattern.sub('', text)
	text_lower=text.lower()
	tokens_without_sw=remove_stopwords(text_lower)
	unique_words=[e for e in tokens_without_sw if e.isalnum()]
	lemma = [lemmatizer.lemmatize(e) for e in unique_words]
	return lemma

def remove_stopwords(text):
    text_tokens = word_tokenize(text)
    tokens_without_sw = set(filter(lambda x: x not in stopwords_set, text_tokens))
    # tokens_without_sw = set([word for word in text_tokens if not word in stopwords.words()]) # TOO SLOW!
    return tokens_without_sw


