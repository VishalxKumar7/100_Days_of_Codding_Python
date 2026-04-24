### NESTED DICTIONARY

# Normal List
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# # Print Lille
# print(travel_log["France"][1])

# # Nested List
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][0])


# Dictionary inside a Dictionary (Nested Dictionary)
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijson"]
    },
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"]["cities_visited"][2])
print(travel_log["Germany"][1])