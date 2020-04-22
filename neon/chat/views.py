# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib import auth
# from django.template.context_processors import csrf
# from django.contrib.auth import *
# from django.contrib.auth.models import User
# from login.models import *
# from .models import *
# import os
# # Data Procesing imports

# import numpy as np
# import pandas as pd
# from nltk.corpus import stopwords
# import spacy
# from nltk.tokenize import word_tokenize
# import pickle
# from keras.preprocessing.sequence import pad_sequences
# from keras.models import load_model


# # Global variables

# chatt = []
# stop_words = set(stopwords.words('english'))
# nlp = spacy.load('en')
# with open(os.path.dirname(os.path.abspath(
#         __file__))+'/intent_tokenizer.pkl', 'rb') as input:
#     global intent_tokenizer
#     intent_tokenizer = pickle.load(input)

# with open(os.path.dirname(os.path.abspath(
#         __file__))+'/entity_tokenizer.pkl', 'rb') as input:
#     global entity_tokenizer
#     entity_tokenizer = pickle.load(input)

# entity_model = load_model(os.path.dirname(os.path.abspath(
#     __file__))+'/entity_model.h5')

# intent_model = load_model(os.path.dirname(os.path.abspath(
#     __file__))+'/intent_model.h5')


# # Create your views here.


# # def load_intent():
# #     intent = []
# #     for row in intents.objects.all():
# #         intent.append(row.Intent)
# #     global unique_intent
# #     unique_intent = list(set(intent))
# #     return intent


# # def load_entities():
# #     entity = []
# #     for row in entities.objects.all():
# #         entity.append(row.Entity)
# #     global unique_entity
# #     unique_entity = list(set(entity))
# #     return entity


# def get_unique_entity():
#     unique_entity = []
#     for row in UniqueEntity.objects.all():
#         unique_entity.append(row.Entity)
#     return unique_entity


# def get_unique_intent():
#     unique_intent = []
#     for row in UniqueIntent.objects.all():
#         unique_intent.append(row.Intent)
#     print(unique_intent)
#     return unique_intent


# def padding_doc(encoded_doc):
#     return(pad_sequences(encoded_doc, maxlen=7, padding="post"))


# @login_required(login_url='/login/')
# def index(request):
#     c = {}
#     c.update(csrf(request))
#     return render(request, "chatBot.html", c)


# def process(request):
#     c = {}
#     c.update(csrf(request))
#     msg = request.POST.get('msg', '')
#     entity = predict_entity(msg, get_unique_entity())
#     intent = predict_intent(msg, get_unique_intent())
#     chatt.append(msg)
#     for ent in UniqueEntity.objects.all():
#         if ent.Entity == entity:
#             entid = ent.EId
#     for it in UniqueIntent.objects.all():
#         if it.Intent == intent:
#             intid = it.IId
#     for resp in Responses.objects.all():
#         if resp.Entity_id.EId == entid and resp.Intent_id.IId == intid:
#             chatt.append(resp.Response)
#             break
#     c['chat'] = chatt
#     c['isopen']: 'true'
#     return render(request, "chatBot.html", c)


# def predict_entity(text, classes):
#     clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
#     doc = nlp(clean)
#     s = ""
#     for w in doc:
#         s = s + " " + w.lemma_
#     test_word = word_tokenize(s)
#     test_word = [w.lower()
#                  for w in test_word if not w in stop_words and w != 'i' and w != 'I']
#     test_ls = entity_tokenizer.texts_to_sequences(test_word)
#     if [] in test_ls:
#         test_ls = list(filter(None, test_ls))
#     test_ls = np.array(test_ls).reshape(1, len(test_ls))
#     x = padding_doc(test_ls)
#     # graph = tf.compat.v1.get_default_graph()
#     # with graph.as_default():
#     pred = entity_model.predict_proba(x)
#     classes = np.array(classes)
#     ids = np.argsort(-pred[0])
#     classes = classes[ids]
#     # predictions = -np.sort(-pred[0])
#     return classes[0]


# def predict_intent(text, classes):
#     clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
#     doc = nlp(clean)
#     s = ""
#     for w in doc:
#         s = s + " " + w.lemma_
#     test_word = word_tokenize(s)
#     test_word = [w.lower()
#                  for w in test_word if not w in stop_words and w != 'i' and w != 'I']
#     test_ls = intent_tokenizer.texts_to_sequences(test_word)
#     if [] in test_ls:
#         test_ls = list(filter(None, test_ls))
#     test_ls = np.array(test_ls).reshape(1, len(test_ls))
#     x = padding_doc(test_ls)
#     # graph = tf.compat.v1.get_default_graph()
#     # with graph.as_default():
#     pred = intent_model.predict_proba(x)
#     classes = np.array(classes)
#     ids = np.argsort(-pred[0])
#     classes = classes[ids]
#     # predictions = -np.sort(-pred[0])
#     return classes[0]
