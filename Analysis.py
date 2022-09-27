import csv
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import textstat




def clean_text(text):
    # Diese Funktion reduziert die Komplexität der Textpassagen.
    # Sie entfernt Satzzeichen, setzt bei jedem Wort die Kleinschreibung durch und entfernt Worte, in denen Nummern beinhaltet sind
    text = text.lower()
    text = re.sub('\[.*?]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def tokenize_text(text):
    # Diese Funktion zerteilt den Text in einzelne Buchstaben und zählt die Häufigkeit der einzenen Wörter.
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

# # Count Words
# with open("Quellen.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#     skip_header = True
#     i = 0
#     for row in csv_reader:
#         if skip_header:
#             skip_header = False
#             continue
#         if row[0] == "ECOSIO":
#             word_list = row[3].split()
#             result = number_of_words = len(word_list)
#             print('Ecosio, ' + str(row[2]) + ': ' + str(result))
#         if row[0] == "GEFEG":
#             word_list = row[3].split()
#             result = number_of_words = len(word_list)
#             print('GEFEG, ' + str(row[2]) + ': ' + str(result))
#         i += 1


# Diese Funktion berechnet die Tonalität (Sentiment) der jeweiligen
# with open("Quellen.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=";")
#     skip_header = True
#     i = 0
#     for row in csv_reader:
#         if skip_header:
#             skip_header = False
#             continue
#         if row[0] == "ECOSIO":
#             sia = SentimentIntensityAnalyzer()
#             result = sia.polarity_scores(row[3])
#             print('Ecosio, ' + str(row[2]) + ': ' + str(result))
#         if row[0] == "GEFEG":
#             sia = SentimentIntensityAnalyzer()
#             result = sia.polarity_scores(row[3])
#             print('GEFEG, ' + str(row[2]) + ': ' + str(result))
#         i += 1


# Diese Funktion berechnet den flesh Reading ease Score für jeden einzelnen Artikel
with open("Quellen.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    skip_header = True
    i = 0;
    for row in csv_reader:
        if skip_header:
            skip_header = False
            continue
        if row[0] == "ECOSIO":
            print('Ecosio Flesh Reading Score: ' + str(row[2]) + ': ' + str(textstat.flesch_reading_ease(row[3])))
        if row[0] == "GEFEG":
            print('GEFEG Flesh Reading Score: ' + str(row[2]) + ': ' + str(textstat.flesch_reading_ease(row[3])))
        i += 1




