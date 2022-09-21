import csv;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# open and use the source file with all the text messages that should be analysed
with open('Quellen.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for columns in csv_reader:
        # defining GEFEG as the analyzed target
        if columns[0] == 'GEFEG':
            print(clean_text(columns[3]))




