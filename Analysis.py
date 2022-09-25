import csv;
import pandas as pd
import numpy as np
import textstat
import re
import string
import textstat
import nltk
from transformers import pipeline


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


print('GEFEG Flesh Reading Score: ' + textstat.flesch_reading_ease(GEFEF_normal_text))
print('Ecosio Flesh Reading Score: ' + textstat.flesch_reading_ease(Ecosio_normal_text))


sentiment_pipeline = pipeline("sentiment-analysis")
#data = ["I love you", "I hate you"]
#sentiment_pipeline(data)