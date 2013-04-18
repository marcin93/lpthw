# -*- coding: utf-8 -*-
cars = 100 # numbers of cars
space_in_a_car = 4 # 4.0 floating point | sits per car
drivers = 30 # number of drivers
passengers = 90 # number of passengers
cars_not_driven = cars - drivers # one driver per car
cars_driven = drivers # one driver per car i = 30
carpool_capacity = cars_driven * space_in_a_car # j = 30 * 4
average_passagers_per_car = passengers / cars_driven # x = 90 / 30

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passagers_per_car, "in each car."