#!/usr/bin/python

people = 30
cars = 40
buses = 15

if cars > people:
  print "take the cars"

elif cars < people:
  print "don't take the cars"

else:
  print "we can't decide"

if buses > cars:
  print "too many buses"

elif buses < cars:
  print "we could take the buses"

else:
  print "we still can't decide"

if people > buses:
  print "just takes the buses"

else:
  print "fuck it, stay home"
