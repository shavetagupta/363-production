from psychopy import visual,core,event,clock,data
from list import wl1,wl2,wlr			#three word pools from list.py
import random
underline_list = []
normal_list = []
distractor_list = []

def make_list():	
	rannum1 = random.sample(range(0,20),16) #generate 16 numbers 0 to 19
	rannum2 = random.sample(range(0,20),16) #have to generate 3 random sequences
	rannum3 = random.sample(range(0,20),16) #for each pool in list.py	
	for i in rannum1:			#goes through each number in rannum1
		underline_list.append(wl1[i])        #take 16 random words from wl1 and give them to show_list 
	for o in rannum2:
		normal_list.append(wl2[o])
make_list()		
print(normal_list)
print(underline_list)