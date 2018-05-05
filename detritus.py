# This program plays several moves of Zork for the user and then
# turns control of the game over to the user.

import pexpect 
import sys

# Run Zork "in the terminal."
# NOTE: use spawn(), not spawnu(), unless you want to mess with 
# Unicode nonsense.
zork = pexpect.spawn('frotz ZORKI')
#zork.maxread = 1024
#zork.searchwindowsize = 1024

# Write child output to the screen
zork.logfile = sys.stdout

# Write child output to a file
# fout = file('mylog.txt','w')
# zork.logfile = fout

# List of commands to give to Zork
# commands = ['n', 'n', 'climb tree', 'take egg', 'down', 's', 'e', 'open window', 'in', 'west', 'open case', 'put egg in case', 'take lamp', 'move rug', 'open trap door', 'down', 'light lamp', 's', 'turn off lamp', 'e', 'take painting', 'n', 'up', 'w', 'put painting in case', 'e', 'up', 'light lamp', 'take all', 'down', 'turn off lamp', 'take all', 'w', 'take sword', 'open trap door', 'down', 'light lamp', 'n']

# List of commands to give to Zork
# Egg, painting, coins first, to troll room to kill troll
commands = ['n', 'n', 'climb tree', 'take egg', 'down', 's', 'e', 'open window', 'in', 'west', 'open case', 'put egg in case', 'take lamp', 'move rug', 'open trap door', 'down', 'light lamp', 's', 'turn off lamp', 'e', 'take painting', 'n', 'up', 'w', 'put painting in case', 'e', 'up', 'light lamp', 'take all', 'down', 'turn off lamp', 'take all', 'w', 'drop all', 'take lamp', 'take sword', 'open trap door', 'down', 'light lamp', 'n']

for command in commands:
    # print command
    zork.expect(">")
    zork.sendline(command)

# Deal with the troll
# troll_dead = False
# zork.expect(">")
# while not troll_dead:
 #    zork.sendline('kill troll with sword')
    # The first pattern matches the case in which you kill the troll, 
    # and must catch the word "troll" before the last case.
    # The second matches the case in which the troll kills you.
    # The third matches everything else. The only thing we know for sure 
    # involving the troll is that all the verbage contains the word "troll".
  #  i = zork.expect(["troll.*breathes", "troll.*sunlight", "troll", pexpect.EOF])
#    out = open('out', 'a')
#    out.write('%d\n'%i)
#    out.close()
  #   if i == 0:
   #      troll_dead = True
    #     zork.sendline("e")
    # elif i == 1:
     #    zork.sendline("q")   
      #   exit(0)
   #  zork.expect(">")
##    raw_input('any key')


# Turn control over to user to kill troll
zork.expect(">")
zork.logfile = None
zork.interact()

# After interacting, user will enter escape character (ctrl-]) to stop the interacting method

# Write child output to the screen again
zork.logfile = sys.stdout

# Post-troll-killing commands to give Zork 

# to dam lobby, to torch room
# commands = ['e', 'n', 'ne', 'e', 'n', 'take matches', 's', 's', 'down', 'w', 'se', 'e', 'tie rope to railing', 'down', 'take torch'] 

# to dam lobby, to ladder top
# commands = ['e', 'n', 'ne', 'e', 'n', 'take matches', 's', 's', 'down', 'w', 'se', 'e', 'tie rope to railing', 'down', 's', 's', 'd', 'w', 'n', 'touch mirror', 'n', 'w', 'n', 'w', 'open sack', 'take garlic', 'n', 'e', 'n', 'down', 'e', 'ne', 'se', 'sw', 'down'] 

# getting supplies, going back to maze
# commands = ['drop all', 'take lantern', 'e', 'n', 'ne', 'e', 'n', 'take all', 'n', 'take all', 's', 's', 'w', 'sw', 'sw', 'w', 'drop all', 'take knife', 'take sack', 'take bottle', 'take matches', 'take wrench', 'take lantern', 'w', 'drop knife', 'w', 'open sack', 'drop garlic', 'e', 'drop wrench', 's', 'w', 'drop bottle', 'w', 'drop matches', 'down', 'n', 'e', 'take all', 'w', 'w', 'w', 'up', 'e', 'drop guidebook', 'w', 'take key', 'sw', 'drop tube', 'e', 'drop rope', 'e', 'drop sack', 'se', 'drop key', 'n', 'ne', 'w', 'down', 'take rusty knife', 'take lantern', 'sw', 'e', 'up', 'drop screwdriver', 'w', 's', 'w', 'up', 'drop burned-out lantern', 'e', 'drop sword', 'e', 's', 'drop rusty knife'] 

# maze, skeleton key, bag of coins, house
commands = ['w', 'w', 'w', 'up', 'take key', 'take bag', 'sw', 'up', 'down', 'ne', 'open grating with key', 'open grating', 'up', 'turn off lamp', 's', 's', 'e', 'in', 'w', 'put bag in case', 'put sword in case'] 

for command in commands:
    # print command
    zork.sendline(command)
    zork.expect(">")
    
# living room up to dam maintenance room, fix leak, open sluice gates
# get plastic, get pump, close sluice gates, boat on reservoir, float
# to land east on sandy beach, go into cave, dig and get scarab
commands = ['take knife', 'take rope', 'open trap door', 'down', 'light lamp', 
            'n', 'e', 'e', 'n', 'ne', 'nw', 'e', 'n', 'take matches',
            'n', 'push all buttons', 
            'turn off lamp', 'take tube', 'open tube', 
            'fix leak with viscous material', 'take wrench', 's', 's', 
            'turn bolt', 'wrench', 'drop wrench', 'w', 'light lamp', 'look', 
            'look', 'l', 'l', 'n', 'n', 'take pump', 's', 's', 'drop knife', # knife is in res. south
            'e', 'd', 
            'turn off lamp', 'inflate plastic with pump', 
            'get in boat', 'launch']

for command in commands:
    # print command
     zork.sendline(command)
     zork.expect(">")
     
# Turn control over to user to navigate river to sandy branch
zork.expect(">")
zork.logfile = None
zork.interact()


# After interacting, user will enter escape character (ctrl-]) to stop the interacting method

# Write child output to the screen again
zork.logfile = sys.stdout

# more commands after escape signal: sandy beach, dig hole, get scarab, 
# get to wcb
commands = ['east', 'get out of boat', 'take shovel', 'ne', 
            'dig sand with shovel,' 'dig sand with shovel',
            'dig sand with shovel', 'dig sand with shovel', 'take scarab',
            'sw', 'get in boat', 'launch', 'w', 'get out of boat', 'n']

for command in commands:
    # print command
     zork.sendline(command)
     zork.expect(">")
     
# go down to Hades
# commands = ['w', 'w', 'echo', 'drop scarab', 'w', 'se', 'e', 
#            'tie rope to railing', 'down', 'take torch', 's', 
#            'take bell', 's', 'take candles', 'take book', 'd', 'd'] 


# for command in commands:
    # print command
#      zork.sendline(command)
#      zork.expect(">")


# troll room to dam lobby, to Hades
# commands = ['e', 'n', 'ne', 'e', 'n', 'take matches', 's', 's', 'down', 'w', 'se', 'e', 'tie rope to railing', 'down', 'take torch', 's', 'take bell', 's', 'take candles', 'take book', 'd', 'd'] 

# for command in commands:
    # print command
#    zork.sendline(command)
#    zork.expect(">")

# Turn control back over to user

zork.logfile = None
zork.interact()

# zork.expect("I don't know the word \"resume\".")
# zork.sendline("e")


