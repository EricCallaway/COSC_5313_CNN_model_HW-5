import os
from numpy import isin
import pandas as pd

test_dir = os.listdir('/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/final_dataset/test/')
test_bubble = os.listdir('/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/final_dataset/test/bubble_defects')
test_glue = os.listdir('/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/final_dataset/test/glue_defects')
test_normal = os.listdir('/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/final_dataset/test/normal')
test_obj = os.listdir('/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/final_dataset/test/object_defects')


test_csv = '/Users/ericcallaway/Google Drive/School Work/Summer 2022/Artificial Intelligence/Home Work/HW#5/test_data.csv'

df = pd.read_csv(test_csv)

# print(df.head())


bubble_list = []
glue_list = []
normal_list = []
obj_list = []

# print(df[' file_name'])
# for f in test_bubble:
#     print(int(f.strip('.bmp')))
for file in test_bubble:
    temp = int(file.strip('.bmp'))
    bubble_list.append(temp)    

for file in test_glue:
    temp = int(file.strip('.bmp'))
    glue_list.append(temp)

for file in test_normal:
    temp = int(file.strip('.bmp'))
    normal_list.append(temp)

for file in test_obj:
    temp = int(file.strip('.bmp'))
    obj_list.append(temp)

final_list = bubble_list + glue_list + normal_list + obj_list


print(len(bubble_list))
print(len(glue_list))
print(len(normal_list))
print(len(obj_list))
print(len(final_list))

df_filtered = df[df[' file_name'].isin(final_list)]
df_filtered.to_csv('test_data_final.csv', index=False)

print(df_filtered)
