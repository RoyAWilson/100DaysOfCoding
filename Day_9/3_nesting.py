travel_log = {
    'France': ['Paris', 'Lille', 'Marseille', 'Lyon'],
    'Germay': ['Berlin', 'Munich', 'Hamburg'],

}

# Challenge extract 'Lille' from the dictionary:

print(travel_log['France'][1])

#  Challenge 2 print D from following list:

nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])

# nested dictionaries

travel_log2 = {
    'France': {
        'times_visited': 8,
        'cities': ['Paris', 'Lille', 'Marseille', 'Lyon']
    },
    'Germay': {
        'times visited': 5,
        'cities': ['Berlin', 'Munich', 'Hamburg']
    },
}

# Access the items:

print(travel_log2['France']['cities'][2])
