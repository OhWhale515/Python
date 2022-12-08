# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# # average = sum(temp_list) / len(temp_list)
# # print(average)


# # Data Columns!
# # print(data["condition"])
# print(data.condition)

# Data Rows!
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Dataframe from scratch!
data_dict = {
    "students": ["Jess", "Qoun", "Shae"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)