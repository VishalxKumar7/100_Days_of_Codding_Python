import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))


# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])

# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])


data_dict = {
    "students":["Amy", "James", "Angela"],
    "scores": [72, 56, 65]
}

data_ = pd.DataFrame(data_dict)

print(data_)

data_.to_csv("new_data.csv")  