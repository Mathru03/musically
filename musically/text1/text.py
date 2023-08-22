import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Download necessary resources for NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Sample raw lyrics text
raw_lyrics = '''Don't you know I'm no good for you?
I've learned to lose you, can't afford to
Tore my shirt to stop you bleedin'
But nothin' ever stops you leavin'
Quiet when I'm comin' home and I'm on my own
I could lie, say I like it like that, like it like that
I could lie, say I like it like that, like it like that
Don't you know too much already?
I'll only hurt you if you let me
Call me friend but keep me closer (call me back)
And I'll call you when the party's over
Quiet when I'm comin' home and I'm on my own
And I could lie, say I like it like that, like it like that
Yeah, I could lie, say I like it like that, like it like that
But nothin' is better sometimes
Once we've both said our goodbyes
Let's just let it go
Let me let you go
Quiet when I'm comin' home and I'm on my own
I could lie, say I like it like that, like it like that
I could lie, say I like it like that, like it like that'''

# Tokenize lyrics into words
def tokenize_lyrics(lyrics):
    words = word_tokenize(lyrics)
    return words

# Clean and preprocess lyrics
def preprocess_lyrics(lyrics):
    # Tokenize
    words = tokenize_lyrics(lyrics)

    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in words if re.match(r'\w', word)]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return words

# Preprocess raw lyrics
preprocessed_lyrics = preprocess_lyrics(raw_lyrics)

# Print preprocessed lyrics
print(preprocessed_lyrics)