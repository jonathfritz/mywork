import csv;
import pandas as pd
import numpy as np

import re
import string

import nltk


# Step 1: Read in Data



def clean_text(text):
    # Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

with open('Quellen.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for columns in csv_reader:
        # defining GEFEG as the analyzed target
        #if columns[0] == 'GEFEG':
            print(columns)




#textstat.flesch_reading_ease(text)

#pip install -q transformers
#from transformers import pipeline
#sentiment_pipeline = pipeline("sentiment-analysis")
#data = ["I love you", "I hate you"]
#sentiment_pipeline(data)