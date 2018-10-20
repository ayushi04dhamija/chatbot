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

def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    bot_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response=bot_response+"I couldn't quite get how that response can be your age :/ Please enter your valid age."
        return bot_response
    else:
        bot_response = bot_response+sent_tokens[idx]
        return bot_response
 flag=True
print("BOT: My name is Elth. I am your personal assistant")

while(flag==True):
    user_response = input()
 
    if(user_response.isdigit()):
       print("Congratulations! Registration Successful.")
    else
    flag==False
        
        


