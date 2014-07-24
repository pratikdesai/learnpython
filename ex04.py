# assigning cars a value of 100
cars = 100
# Space in each car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Calculate cars not driven
cars_not_driven = cars - drivers
# Calculate cars being driven
cars_driven = drivers
# What's the carpool capacity?
carpool_capacity = cars_driven * space_in_a_car
# Average passengers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

