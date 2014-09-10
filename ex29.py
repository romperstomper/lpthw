#!/usr/bin/python

people = 20
cats = 30
dogs = 15



if people < cats:
  print "too many cats!"

if people > cats:
  print "not enough cats"

if people < dogs:
  print "not enough dogs"

if people > dogs:
  print "defo too many ppl"

dogs += 5

if people >= dogs:
  print "ppl are greater or equal to dogs"

if people <= dogs:
  print "ppl are less than or equal to dogs"

if people == dogs:
  print "people are dogs!"
