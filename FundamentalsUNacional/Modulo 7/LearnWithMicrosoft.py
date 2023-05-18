def rocket_parts():
    return "Payload, propellant, structure"

##output = rocket_parts()
#Es interesante la primera funcion porque me ayuda a entender mejor el return
#print(output)

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))
