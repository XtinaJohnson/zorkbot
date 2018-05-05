# This program plays several moves of Zork for the user and then
# turns control of the game over to the user.

import pexpect 
import sys

# Run Zork "in the terminal"
# "zork" is now the "child"
# NOTE: use spawn(), not spawnu(), unless you want to mess with Unicode
zork = pexpect.spawn('frotz ZORKI')

# Write child output to the screen
zork.logfile = sys.stdout


# Commands to get to the troll
commands = ['s', 'e', 'open window', 'in', 'w', 'take lamp', 'e', 'u',
            'light lamp', 'take knife', 'take rope', 'turn off lamp', 'd',
            'w', 'drop rope', 'take sword', 'move rug', 
            'open trap door', 'down', 'light lamp', 'n']


# Given each Zork prompt, run through list of commands above
for command in commands:
    # print command
    zork.expect(">")
    zork.sendline(command)

# Wait for next prompt
# zork.expect(">")


# Slow down time a bit
zork.delaybeforesend = 1 

# Take first stab at troll (moving this down to while loop)
# zork.sendline('kill troll with sword')
# zork.expect(">")

# You can see all the data read before the match in
# 'before'. You can see the data that was matched in 'after'. The
# re.MatchObject used in the re match will be in 'match'. If an error
# occurred then 'before' will be set to all the data read so far and
# 'after' and 'match' will be None.
# pexpect must match a regex in the list or it'll time out. From SO: 
# Remember that child.expect() is a blocking call and will not return until 
# either it matches the regex or it hits EOF/TIMEOUT exception.

# Read what happens in troll room and figure out if knife gets p0wned
weapon = "sword"
i = zork.expect(["troll.*knife\.", "(sunlight\.|\[MORE\])", "brightly.*(\.|!)", pexpect.EOF, pexpect.TIMEOUT])
if i == 0:  # troll knocks away sword
  weapon = "knife"
  zork.sendline("kill troll with %s" %weapon)
  # zork.sendline("q")
  # exit(0)
  # zork.expect(">")
  # raw_input('any key')
  # print ("de-sworded")
  # print zork.after
if i == 1:  # troll kills you
  zork.sendline("deaded")
  zork.sendline("q")
  exit(0)
  zork.expect(">")
  raw_input('any key')
elif i == 2:  # troll does nothing special; move to next set
  troll_dead = False
elif i == 3:
  zork.sendline("first eof")
  print zork.after
elif i == 4:
  # zork.sendline("first timeout!")
  print ("timeout")
  print zork.before
  print zork.after
else:
  zork.sendline("first dunno")
  print zork.before
  print zork.after


while troll_dead == False:
  zork.sendline("kill troll with %s" %weapon)
  i = zork.expect(["troll.*glowing\.", "troll.*don't have", "troll.*knife\.", "troll.*sunlight\.", "troll.*disappeared\.", "troll.*have that!", "troll.*(\.|!)", pexpect.EOF, pexpect.TIMEOUT])
  if i == 0:  # troll dies; go east
    troll_dead = True
    # zork.sendline("e")
    # zork.expect(">")
  elif i == 1:    # you don't have the weapon
    zork.sendline("1st you don't have that")
    zork.logfile = None
    zork.interact()
  elif i == 2:  # troll knocks away sword
    weapon = "knife"
    # zork.sendline("2 de-sworded") # seems to work
    # print zork.after
    # zork.expect(">") # not waiting for this?
    # zork.sendline("q")   
    # exit(0)
    # zork.expect(">")
    # raw_input('any key')
  elif i == 3:  # you've died; just quit for now
    # zork.logfile = None
    # zork.interact()
    zork.sendline("2 deaded")  # not sure this or one above quite works 
    zork.expect(">")
    zork.sendline("q")   
    exit(0)
    zork.expect(">")
    raw_input('any key')
  elif i == 4:    # knife killed troll
    troll_dead = True
    zork.sendline("take sword")
  elif i == 5:   # you don't have that!
    zork.sendline("whaaaatttt! 2nd you don't have that")
    zork.sendline("q")   
    exit(0)
    zork.expect(">")
    raw_input('any key')
  elif i == 6:  # fighting continues; want to do loop again
    # zork.sendline("fight scene")
    # print zork.after
    troll_dead = False
  elif i == 7:
    zork.sendline("eof")
    print zork.after
  elif i == 8:
    zork.senkline("timeout!")
    print zork.before
    print zork.after
  else:
    zork.sendline("dunno")


# zork.expect(">")

# troll room to maze to cyclops to house 
commands = ['w', 'w', 'w', 'up', 'take key', 'take coins',
            'sw', 'e', 's', 'se', 'ulysses', 'e', 'e', 'open case',
            'put coins in case']


# Move along while keeping an eye out for the thief
for command in commands:
  i = zork.expect(["you are dead.*sunlight\.", "Someone.*body\.", "individual.*\.\"", ">"])
  if i == 0:
    zork.sendline("dead!")
    zork.sendline("q")   
    exit(0)
    zork.expect(">")
    raw_input('any key')
  if i == 1:    # thief!
    zork.sendline("hail, theif!")
    zork.logfile = None
    zork.interact()
  elif i == 2:
    zork.sendline("hello, individual!")
    zork.sendline("q")   
    exit(0)
    zork.expect(">")
    raw_input('any key')
  elif i == 3:
#    zork.expect(">")
    zork.sendline(command)

zork.expect(">")
zork.logfile = None
zork.interact()

# Turn control back over to user
# zork.logfile = None
# zork.interact()


