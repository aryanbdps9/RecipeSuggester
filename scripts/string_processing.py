import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def process_text(text):
	text_lower=text.lower()
	tokens_without_sw=remove_stopwords(text_lower)
	unique_words=[e for e in tokens_without_sw if e.isalnum()]
	lemma = [lemmatizer.lemmatize(e) for e in unique_words]
	return lemma

def remove_stopwords(text):
    text_tokens = word_tokenize(text)
    tokens_without_sw = set([word for word in text_tokens if not word in stopwords.words()])
    return tokens_without_sw


