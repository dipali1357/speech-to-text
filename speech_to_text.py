import numpy as np
import tensorflow as tf
import re
import time
import nltk.data 
import os 
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    text = r.listen(source)





# Doing a first cleaning of the texts
def text_preprocessing(text):  
# Loading PunktSentenceTokenizer using English pickle file 
    tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle') 
    tokenizer.tokenize(text) 
    text = text.lower()
    text = re.sub(r"C M", "CM", text)
    text = re.sub(r"TRIPLE A", "AAA", text)
    text = re.sub(r"two dollars", "$2", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]", "", text)
    return text


clean_txt = []
for word in text:
    k = text_preprocessing(word)
    clean_txt.append(k)
 
print(clean_txt)



