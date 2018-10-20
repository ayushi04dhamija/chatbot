import nltk
import numpy as np
import random
import string
f=open('chatbot.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
sent_tokens[:2]
word_tokens[:5]
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
GREETING_INPUTS = ("Hello! I'm Elth. I'm your personal assistant.Before starting please tell me your first name")
GREETING_OUTPUTS = ("Srinath","Akula")

GREETING_INPUTS = ("And your gender?")
GREETING_OUTPUTS = ("Male","Female")

GREETING_INPUTS = ("May I know your age?")
GREETING_OUTPUTS = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15




def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
