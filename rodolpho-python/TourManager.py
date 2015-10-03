destination_cities = []

def add_city(city):
    global destination_cities
    destination_cities.append(city)

def get_city(index):
    global destination_cities
    return destination_cities[index]

def cities_number():
    global destination_cities
    return len(destination_cities)
