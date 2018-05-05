# This program plays several moves of Zork for the user and then
# turns control of the game over to the user.

import pexpect 
import sys

# Run Zork "in the terminal."
# NOTE: use spawn(), not spawnu(), unless you want to mess with Unicode

zork = pexpect.spawn('frotz ZORKI')
#zork.delaybeforesend = 1 
#zork.maxread = 1024
#zork.searchwindowsize = 1024

# Write child output to the screen
zork.logfile = sys.stdout

# Write child output to a file
# fout = file('mylog.txt','w')
# zork.logfile = fout

# Pre-troll list of commands to give to Zork
# start at west of house
# go treasure-free to troll with sword
commands = ['s', 'e', 'open window', 'in', 'west', 'take lamp', 
            'e', 'u', 'light lamp', 'take knife', 'take rope', 
            'turn off lamp', 'd', 'w', 
            'drop rope', 'take sword', 'move rug', 
            'open trap door', 'down', 'light lamp', 'n']

for command in commands:
    # print command
    zork.expect(">")
    zork.sendline(command)


# Deal with the troll
# Some responses seem to be 2+ lines, and it looks like this program
# is sending a "kill troll" response for every line. Need to rethink this...
troll_dead = False
while not troll_dead:
   zork.sendline('kill troll with sword')
  # The first pattern matches the case in which you kill the troll, 
  # and must catch the word "troll" before the last case.
  # The second matches the case in which the troll kills you.
  # The third matches everything else. The only thing we know for sure 
  # involving the troll is that all the verbiage contains the word "troll".
   zork.delaybeforesend = 2 
   i = zork.expect(["troll .+\n?.+breathes.*\n?.*(glowing)?", "stroke.*\n.*\n?.*\n?.*\n?.*dead\.\n+\*.*\n+Now.*\n+Forest\n.*sunlight", ".+\n?.*", pexpect.EOF])
   out = open('out', 'a')
   out.write('%d\n'%i)
   out.close()
   if i == 0:   # troll killed
     troll_dead = True
     zork.sendline("e")
   elif i == 1:   # troll kills me
     zork.sendline("q")   
     exit(0)
     zork.expect(">")
     raw_input('any key')
     
zork.expect(">")
# troll room to maze, get skeleton key, get bag of coins, 
# open strange passageway, go back to house, put coins in case
# troll to skeleton
commands = ['w', 'w', 'w', 'up']
# skeleton to cyclops
commands = ['sw', 'e', 's', 'se']
#             'open sack', 'give lunch to cyclops', 'give water to cyclops']
# 'take key', 'take bag']#, 'sw', 'up', 'down', 
#            'ne', 'open grating with key', 'open grating', 'up', 
#            'turn off lamp', 's', 's', 'e', 'in', 'w', 'put bag in case', 
#            'put sword in case'] 



# Turn control over to user 
# zork.expect(">")
# zork.logfile = None
# zork.interact()

# Turn control over to user to kill troll; logfile = None
# zork.expect(">")
# zork.logfile = None
# zork.interact()

# After interacting, user will enter escape character (ctrl-]) to stop the interacting method

# Write child output to the screen again
# zork.logfile = sys.stdout

# Post-troll list of commands to give to Zork

# maze, skeleton key, bag of coins, open grating, cyclops, house
# troll room to skeleton: w, w, w, u
# skeleton to grating: sw, s, d, ne
# grating to cyclops: sw, d, e, n, e, s, se
# commands = ['w', 'w', 'w', 'up', 'take rusty knife', 'sw', 'e', 's', 'se',
#             'open sack', 'give lunch to cyclops', 'give water to cyclops']
# 'take key', 'take bag']#, 'sw', 'up', 'down', 
#            'ne', 'open grating with key', 'open grating', 'up', 
#            'turn off lamp', 's', 's', 'e', 'in', 'w', 'put bag in case', 
#            'put sword in case'] 



# maze, skeleton key, bag of coins, house
# troll room to skeleton: w, w, w, u
# skeleton to cyclops: sw, e, s, se
# commands = ['w', 'w', 'w', 'up', 'take rusty knife', 'sw', 'e', 's', 'se',
#             'open sack', 'give lunch to cyclops', 'give water to cyclops']
# 'take key', 'take bag']#, 'sw', 'up', 'down', 
#            'ne', 'open grating with key', 'open grating', 'up', 
#            'turn off lamp', 's', 's', 'e', 'in', 'w', 'put bag in case', 
#            'put sword in case'] 

# for command in commands:
    # print command
#     zork.sendline(command)
#     zork.expect(">")
     
# Hades: troll room to dam lobby (to get matches), then Hades
# commands = ['e', 'n', 'ne', 'e', 'n', 'take matches', 's', 's', 'down', 'w', 
#             'se', 'e', 'tie rope to railing', 'down', 'take torch', 's', 
#             'take bell', 'e', 'open coffin', 'take sceptre', 'w', 's', 
#             'take candles', 'take book', 'd', 'd'] 
            # to enter Land of the Dead (candles may or may not be blown
            # out in the cave): 'drop candles', 'light match', 'light 
            # candles with match', 'ring bell', 'take candles', 'read book', 
            # 'enter gate', 'take skull'

# Boat: troll room to dam maintenance room, fix leak, open sluice gates,
# get plastic and take it to the pump (reservoir)
# commands = ['e', 'n', 'ne', 'nw', 'e', 'n', 'n', 'push all buttons', 
#             'turn off lamp', 'take tube', 'open tube', 
#             'fix leak with viscous material', 'take wrench', 's', 's', 
#             'turn bolt with wrench', 'drop wrench', 'down', 'take plastic',
#             'up', 'w', 'light lamp', 'n', 'n', 'take pump'] 

# Coal mine 1: troll room, get screwdriver and torch, to shaft room
#commands = ['e', 'n', 'ne', 'e', 'n', 'n', 'take screwdriver',
#            's', 's', 'w', 'se', 'down', 'west', 'se', 'e', 
#            'tie rope to railing', 'down', 'take torch', 'turn off lamp',
#            's', 's', 'd', 'w', 'n', 'touch mirror', 'n', 'w', 'n', 'w', 
#            'open sack', 'take garlic', 'n', 'e', 'put torch in basket',
#            'light lamp']

#for command in commands:
   # print command
#   zork.sendline(command)
#   zork.expect(">")

# Coal mine 2 (machine): in shaft room, put torch in basket and lower
# basket, then go to drafty room and remove torch 
# Shaft to timber:  'n', 'down', 'e', 'ne', 'se', 'sw', 'down', 'down', 'w'
# Timber to shaft: 'e', 'u', 'u', 'n', 'e', 's', 'n', 'u', 's'
# commands = ['put torch in basket', 'lower basket', 'n', 'down', 'e', 
#             'ne', 'se', 'sw', 'down', 'down', 'w', 'drop all', 'w',
#             'take torch', 'drop torch']

# New Coal mine 2 -- Put multiple things in basket
# Coal mine 2 (machine): get coal, come back to shaft room, put coal
# and screwdriver in basket and lower basket, go to drafty room,
# put coal in machine and remove diamond, go back to shaft room,
# get bracelet in gas room, get diamond, put bracelet and diamond in sack
#commands = ['n', 'down', 'e', 'ne', 'se', 'sw', 'down', 'down', 's',
#            'take coal', 'n', 'u', 'u', 'n', 'e', 's', 'n', 'u', 's',
#            'turn off lamp', 'put coal in basket',
#            'put screwdriver in basket', 'lower basket', 'turn on lamp',
#            'n', 'down', 'e', 'ne', 'se', 'sw', 'down', 'down', 'w', 
#            'drop all', 'w', 'take coal', 'take screwdriver',
#            'take torch', 's', 'open machine', 'put coal in machine', 
#            'close machine', 'turn switch with screwdriver', 'open machine',
#            'take diamond', 'n', 'put all in basket', 'e', 
#            'take all', 'e', 'u', 'u', 'n', 'e', 's', 'n', 'take bracelet',
#            'u', 's', 'raise basket', 'turn off lamp', 'drop timber', 
#            'take torch', 'take diamond', 'open sack', 'put diamond in sack',
#            'put bracelet in sack']  
 
#for command in commands:
   # print command
#    zork.sendline(command)
#    zork.expect(">")

# Coal mine 3 (machine): drafty room to timber room, take screwdriver,
# go to basket, put screwdriver in basket, lower it, go back to drafty room, 
# remove screwdriver 
# Shaft to timber:  'n', 'down', 'e', 'ne', 'se', 'sw', 'down', 'down', 'w'
# Timber to shaft: 'e', 'u', 'u', 'n', 'e', 's', 'n', 'u', 's'
# commands = ['e', 'take lamp', 'take screwdriver', 'e', 'u', 'u', 'n', 'e', 
#            's', 'n', 'u', 's', 'raise basket', 'put screwdriver in basket',
#            'lower basket', 'n', 'down', 'e', 'ne', 'se', 'sw', 'down', 
#            'down', 'w', 'drop all', 'w', 'take screwdriver', 'drop screwdriver']


#for command in commands:
   # print command
#   zork.sendline(command)
#   zork.expect(">")

# Coal mine 4 (machine): get coal to basket, lower it, remove it 
# Shaft to timber:  'n', 'down', 'e', 'ne', 'se', 'sw', 'down', 'down', 'w'
# Timber to shaft: 'e', 'u', 'u', 'n', 'e', 's', 'n', 'u', 's'
#commands = ['e', 'take lamp', 'e', 's', 'take coal', 'n', 'u', 'u', 'n', 'e', 
#            's', 'n', 'u', 's', 'raise basket', 'put coal in basket',
#            'lower basket', 'n', 'down', 'e', 'ne', 'se', 'sw', 'down', 
#            'down', 'w', 'drop all', 'w', 'take coal', 'take screwdriver',
#            'take torch', 's', 'open machine', 'put coal in machine', 
#            'close machine', 'turn switch with screwdriver', 'open machine'
#            'take diamond']


#for command in commands:
   # print command
#   zork.sendline(command)
#   zork.expect(">")

# Turn control back over to user

# zork.logfile = None
# zork.interact()
