# calculating the amount of dollars it cost to stay in the hotel
# u pay per night so its days - 1, and every night cost 40$
def hotel_cost (days):
    return 40 * (days - 1)
# calculating the cost of fly in U.S define by city.
def fly_cost (city):
    if city == "Los Angeles":
        return 205
    elif city == "Chicago":
        return 186
    elif city == "Las Vegas":
        return 225
    else:
        return 200
# calculating the cost of a renting car 30$ per day
def car_cost (days):
    return 30 * days
# getting the cost of the total cost from all the functions together
def total_cost (days,city, spending):
    return hotel_cost(days) + fly_cost(city) + car_cost(days) + spending
# settings up the trips specs so i get the cost of all of it and print it
print (total_cost(12, "Chicago", 400))
print (total_cost(5, "Montana", 250))
