#### PANDAS


# with open('weather_data.csv') as f:
#     data = f.readlines()      ## It won't work
#     print(data)


# import csv   ## Using files

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for raw in data:
#         if raw[1] != "temp":
#             temperature.append(int(raw[1]))
#     print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])
    