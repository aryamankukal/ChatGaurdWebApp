import regex as re

def deleteSmallWords(text):
	phrase = []
	for word in text.split():
		if len(word) > 3:
			phrase.append(word)
	phrase = ' '.join(phrase)
	return phrase

def cleanText(text):
	text = text.lower().split()

	stops = set(stopwords.word('english'))
	text = [x for x in text if not x in stops and len(x) >= 3]

	text = " ".join(text)  
	
	text = re.sub(r'https?://[A-Za-z0-9./]+', 'url', text)
	text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
	text = re.sub(r"what's", "what is ", text)
	text = re.sub(r"\'s", " ",text)
	text = re.sub(r"\'ve", " have ", text)
	text = re.sub(r"n't", " not ", text)
	text = re.sub(r"i'm", "i am ", text)
	text = re.sub(r"\'re", " are ", text)
	text = re.sub(r"\'d", " would ", text)
	text = re.sub(r"\'ll", " will ", text)
	text = re.sub(r",", " ", text)
	text = re.sub(r"\.", " ", text)
	text = re.sub(r"!", "!", text)
	text = re.sub(r"\/", "", text)
	text = re.sub(r"\^", " ^ ", text)
	text = re.sub(r"\+", " + ", text)
	text = re.sub(r"\-", " - ", text)
	text = re.sub(r"\=", " = ", text)
	text = re.sub(r"'", " ", text)
	text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
	text = re.sub(r":", " : ", text)
	text = re.sub(r" e g ", " eg ", text)
	text = re.sub(r" b g ", " bg ", text)
	text = re.sub(r" u s ", " american ", text)
	text = re.sub(r"\0s", "0", text)
	text = re.sub(r" 9 11 ", "911", text)
	text = re.sub(r"e - mail", "email", text)
	text = re.sub(r"j k", "jk", text)
	text = re.sub(r"\s{2,}", " ", text)
	text = re.sub(r"@[A-Za-z0-9]+", "", text)
	text = re.sub(r"(\w)\1{2,}", "\1\1", text)
	text = re.sub(r"\w(\w)\1{2}", "", text)

	text = EliminaParolePiccole(text)

	return text

def deleteNonAlphaWords(sentence):
	return ' '.join([word for word in sentence.split() if word.isalpha()])

tokenizer = Tokenizer(num_words=DIM_DIZIONARIO, lower=True)
tokenizer.fit_on_texts(X_trainClean)
tokenizer.texts_to_sequences(X_trainClean)

ListaTrainIndex = [phrase from phrase in X_trainIndex]
pad_sequences(ListaTrainIndex, maxlen=INPUT_LENGTH)

embeddings_Glove = dict()
testo = open(path, )