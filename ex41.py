#!/usr/bin/python

from sys import exit
from random import randint

class Game(object):

  def __init__(self, start):
    self.quips = ["you died, you suck at this.",
             "blah you died",
             "loser!",
             "a puppy would be better"]
    self.start = start
  
  def play(self):
    next = self.start

    while True:
      print 'n--------'
      room = getattr(self, next)
      next = room()

  def death(self):
    print self.quips[randint(0, len(self.quips)-1)]
    exit(1)

  def central_corridor(self):
    print 'the gothons of planet percal#25 have invaded your ship and destroyed'
    print 'your entire crew. you are the last surviving member and the last'
    print 'mission is to get to the neutron destruct bomb from the weapons armory'
    print 'put it in the bridge, blow the ship up after getting into an '
    print 'escape pod'
    print '\n'
    print 'your running down the central corridor to the weapons armory when'
    print 'a gothon jumps out, red scaly skin, dark grimy teeth, and an evil clown costume'
    print 'flowing around his hate filled body. hes blocking the door to the'
    print 'armory and about to pull a weapon to blast you'
  
    action = raw_input('> ')
  
    if action == 'shoot!':
      print 'quick on the draw you yank out your blaster and fire it at the gothon'
      print 'his clown costume is flowing and moving around his body, which throws'
      print 'off your aim. your laser hits his costume but misses him entirely. this'
      print 'completely ruins his brand new costume his mother bought him which'
      print 'makes him fly into an insane rage and blast you repeatedly in the face until'
      print 'you are dead. then he eats you'
      return 'death'
  
    elif action == 'tell a joke':
      print 'lucky for you that they taught gothom humour in the academy'
      print 'you tell the one gothon joke that you know'
      print 'zzzzzzzzzzzzzzzzzzzzzzzzzz'
      print 'the gothon stops, tries not to laugh, then bursts out laughing and cant move'
      print 'while hes laughing you run up and shoot him square in the head'
      print 'putting him down, then jump through the weapon armory door'
      return 'laser_weapon_armory'
  
    else:
      print 'does not compute'
      return 'central_corridor'
  
  def laser_weapon_armory(self):
    print 'you do a dive roll into the weapon armory, crouch and scan the room'
    print 'for more gothons might be hiding. its dead quiet, too quiet'
    print 'you stand up and run to the far side of the room and find the'
    print 'neutron bomb in its container. theres a keypad lock on the box'
    print 'and you need the code to get the bomb out. if you get the code'
    print 'wrong 10 times then the lock closes forever and you cant'
    print 'get the bomb. the code is 3 digits'
    code = '%d%d%d' % (randint(1,9), randint(1,9), randint(1,9))
    guess = raw_input('[keypad]> ')
    guesses = 0
  
    while guess != code and guesses < 10:
      print 'bbbbbzzzzzdddd!'
      guesses += 1
      guess = raw_input('[keypad]> ')
  
    if guess == code:
      print 'the container clicks open and the seal breaks, letting gas out'
      print 'you grab the neutron bomb and run as fast as you can to the'
      print 'bridge where you must palce it in the right spot'
      return 'the_bridge'
    else:
      print 'the lock buzzes one last time and then you hear a sickening'
      print 'melting sound as the mechanism is fused together'
      print 'you decide to sit there and finally the gothons blow up the'
      print 'ship from their ship and you die'
      return 'death'
  
  def the_bridge(self):
    print 'you burst onto the bridge with the neutron destruct bomb'
    print 'under your arm and surprise 5 gothons who are trying to'
    print 'take control of the ship. each of them has an even uglier'
    print 'clown costume than the last. they havent pulled their'
    print 'weapons out yet as they see the active bomb under your'
    print 'arm and dont want to set it off'
  
    action = raw_input('> ')
  
    if action == 'throw the bomb':
      print 'in a panic you throw the bomb at the group of gothons'
      print 'and make a leap for the door. right as you drop it a'
  
      print 'gothon shoots you right in the back killing you'
      print 'as you die you see another gothon frantically try to disarm'
      print 'the bomb. you die knowing they will probably blow up when'
      print 'it goes off'
      return 'death'
  
    elif action == 'slowly place the bomb':
      print 'you point your blaster at the bomb under your arm'
      print 'and the gothons put their hands up and start to sweat'
      print 'you inch backward to the door, open it, and then carefully'
      print 'place the bomb on the floor, pointing your blaster at it'
      print 'you then jump back through the door, punch the close button'
      print 'and blast the lock so the gothons cant get out'
      print 'now that the bomb is placed you run to the escape pod to'
      print 'get off this tin can'
      return 'escape_pod'
  
    else:
      print 'does not compute'
      return 'the_bridge'
  
  def escape_pod(self):
    print 'you rush through the ship desperately trying to make it to'
    print 'the escape pod before the whole ship explodes. it seems like'
    print 'hardly any gothons are on the ship, so your run is clear of'
    print 'interference. you get to the chamber with the escape pods and'
    print 'now need to pick one to take. some of them could be damaged'
    print 'but you dont have time to look. theres 5 pods, which one?'
    print 'do you take'
  
    good_pod = randint(1,5)
    guess = raw_input('[pod #]> ')
  
    if int(guess) != good_pod:
      print 'you jump pod %s and hit the escape button' % guess
      print 'the pod escapes out into the void of space, then'
      print 'implodes as the hull ruptures, crushing your body'
      print 'into jam jelly'
      return 'death'
    else:
      print 'you jump into pod %s and hit the eject button' % guess
      print 'the pod easily slides out into space heading to'
      print 'the planet below. as it flies to the planet, you look'
      print 'back and see your ship implode then explode like a'
      print 'bright star, taking out the gothon ship at the same'
      print 'time. you won'
  
  
a_game = Game('central_corridor')

if __name__ == "__main__":
 a_game.play()
  
