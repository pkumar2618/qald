import json
import pandas as pd
data = json.load(open("qald-9-train-multilingual.json"))
# # data = pd.read_json("./qald-9-train-multilingual.json")
# questions = pd.DataFrame(data["questions"])
# print(questions[:1])
# a =questions[:1]
# for c in a:
#     print(c)
# with open("qald-9-train-multilingual.json", "r") as read_file:
#     data = json.load(read_file)