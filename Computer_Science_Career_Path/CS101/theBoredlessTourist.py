destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
attractions = [[] for destination in destinations]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
    except ValueError:
        print("Destination does not exist in list")
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

def get_attractions_for_traveler(traveler):
    traveler_name = traveler[0]
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    attractions_string = ""
    for attraction in traveler_attractions:   
        if attractions_string == "":
            attractions_string += attraction
        else:
            attractions_string += ", " + attraction
    interests_string = "Hi, " + traveler_name + ". We think you will like these places around " + traveler_destination + ": " + attractions_string + "."
    return interests_string

smill_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
#print(smill_france)
