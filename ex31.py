#!/usr/bin/python
print "there is a room with two doors, do you want to go through #1 or #2?"
door = raw_input("> ")

if door == "1":
  print "bear eating a cheesecake, what will you do"
  print "1: take the cake"
  print "2: scream at the bear!"

  bear = raw_input("> ")

  if bear == "1":
    print "the bear eats your face off!"
  elif bear == "2":
    print "the bear eats your lets off!"
  else:
    print "doing %s is probably better. bear runs away" % bear




elif door == "2":
  print "you stare in the the abyss"
  print "will you stay sane or not"
  insanity = raw_input("> ")

  if insanity == "1":
    print "you are insane"
  else:
    print "everyone is insane!"

else:
  print "you stumble and fall on a knife. Game Over"
