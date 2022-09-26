import csv;
import pandas as pd
import numpy as np
import re
import string
import textstat
import nltk
from transformers import pipeline
import pprint

# Step 1: Read in Data



def clean_text(text):
    # Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# die Artikel und Textpassagen aus dem Excel-File werden in das Programm hochgeladen
with open('Quellen.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for columns in csv_reader:
        # An dieser Stelle werden die Quellen von GEFEG einzelnd untersucht
        if columns[0] == 'ECOSIO':
            Ecosio_cleaned_text = clean_text(columns[3])
            Ecosio_normal_text = columns[3]

with open('Quellen.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for columns in csv_reader:
        # An dieser Stelle werden die Quellen von GEFEG einzelnd untersucht
        if columns[0] == 'GEFEG':
            GEFEG_cleaned_text = clean_text(columns[3])
            GEFEF_normal_text = columns[3]

# Die beiden Textkorpusse werden jeweils seperat auf ihre Lesefreundlichkeit gemessen.
# Da die Satzzeichen bei diesem Test eine wichtige Rolle spielen, wurden für diesen Test die orginalen Textpassagen ohne Überabrietung genutzt.
print('GEFEG Flesh Reading Score: ' + str(textstat.flesch_reading_ease(GEFEF_normal_text)))
print('Ecosio Flesh Reading Score: ' + str(textstat.flesch_reading_ease(Ecosio_normal_text)))



words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
stopwords = nltk.corpus.stopwords.words("english")
#Wörter ohne Stoppwörter (aber alle in lower case)
words = [w for w in words if w.lower() not in stopwords]

# use str.isalpha to filter out punctuation
pprint((nltk.word_tokenize(GEFEG_cleaned_text), width=79, compact=True)

#sentiment_pipeline = pipeline("sentiment-analysis")
#data = ["I love you", "I hate you"]
#sentiment_pipeline(data)