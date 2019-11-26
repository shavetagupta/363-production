from psychopy import visual,core,event,clock,data
from list import silent_list,read_list,distractor_list				
import random
test_list_1 = []
test_list_2 = []
test_list = []
intro1 = "Welcome to our study.\n \nIn this first part, you will see words appearing one at a time.\n \nPlease read white words silently without moving your lips and blue words aloud. \n \nYour memory for these words will be tested later regardless of the color. \n \nPress spacebar to begin."
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
	random.shuffle(test_list)

partName = input('Input participant codename:')
gender = input ('What is your gender? (M/F/O/NA)')

win = visual.Window([600, 600],color = 'black', allowGUI = False)
show = visual.TextStim(win, text = intro1, color = 'white', height = 0.05, pos = (0.5,0.0))
show.draw()
win.flip()

if event.waitKeys(keyList=['space']):	
	c = 0 
	while c < 20: 
		show = visual.TextStim(win, text = silent_list[c], color = 'white', pos = (0.75,0.0))
		show.draw()
		win.flip()
		core.wait(2.25)
		show = visual.TextStim(win, text = read_list[c], color = 'blue', pos = (0.75,0.0))
		show.draw()
		win.flip()
		core.wait(2.25)
		c = c + 1

show = visual.TextStim(win, text = intro2, color = 'white', height = 0.05, pos = (0.5,0.0))
show.draw()
win.flip()
make_test()
filename = 'results_' + partName + gender + '.csv'
f = open(filename,'a+')
f.write("trial,word,list,assessment,identification\n")

if event.waitKeys(keyList=['space']):
	for i in range(0,40):
		show = visual.TextStim(win, text = test_list[i], color = 'yellow', pos = (0.75,0.0))
		show.draw()
		win.flip()
		f.write(str(i + 1) + ',' + test_list[i] + ',')
		press = event.waitKeys(keyList = ['y','n'])
		if 'y' in press:
			if test_list[i] in silent_list:
				f.write("silent,correct,identification\n")
			elif test_list[i] in read_list:
				f.write('read,correct,identification\n')	
			else:
				f.write('distract,false,identification\n')
		else:
			if test_list[i] in silent_list:
				f.write('silent,false,rejection\n')
			elif test_list[i] in read_list:
				f.write('read,false,rejection\n')
			else:
				f.write('distract,correct,rejection\n')
f.close()

show = visual.TextStim(win, text = 'Thank you for participating.', color = 'white', height = 0.05, pos = (0.5,0.0))
show.draw()
win.flip()
core.wait(5.0)
win.close()

#cor_id
#fal_id
#cor_rej
#fal_rej


