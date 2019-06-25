import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# pickle_handle = open("pickle_df_train_processed", "rb")
pickle_handle = open("pickle_df_test_processed", "rb")
category_df = pickle.load(pickle_handle)
pickle_handle.close()
# print(category_df)
# category_df.to_csv("qald_en_train_pos_ner_list_count.csv", index=False)
category_df.to_csv("qald_en_test_pos_ner_list_count.csv", index=False)


# # y-axis in bold
# rc('font', weight='bold')
#
#
# # Values of each group
# hard = [0, 0]
# medium = [0, 0]
# easy = [0, 0]
#
# category_df = category_df.set_index("qald_id", drop=False)
# for id_label in category_df.index:
#     pos_complex = category_df.at[id_label, "pos-complex(H/M/E)"]
#     if pos_complex == "hard":
#         hard[0] += 1
#     elif pos_complex == "medium":
#         medium[0] += 1
#     elif pos_complex == "easy":
#         easy[0] += 1
#
#     ner_complex = category_df.at[id_label, "ner-complex(H/M/E)"]
#     if ner_complex == "hard":
#         hard[1] += 1
#     elif ner_complex == "medium":
#         medium[1] += 1
#     elif ner_complex == "easy":
#         easy[1] += 1
#
#
#
# # Heights of bars1 + bars2
# bars = np.add(easy, medium).tolist()
#
# # The position of the bars on the x-axis
# r = [0, 1]
#
# # Names of group and bar width
# names = ['pos_complex', 'ner_complex']
# barWidth = 0.85
#
# # labels for the stacked bar
# stack_label = ["easy", "medium", "hard"]
# # Create brown bars
# plt.bar(r, easy, color='#b5ffb9', edgecolor='white', width=barWidth)
# # Create green bars (middle), on top of the firs ones
# plt.bar(r, medium, bottom=easy, color='#f9bc86', edgecolor='white', width=barWidth)
# # Create green bars (top)
# plt.bar(r, hard, bottom=bars, color='#a3acff', edgecolor='white', width=barWidth)
#
# # Custom X axis
# plt.xticks(r, names, fontweight='bold')
# plt.xlabel("Complexity Dimension", fontsize=16)
# plt.ylabel('Sentence count', fontsize=16)
# plt.title('Complexity of QALD sentences', fontsize=18)
# plt.legend(stack_label, loc=2)
# # Show graphic
# plt.show()
