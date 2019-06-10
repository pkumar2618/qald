import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

pickle_handle = open("pickle_df_processed_bup", "rb")
category_df = pickle.load(pickle_handle)
pickle_handle.close()
# print(category_df)
category_df.to_csv("qald_en_pos_ner_list_count.csv", columns=["qald_id", "sentence_en", "pos-complex(H/M/E)",
                                                          "ner-complex(H/M/E)", "list_type(Y/N)", "count_type(Y/N)"],
                   index=False)


# y-axis in bold
rc('font', weight='bold')


# Values of each group
hard = [0, 0]
medium = [0, 0]
easy = [0, 0]

category_df = category_df.set_index("qald_id", drop=False)
for id_label in category_df.index:
    pos_complex = category_df.at[id_label, "pos-complex(H/M/E)"]
    if pos_complex == "hard":
        hard[0] += 1
    elif pos_complex == "medium":
        medium[0] += 1
    elif pos_complex == "easy":
        easy[0] += 1

    ner_complex = category_df.at[id_label, "ner-complex(H/M/E)"]
    if ner_complex == "hard":
        hard[1] += 1
    elif ner_complex == "medium":
        medium[1] += 1
    elif ner_complex == "easy":
        easy[1] += 1



# Heights of bars1 + bars2
bars = np.add(easy, medium).tolist()

# The position of the bars on the x-axis
r = [0, 1]

# Names of group and bar width
names = ['pos_complex', 'ner_complex']
barWidth = 1

# Create brown bars
plt.bar(r, easy, color='#7f6d5f', edgecolor='white', width=barWidth)
# Create green bars (middle), on top of the firs ones
plt.bar(r, medium, bottom=easy, color='#557f2d', edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, hard, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)

# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")

# Show graphic
plt.show()