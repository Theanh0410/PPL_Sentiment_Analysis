import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# List of stopwords 
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    return list(
        filter(
            #Remove stopwords
            lambda token: token not in STOPWORDS,
            # Lowercase , Remove punctuation , Tokenizes
            map(
                lambda word: word.lower().translate(str.maketrans('', '', string.punctuation)),
                word_tokenize(text)
            )
        )
    )

