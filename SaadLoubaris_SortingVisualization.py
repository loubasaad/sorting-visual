from graphics import *
from string import *
import re


nextline = 0

def exercise():
	win = GraphWin("Win", 1360, 730)

	sou2al = Text(Point(150,50), "Please enter the number of numbers: ")
	sou2al.draw(win)

	#Field to enter number of numbers
	blassasou2 = Entry(Point(320, 50), 5)    
	blassasou2.draw(win)
	#Button to validate the answer
	jawab = Rectangle(Point(360, 35), Point(410, 65))   
	jawab.draw(win)
	jaw = Text(Point(385, 51), "Next")
	jawab.setFill('white')
	jaw.draw(win)
	

	#Button to add lines
	addline = Rectangle(Point(675,75), Point(775, 120))    
	addline.setFill('white')
	addline.draw(win)
	addlinetext = Text(Point(725, 97), "Add Line")
	addlinetext.draw(win)

    #Button to launch the animation
	addline2 = Rectangle(Point(675, 130),Point(775, 175))    
	addline2.setFill('white')
	addline2.draw(win)
	addlinetext2 = Text(Point(725, 152), "GO!!")
	addlinetext2.draw(win)

	#Draw the 10 default lines where to enter the algorithm
	mylines = []
	for i in range(10):
		mylines.append(Entry(Point(1000,(i+2)*21),40))
		num = i
		mylines[i].draw(win)

	end = 0
	cnt = 0
	num=num+1

	while end == 0:
		#Get the mouse action
		mimi = win.getMouse()
		if mimi.getX()>675 and mimi.getX()<775 and mimi.getY()>75 and mimi.getY()<120:     #If the user clicks on 'Add line'
			addlinetext.setStyle('bold')
			addlinetext.setTextColor('red')
			time.sleep(0.2)
			addlinetext.setStyle('normal')
			addlinetext.setTextColor('black')
			mylines.append(Entry(Point(1000,(num+2)*21),40))
			mylines[num].draw(win)
			num = num+1
		elif mimi.getX()>675 and mimi.getX()<775 and mimi.getY()>130 and mimi.getY()<175:     #If the user clicks on 'GO!!'
			addlinetext2.setStyle('bold')
			addlinetext2.setTextColor('red')
			time.sleep(0.2)
			addlinetext2.setStyle('normal')
			addlinetext2.setTextColor('black')
			inputt = []
			gigi = Text(Point(400, 500), "")
			gigi.draw(win)
			for i in range(num):
				inputt.append(mylines[i].getText())

			# Create the double array of words needed for parsing
			listwords = []
			for i in range(num):
				listwords.append(inputt[i].split())

			print(listwords)

			rows = len(listwords)
			wantedwords = []

			unwantedset = set(["swap", "for", "if", "else", "end", "of", ":", "+", "*", "-", "/", "range", "in", "(", ")", "=", "==", "!=", "<", ">"])

			#Create a set of the variables used
			for i in range (rows):
				for j in range(len(listwords[i])):
					if ((listwords[i][j].startswith("a[") == False) & (listwords[i][j].isdigit() == False) & (listwords[i][j] not in unwantedset) ):
						wantedwords.append(listwords[i][j])

			setofwords = set(wantedwords)

			print(wantedwords)
			wantedlength = len(wantedwords)

			#Draw the variables in the middle of the window when the animation begins
			totalw = 100*wantedlength
			middlew = totalw/2
			midw = 500 - middlew


			print(setofwords)

			arrayvartext = []
			arrayvarname = []
			arrayvarvalue = []

			i = 0
			for x in setofwords:
				p1 = Point(midw+100*(i), 450)
				p2 = Point(midw+100*(i+1), 450+50)
				rectw = Rectangle(p1, p2)
				rectw.draw(win)
				p5 = Point(midw+50+100*i, 475)
				textw = Text(p5, x)
				arrayvarname.append(x)
				textw.draw(win)
				p3 = Point(midw+100*(i), 500)
				p4 = Point(midw+100*(i+1), 500+50)
				rectw2 = Rectangle(p3, p4)
				rectw2.draw(win)	
				p6 = Point(midw+50+100*i, 525)
				textw2 = Text(p6, "0")
				arrayvartext.append(textw2)
				arrayvarvalue.append(0)
				textw2.draw(win)
				i = i + 1			


			numberlines = len(listwords)
			print(numberlines)

			nextline = 0
			for i in range(numberlines):
				nextline = codeLineIdentifier(listwords[nextline], setofwords, arrayvarname, arrayvartext, arrayvarvalue, listnumbers, listwords, mylines, listtexts, nextline, win)
			# codeLineIdentifier(listwords[1], setofwords, arrayvarname, arrayvartext, arrayvarvalue, listnumbers, listwords, mylines, listtexts, win)
			# codeLineIdentifier(listwords[2], setofwords, arrayvarname, arrayvartext, arrayvarvalue, listnumbers, listwords, mylines, listtexts, win)
			# codeLineIdentifier(listwords[3], setofwords, arrayvarname, arrayvartext, arrayvarvalue, listnumbers, listwords, mylines, listtexts, win)
			# codeLineIdentifier(listwords[4], setofwords, arrayvarname, arrayvartext, arrayvarvalue, listnumbers, listwords, mylines, listtexts, win)

			print(listnumbers)

				# p3 = Point(mid+25+50*i, 300)
				# text = Text(p3, number)
				# listtexts.append(text)
				# listnumbers.append(number)
				# text.draw(win)
		

			# for i in range(numofnum):
			# 	print(listnumbers[i])
			# for i in range(num):
			# 	gigi.setText(inputt[i])
			# 	time.sleep(2)
				# print(i)	


		#If the user clicks on 'Next' when inputting the number of numbers to sort
		elif mimi.getX()>360 and mimi.getX()<410 and mimi.getY()>35 and mimi.getY()<65:
			jaw.setTextColor('red')
			jaw.setStyle('bold')
			time.sleep(0.2)
			jaw.setTextColor('black')
			jaw.setStyle('normal')
			numofnum = eval(blassasou2.getText())
			blassasou2.setText("")
			sou2al.undraw()
			
			sou2al = Text(Point(150, 50), "Please enter a number: ")
			sou2al.draw(win)
			totallength = 50*numofnum
			middle = totallength/2
			mid = 250 - middle
			listnumbers = []
			listtexts = []

			for i in range(numofnum):
				riri = win.getMouse()
				#When the user clicks on 'Next' while entering the numbers, these numbers are being drawn one at a time
				if riri.getX()>360 and riri.getX()<411 and riri.getY()>35 and riri.getY()<65:
					totallength = 50*numofnum
					middle = totallength/2
					mid = 250 - middle

					jaw.setTextColor('red')
					jaw.setStyle('bold')
					time.sleep(0.2)
					jaw.setTextColor('black')
					jaw.setStyle('normal')
					number = blassasou2.getText()
					blassasou2.setText("")
					p1 = Point(mid+50*(i), 275)
					p2 = Point(mid+50*(i+1), 275+50)
					rect = Rectangle(p1, p2)

					rect.draw(win)
					p3 = Point(mid+25+50*i, 300)
					text = Text(p3, number)
					listtexts.append(text)
					listnumbers.append(number)
					text.draw(win)
			jawab.undraw()
			jaw.undraw()
			sou2al.undraw()
			blassasou2.undraw()
			animationstart = Text(Point(150, 50), "ANIMATION")
			animationstart.setSize(20)
			animationstart.draw(win)
	  


#Function that does the simulation when updating the value of a variable
def varupdatesim(nameofvar, newvalue, array1, array2, array3, windo):
	time.sleep(2)
	index = array1.index(nameofvar)
	array3[index] = newvalue
	anchor = array2[index].getAnchor()
	array2[index].setTextColor('red')
	array2[index].setStyle('bold')
	array2[index].setSize(15)
	time.sleep(2)
	array2[index].undraw()
	array2[index] = Text(anchor, newvalue)
	array2[index].draw(windo)
	array2[index].setTextColor('red')
	array2[index].setStyle('bold')
	array2[index].setSize(15)
	time.sleep(2)
	array2[index].setTextColor('black')
	array2[index].setStyle('normal')
	array2[index].setSize(12)



#Function that does the simulation when assigning the value of a variable to another variable
def simpleassignsim(lhsvar, rhsvar, array1, array2, array3, windo):
	
	lhsindex = array1.index(lhsvar)
	rhsindex = array1.index(rhsvar)
	
	lhsanchor = array2[lhsindex].getAnchor()
	rhsanchor = array2[rhsindex].getAnchor()

	lhstext = array3[lhsindex]
	rhstext = array3[rhsindex]

	stepsize = 1

	# array2[rhsindex].undraw()

	time.sleep(2)

	array2[rhsindex].setTextColor('red')
	array2[rhsindex].setStyle('bold')
	array2[rhsindex].setSize(15)
	time.sleep(2)

	for i in range(35):
		text = Text(Point(rhsanchor.getX(), rhsanchor.getY()+stepsize*(i+1)), rhstext)
		text.draw(windo)
		text.setStyle('bold')
		text.setTextColor('red')
		text.setSize(15)
		time.sleep(0.02)
		text.undraw()

	currenty = rhsanchor.getY()+stepsize*(i+1)
	xdisplacement = lhsanchor.getX()-rhsanchor.getX()

	if xdisplacement < 0:
		stepsize = -1 * stepsize

	numsteps = int(xdisplacement/stepsize)

	text = Text(Point(rhsanchor.getX(), currenty), rhstext)
	
	for j in range(numsteps):
		text = Text(Point(rhsanchor.getX()+stepsize*j, currenty), rhstext)
		text.draw(windo)
		text.setStyle('bold')
		text.setTextColor('red')
		text.setSize(15)
		time.sleep(0.02)
		text.undraw()

	stepsize = 1
	for i in range(35):
		text = Text(Point(lhsanchor.getX(), rhsanchor.getY()+stepsize*(35)-stepsize*(i+1)), rhstext)
		text.draw(windo)
		text.setStyle('bold')
		text.setTextColor('red')
		text.setSize(15)
		time.sleep(0.02)
		text.undraw()


	array2[lhsindex].undraw()
	array2[lhsindex].setText(rhstext)
	array2[lhsindex].draw(windo)
	array2[lhsindex].setTextColor('red')
	array2[lhsindex].setStyle('bold')
	array2[lhsindex].setSize(15)
	time.sleep(2)
	array2[lhsindex].setTextColor('black')
	array2[lhsindex].setStyle('normal')
	array2[lhsindex].setSize(12)
	array2[rhsindex].setTextColor('black')
	array2[rhsindex].setStyle('normal')
	array2[rhsindex].setSize(12)


def twoarraysim(t, x, windo):

	tx = t.getAnchor().getX()
	ty = t.getAnchor().getY()

	xx = x.getAnchor().getX()
	xy = x.getAnchor().getY()

	xtext = x.getText()
	ttext = t.getText()

	xdisplacement = xx - tx
	ydisplacement = xy - ty

	bigstepsize = 1

	print("1")

	if(xdisplacement<ydisplacement):
		bigdisplacement = ydisplacement
		smalldisplacement = xdisplacement

	else:
		bigdisplacement = xdisplacement
		smalldisplacement = ydisplacement

	print("2")


	numsteps = int(bigdisplacement/bigstepsize)	 

	smallstepsize = int(smalldisplacement/numsteps)

	xstepsize = bigstepsize
	ystepsize = bigstepsize

	bigxstepsize = xstepsize
	bigystepsize = ystepsize

	print("3")

	if(xdisplacement<0):
		bigxstepsize = (-1) * xstepsize

	if(ydisplacement<0):
		bigystepsize = (-1) * ystepsize

	print(bigystepsize)
	print(bigxstepsize)

	for i in range(numsteps):
		textt = Text(Point(tx+bigxstepsize*(i+1),ty+bigystepsize*(i+1)), ttext)
		textx = Text(Point(xx+bigxstepsize*(i+1)*(-1),xy+bigystepsize*(i+1)*(-1)), xtext)
		textt.draw(windo)
		textx.draw(windo)
		time.sleep(0.02)
		textt.undraw()
		textx.undraw()

	print("1")




#Function that handles the simulation of the operations
def simulation(line, t, x, array, array2, array3, array4, windo):
	lengt = len(t)
	lengx = len(x)

	operatorset = set(['+', '-', '*', '/'])

	lhscontent = t[2:lengt-1]
	rhscontent = x[2:lengx-1]

	# if(lhscontent.isdigit)
	setarray3 = set(array3)

	lhsdelimited = expressioneval(lhscontent, operatorset)
	rhsdelimited = expressioneval(rhscontent, operatorset)

	lhsdelimitedlen = len(lhsdelimited)
	rhsdelimitedlen = len(rhsdelimited)

	for i in range(lhsdelimitedlen):
		if(lhsdelimited[i] in setarray3):
			lhsindexii = array3.index(lhsdelimited[i])
			lhsdelimited[i] = str(array4[lhsindexii])

	lhsdelimitedlen = len(lhsdelimited)
	lhsevaluated = ""
	for i in range(lhsdelimitedlen):
		lhsevaluated = lhsevaluated + lhsdelimited[i]

	# lhsevaluated = int(lhsevaluated)
	print(lhsevaluated)
	lhsevaluated = int(eval(lhsevaluated))

	


	for i in range(rhsdelimitedlen):
			if(rhsdelimited[i] in setarray3):
				indexii = array3.index(rhsdelimited[i])
				rhsdelimited[i] = str(array4[indexii])

	rhsdelimitedlen = len(rhsdelimited)
	rhsevaluated = ""
	for i in range(rhsdelimitedlen):
		rhsevaluated = rhsevaluated + rhsdelimited[i]

	# rhsevaluated = int(rhsevaluated)
	print(rhsevaluated)
	rhsevaluated = int(eval(rhsevaluated))

	time.sleep(0.5)

	tanchor = array[lhsevaluated].getAnchor()
	xanchor = array[rhsevaluated].getAnchor()

	tx = tanchor.getX()
	ty = tanchor.getY()
	xx = xanchor.getX()

	# tt = t.getText()
	# xt = x.getText()		


	ttext = array[lhsevaluated].getText()
	xtext = array[rhsevaluated].getText()

	stepsize = 1

	array[rhsevaluated].setTextColor('red')
	array[rhsevaluated].setStyle('bold')
	array[rhsevaluated].setSize(15)
	array[lhsevaluated].setTextColor('red')
	array[lhsevaluated].setStyle('bold')
	array[lhsevaluated].setSize(15)
	time.sleep(2)
	array[rhsevaluated].undraw()
	array[lhsevaluated].undraw()


	for i in range(35):
		text1 = Text(Point(xx, ty+stepsize*(i+1)), xtext)
		text1.draw(windo)
		text1.setStyle('bold')
		text1.setTextColor('red')
		text1.setSize(15)
		text2 = Text(Point(tx, ty+stepsize*(i+1)), ttext)
		text2.draw(windo)
		text2.setStyle('bold')
		text2.setTextColor('red')
		text2.setSize(15)
		time.sleep(0.02)
		text1.undraw()
		text2.undraw()


	currenty = ty+stepsize*(i+1)
	xdisplacement = tx-xx

	if (xdisplacement < 0):
		stepsize = -1 * stepsize

	numsteps = int(xdisplacement/stepsize)

	text1 = Text(Point(xx, currenty), xtext)
	text2 = Text(Point(tx, currenty), ttext)	

	for j in range(numsteps):
		text1 = Text(Point(xx+stepsize*j, currenty), xtext)
		text1.draw(windo)
		text1.setStyle('bold')
		text1.setTextColor('red')
		text1.setSize(15)
		text2 = Text(Point(tx+stepsize*(-1)*j, currenty), ttext)
		text2.draw(windo)
		text2.setStyle('bold')
		text2.setTextColor('red')
		text2.setSize(15)
		time.sleep(0.02)
		text1.undraw()
		text2.undraw()

	stepsize = 1
	for i in range(35):
		text1 = Text(Point(tx, ty+stepsize*(35)-stepsize*(i+1)), xtext)
		text1.draw(windo)
		text1.setStyle('bold')
		text1.setTextColor('red')
		text1.setSize(15)
		text2 = Text(Point(xx, ty+stepsize*(35)-stepsize*(i+1)), ttext)
		text2.draw(windo)
		text2.setStyle('bold')
		text2.setTextColor('red')
		text2.setSize(15)
		time.sleep(0.02)
		text1.undraw()
		text2.undraw()


	array[lhsevaluated].setText(xtext)
	array[rhsevaluated].setText(ttext)

	array[lhsevaluated].draw(windo)
	array[rhsevaluated].draw(windo)

	array[rhsevaluated].setSize(15)
	array[rhsevaluated].setStyle('bold')
	array[rhsevaluated].setTextColor('red')
	array[lhsevaluated].setSize(15)
	array[lhsevaluated].setStyle('bold')
	array[lhsevaluated].setTextColor('red')
	time.sleep(2)
	array[rhsevaluated].setSize(12)
	array[rhsevaluated].setStyle('normal')
	array[rhsevaluated].setTextColor('black')
	array[lhsevaluated].setSize(12)
	array[lhsevaluated].setStyle('normal')
	array[lhsevaluated].setTextColor('black')

	temp = array2[lhsevaluated]
	array2[lhsevaluated] = array2[rhsevaluated]
	array2[rhsevaluated] = temp


	

#Function that handles the line of the algorithm being parsed taking into account the if statements and the loops
def codeLineIdentifier(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo):
	indexline = array5.index(line)
	if (line[0] == 'for'):
		array6[indexline].setFill('red')
		nextline = forhandler(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo)
		array6[indexline].setFill('gray')

	elif (line[0] == "if"):
		array6[indexline].setFill('red')
		nextline = ifhandler(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo)
		array6[indexline].setFill('gray')


	else:
		array6[indexline].setFill('yellow')
		nextline = assignhandler(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo)
		array6[indexline].setFill('gray')

	return nextline


#Function that checks wether the operation is a simple assignment or a swap operation, and does the simulation
def assignhandler(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo):
	linelength = len(line)
	i = array5.index(line)
	if (linelength-2 == 1):
		if ((line[0] in setw) & (line[2].isdigit() == False)):
			simpleassignsim(line[0], line[2], array1, array2, array3, windo)

		elif ((line[0] in setw) & (line[2].isdigit() == True)):
			varupdatesim(line[0], eval(line[2]), array1, array2, array3, windo)

		elif (line[0] == "swap"):
			t = line[1]
			x = line[2]
			simulation(line, t, x, array7, array4, array1, array3, windo)
	nextline = i + 1
	return nextline
			

#Function that handles the for loops
def forhandler(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo):
	indexi = array5.index(line)
	rangee = eval(line[5])
	print("rangee is :" + str(rangee))
	for i in range(rangee):
		j = indexi + 1
		while((array5[j][0] != "end") & (array5[j][2] != "for")):
			codeLineIdentifier(array5[j], setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo)
			j = j + 1
	nextline = j + 1
	return nextline

#Function that handles the if statements
def ifhandler(line, setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo):
	indexi = array5.index(line)
	operatorset = set(['+', '-', '*', '/', '<', '>', '=='])
	setarray3 = set(array3)

	linelen = len(line)
	condition = ""
	for i in range(linelen-1):
		if(line[i+1] in setarray3):
			indexword = array3.index(line[i+1])
			valueword = array1[indexword]
			condition = condition + valueword
		else:
			condition = condition + line[i+1]
	i = indexi + 1
	if(eval(condition) == True):
		while((array5[i][0] != "end") & (array5[i][2] != "if")):
			codeLineIdentifier(array5[i], setw, array1, array2, array3, array4, array5, array6, array7, nextline, windo)
			i = i + 1
	else:
		while((array5[i][0] != "end") & (array5[i][2] != "if")):
			print("no")
			i = i + 1

	nextline = i + 1
	return nextline


#Function to evaluate an expression
def expressioneval(expression, delimiters):
	expressionlen = len(expression)
	text=[]
	lastindex = 0
	for i in range(expressionlen):
		if(expression[i] in delimiters):
			text.append(expression[lastindex:i])
			text.append(expression[i])
			lastindex = i+1
	text.append(expression[lastindex:i+1])

	return text


#Launch the program
exercise()