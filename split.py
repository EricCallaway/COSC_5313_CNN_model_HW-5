import pandas as pd
import numpy as np
df = pd.read_csv('test.csv')


class_labels = df[' class_label'].values

label_0_df = df.loc[(df[' class_label'] == 0)]
label_1_df = df.loc[(df[' class_label'] == 1)]
label_2_df = df.loc[(df[' class_label'] == 2)]
label_3_df = df.loc[(df[' class_label'] == 3)]




with open('file_data.csv', 'r') as f:
    new_line = f.readlines()



with open('class_0.csv', 'w') as f:
    for line in new_line:
        if line[-2] == '0':
            f.write(line)

with open('class_1.csv', 'w') as f:
    for line in new_line:
        if line[-2] == '1':
            f.write(line)

with open('class_2.csv', 'w') as f:
    for line in new_line:
        if line[-2] == '2':
            f.write(line)

with open('class_3.csv', 'w') as f:
    for line in new_line:
        if line[-2] == '3':
            f.write(line)