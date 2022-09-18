import csv;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#with open('Quellen.csv', 'r') as csv_file:
  #  csv_reader = csv.reader(csv_file, delimiter=';')
#
  #  for columns in csv_reader:
   #     print(columns[0])

df = pd.read_csv('C:\Users\jonat\OneDrive\Dokumente\GitHub\mywork\Quellen.csv')
print(df.shape)

# gut
