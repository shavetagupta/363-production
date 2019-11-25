from psychopy import visual,core,event,clock,data
from list import silent_list,read_list,distractor_list				
import random
test_list_1 = []
test_list_2 = []
test_list = []
intro1 = "Welcome to our study.\n \nIn this first part, you will see words appearing one at a time.\n \nPlease read white words silently without moving your lips and red words aloud. \n \nYour memory for these words will be tested later regardless of the color. \n \nPress spacebar to begin."
intro2 = "In the next part, you will see words appearing one at a time.\n \nPlease press Y if you remember seeing the word in the last part, and N if you don't remember seeing the word. \n \nPress spacebar to proceed."

def make_test():	
	rannum1 = random.sample(range(0,20),10) 	
	rannum2 = random.sample(range(0,20),10)	
	for i in rannum1:				
		test_list_1.append(silent_list[i])        	
	for o in rannum2:
		test_list_2.append(read_list[o])
	global test_list
	test_list = test_list_1 + test_list_2 + distractor_list
				

win = visual.Window([600, 600],color = 'black', allowGUI = False)
show = visual.TextStim(win, text = intro1, color = 'white', height = 0.05, pos = (0.5,0.0))
show.draw()
win.flip()

if event.waitKeys(keyList=['space']):	
	c = 0 
	while c < 20: 
		show = visual.TextStim(win, text = silent_list[c], color = (1,1,1), pos = (0.75,0.0))
		show.draw()
		win.flip()
		core.wait(2.5)
		show = visual.TextStim(win, text = read_list[c], color = (1, -1, -1), pos = (0.75,0.0))
		show.draw()
		win.flip()
		core.wait(2.5)
		c = c + 1

show = visual.TextStim(win, text = intro2, color = 'white', height = 0.05, pos = (0.5,0.0))
show.draw()
win.flip()
make_test()
random.shuffle(test_list)
id_silent = 0
id_read  = 0
reject = 0
false_id = 0
f = open('results.txt','a+')

if event.waitKeys(keyList=['space']):
	for i in range(0,40):
		show = visual.TextStim(win, text = test_list[i], color = 'white', pos = (0.75,0.0))
		show.draw()
		win.flip()
		press = event.waitKeys(keyList = ['y','n'])
		if 'y' in press:
			if test_list[i] in silent_list:
				id_silent = id_silent+1
			elif test_list[i] in read_list:
				id_read = id_read+1
			else:
				false_id = false_id+1
		else:
			reject = reject + 1
result = id_read - id_silent
f.write(str(result))
f.close()
win.close()



