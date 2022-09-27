import csv
import pandas as pd
import numpy as np
import re
import string
import textstat
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer



def clean_text(text):
    # Diese Funktion reduziert die Komplexität der Textpassagen.
    # Sie entfernt Satzzeichen, setzt bei jedem Wort die Kleinschreibung durch und entfernt Worte, in denen Nummern beinhaltet sind
    text = text.lower()
    text = re.sub('\[.*?]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def tokenize_text(text):
    # Diese Funktion zerteilt den Text in einzelnde Buchstaben und zählt die Häufigkeit der einzenen Wörter.
    # Die fünf Wörter, die am häufigsten erwähnt werden, sind das abschließende Ergebnis
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [w for w in word_tokens if not w.lower() in stop_words]
    for w in word_tokens:
        if w not in stop_words:
            filtered_text.append(w)
            frequent_words = nltk.FreqDist(filtered_text)
            return frequent_words.most_common(5)


# Die Funktion verbindet die beiden voranggegangenen Funktionen und zeigt die 5 häufigsten Wörter für jeden einzenen Text auf,
# ohne beispielsweise Satzzeichen zu berücksichtigen
# with open("Quellen.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#     skip_header = True
#     i = 0
#     for row in csv_reader:
#         if skip_header:
#             skip_header = False
#             continue
#         if row[0] == "ECOSIO":
#             result = tokenize_text(clean_text(row[3]))
#             print('Ecosio, ' + str(row[2]) + ': ' + str(result))
#         if row[0] == "GEFEG":
#             result= tokenize_text(clean_text(row[3]))
#             print('GEFEG, ' + str(row[2]) + ': ' + str(result))
#         i += 1


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

# Sentiment analysis
with open("Quellen.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    skip_header = True
    i = 0
    for row in csv_reader:
        if skip_header:
            skip_header = False
            continue
        if row[0] == "ECOSIO":
            sia = SentimentIntensityAnalyzer()
            result = sia.polarity_scores(row[3])
            print('Ecosio, ' + str(row[2]) + ': ' + str(result))
        if row[0] == "GEFEG":
            sia = SentimentIntensityAnalyzer()
            result = sia.polarity_scores(row[3])
            print('GEFEG, ' + str(row[2]) + ': ' + str(result))
        i += 1



# Diese Funktion berechnet den flesh Reading ease Score für jeden einzelnen Artikel
# with open("Quellen.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#     skip_header = True
#     i = 0;
#     for row in csv_reader:
#         if skip_header:
#             skip_header = False
#             continue
#         if row[0] == "ECOSIO":
#             print('Ecosio Flesh Reading Score: ' + str(row[2]) + ': ' + str(textstat.flesch_reading_ease(row[3])))
#         if row[0] == "GEFEG":
#             print('GEFEG Flesh Reading Score: ' + str(row[2]) + ': ' + str(textstat.flesch_reading_ease(row[3])))
#         i += 1






# with open("Quellen.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#     skip_header = True
#     i = 0
#     for row in csv_reader:
#         if skip_header:
#             skip_header = False
#             continue
#         if row[0] == "ECOSIO":
#             #(pprint(nltk.word_tokenize(row[3]), width=79, compact=True))
#             Ecosio_words: list= nltk.word_tokenize(row[3])
#             frequent_Ecosio_words = nltk.FreqDist(Ecosio_words)
#             lower_frequent_Ecosio_words = nltk.FreqDist([w.lower() for w in frequent_Ecosio_words])
#             print(lower_frequent_Ecosio_words.most_common(10))
#             words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
#             stopwords = nltk.corpus.stopwords.words("english")
#             words = [w for w in words if w.lower() not in stopwords]
#         if row[0] == "GEFEG":
#             # pprint(nltk.word_tokenize(row[3]), width=79, compact=True)
#             GEFEG_words: list = nltk.word_tokenize(row[3])
#             frequent_GEFEG_words = nltk.FreqDist(GEFEG_words)
#             lower_frequent_GEFEG_words = nltk.FreqDist([w.lower() for w in frequent_GEFEG_words])
#             lower_frequent_GEFEG_words.most_common(10)
#             words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
#             stopwords = nltk.corpus.stopwords.words("english")
#             words = [w for w in words if w.lower() not in stopwords]
#         i += 1


words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
stopwords = nltk.corpus.stopwords.words("english")
#Wörter ohne Stoppwörter (aber alle in lower case)
words = [w for w in words if w.lower() not in stopwords]

# use str.isalpha to filter out punctuation
#pprint((nltk.word_tokenize(GEFEG_cleaned_text), width=79, compact=True)

#sentiment_pipeline = pipeline("sentiment-analysis")
#data = ["I love you", "I hate you"]
#sentiment_pipeline(data)