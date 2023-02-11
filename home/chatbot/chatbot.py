import random
import json
import pickle
import numpy as np
import os
import nltk
from nltk.stem import WordNetLemmatizer
# nltk.download("punkt")
# nltk.download("wordnet")
# nltk.download("omw-1.4")
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.load(open('./home/chatbot/intents.json'))

words = pickle.load(open('./home/chatbot/words.pkl', 'rb'))
classes = pickle.load(open('./home/chatbot/classes.pkl', 'rb'))

model = load_model('./home/chatbot/chatbotmodel.h5')

def clean_up_sentence (sentence):
  sentence_words = nltk.word_tokenize(sentence)
  sentence_words
  [lemmatizer.lemmatize (word) for word in sentence_words]
  return sentence_words

def bag_of_words (sentence):
  sentence_words = clean_up_sentence(sentence)
  bag = [0] * len(words)
  for w in sentence_words:
    for i, word in enumerate (words):
      if word == w:
        bag[i] = 1
  return np.array(bag)

"""def predict_class(sentence):
  bow = bag_of_words(sentence)
  res = model.predict(np.array([bow]))[0] 
  print("---------------------------------------->", res)
  ERROR_THRESHOLD = 0.25
  results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
  print("resssss-->",results)
  index, value = max(results, key=lambda x: x[1])
  results.sort(key=lambda x: x[results.index(value)], reverse=True)
  return_list = []
  for r in results:
    return_list.append({'intent': classes [r[0]], 'probability': str(r[1])})
  return return_list

def get_responses(intents_list, intents_json):
  tag = intents_list[0]['intent']
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if i['tag'] == tag:
      result =  random.choice(i['responses'])
      break
  return result

def message(message):
    ints = predict_class(message)
    res = get_responses(ints, intents)
    return res"""

def predict_class(sentence):
  bow = bag_of_words(sentence)
  res = model.predict(np.array([bow]))[0]
  print(res)
  result = []
  m = res[0]
  ind = 0
  for i in range(len(res)):
    if res[i]>m:
      m = res[i]
      ind = i 
  result.append(({'intent': classes [i], 'probability': str(m)}))
  return result



def get_responses(intents_list, intents_json):
  tag = intents_list[0]['intent']
  
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if i['tag'] == tag:
      result =  random.choice(i['responses'])
      break
  return result

def message(message):
    ints = predict_class(message)
    res = get_responses(ints, intents)
    return res