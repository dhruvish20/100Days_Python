# # import os
# # import csv

# # my_local_file = os.path.join(os.path.dirname(__file__), 'weather_data.csv')

# # with open(my_local_file,  "r") as f:
# #     content = csv.reader(f)
# #     temperature = []
# #     for row in content:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# # print(temperature)

# import pandas as pd
# import os

# my_local_file = os.path.join(os.path.dirname(__file__), 'weather_data.csv')

# data = pd.read_csv(my_local_file)
# # print(type(data))
# # print(data["temp"])

# # temp = data["temp"].to_list()
# # print(temp)

# # print(f"avg temperature = {sum(temp) / len(temp)}")
# # print(data["temp"].mean())

# print(data[data.temp == data.temp.max()]["temp"])

import os
import pandas as pd 

my_file = os.path.join(os.path.dirname(__file__) , "Squirrel_Data.csv")

data = pd.read_csv(my_file)

total_gray = len(data[data["Primary Fur Color"]=="Gray"])
total_cinnamon = len(data[data["Primary Fur Color"]=="Cinnamon"])
total_black = len(data[data["Primary Fur Color"]=="Black"])

print(total_gray)
print(total_cinnamon)
print(total_black)

data_dict = {
    "Fur color" : ["gray","cinnamon","black"],
    "count" : [total_gray,total_cinnamon,total_black]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_Count.csv")