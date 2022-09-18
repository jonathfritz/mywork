import csv;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


with open('Quellen.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for columns in csv_reader:
        if columns[0] == 'GEFEG':
            print(columns[3])
