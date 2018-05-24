# sorting-visual

    Abstract:
This project’s goal is to implement a program that does the animation of sorting algorithms. The user is allowed to put whichever algorithm in the form of pseudo-code, so that he can see its animation.


    Introduction:
Computer Science is full of utilizations of sorting algorithms. Either in fields of algorithm analysis, operating systems, or many other fields, sorting algorithms are used to sort different elements, and some algorithms are made to further optimize this sorting. Moreover, there are several tens of existing sorting algorithms, each with its own advantages, disadvantages, and situations to be used in. These aforementioned thoughts made me impressed by how strong and dazzling many of these algorithms are, and made me motivated to do something that would help people in the process of learning them. 
This program’s objective is to allow the user to enter an array of elements he wants to sort, and the pseudo-code of the sorting algorithm he wants to use, and the program would do the animation for him. To reach that objective, the program reads the algorithm line by line, and makes the animation of each line separately. Also, the program follows certain specifications and syntax that would be imposed on the user in the pseudo-code he enters


    What does the program do?
This program functions following these steps: 
  1- The program is prompted. The user is asked to enter the number of elements he wants to sort; 
  2- The user enters 5 as the number of elements for instance, and then starts entering the elements themselves; 
  3- Once the five elements are entered, the user is prompted to enter the pseudo-code of the algorithm; 
  4- Then, the user enters the pseudo-code of the algorithms? 
  5- After that, the user hits ‘GO’, and the program starts to parse and animate. The first thing it does is that it creates a table of all the variable that were declared in the algorithm, and displays them along with their actual values; 
  6- Then, the program parses the first line and starts the animation. The line being parsed will always be in yellow; 
  7- And so on ...
  

    Description of the technology used:
The language used in this project is Python. Since the beginning of my studies, I was always urged and pushed to learn Python myself, since it is not part of the languages taught in our curriculum. I was always told how clear and easy-to-use Python is. However, this project was my first encounter with this language, and learning it was not as complicated as I had imagined. Having learnt many languages beforehand, and from different paradigms, learning a simple, High-Level language was not hard at all, and this is one of the major advantages of Python.
In order to start implementing the interface, I needed to find a suitable library that would fulfill our graphical needs. Therefore, I needed to find a library that wraps Tkinter, and that provides with the graphical features needed for the interface. I started first with graphics.py, a library written by John Zelle, and which provides the user with elementary graphical objects needed for basic graphical purposes. However, some of the needed graphical features were not provided, and we tried to find a better alternative. Graphics.py was lacking two essential features: buttons and the multiline text field. Concerning the buttons, I was able to hardcode it and make our own buttons, using rectangles and mouse events. However, I could not hardcode the multiline text field, and I did not find any other library that implements it. I thought of adding the multiline text field to the graphics.py library by imitating how Zelle wrapped the Tkinter library. However, there was a major inconsistency between graphics.py and Tkinter libraries in terms of terminology, since the Text feature in graphics.py is used for mere text without any box around it, while the Text in Tkinter is used for the whole field that is created for the text. Hence, I decided to carry on with graphics.py, and that I would put many entries next to each other instead of one multiline text field. 
After the graphical implementation of the program, I moved to the parsing part, and in which I used only built-in libraries in Python 3.3. Some of these libraries were ‘string.py’ for string operations, and ‘re.py’ for regular expression operations. These two libraries were not indispensable to the code, and I preferred, sometimes, coding my own functions that would fulfill our very specific needs.


    How does the code work?
As previously seen, the algorithm starts by taking the number that the user wants to sort. These numbers are put in an array, and are displayed in the interface for the simulation later on. Then, the program parser is made of an algorithm based on three major steps:
  a)	Storing the algorithm in a double array:
  The first major step of our parser is to tokenize the full algorithm and to put in a double array. The rows of the array are the lines, and the elements of each line are the words (here, the tokenization is done with spaces). This double array will be used throughout the whole parsing part of the program as the source of the sorting algorithm.
  b)	Taking the first token in the line being processed and deciding whether it is an assignment, a loop, or a decision:
  Since each row of our double array is a line in the algorithm, the program takes the first token of the row corresponding to the line being processed, in order to decide about the nature of the line. This latter step is done thanks to the function ‘codeLineIdentifier()’. Here, three scenarios are possible. If this first token is ‘for’, then the program needs to take the second token which represents the variable used in the loop, and the fifth token which represents the number of iterations. Then, the program calls the ‘forhandler()’ function to iterate over the following lines of algorithm the appropriate number of times until it reaches the line ‘end of for’. If the first token of the line is ‘if’, the program calls the ‘ifhandler()’ function and takes all what comes after the ‘if’ as the condition to check if it is true. If so, the program runs all what comes next until it reaches the line ‘end of if’. Otherwise, the program finds the line ‘end of if’, and runs the algorithm from the following line. The third and last scenario is when the program finds that the first token is neither a ‘for’ nor an ‘if’. In this case it calls the ‘assignhandler()’ function which checks again that same first token. If the token is ‘swap’, then it knows that the line is for swapping two elements of the array, and so, it takes the second and third tokens, which represent the two elements to be swapped, and calls the function ‘simulation()’. Otherwise, anything else will be considered as a variable, and will be stored and displayed if the variable is newly declared. In this latter case, there are two scenarios: the line might be to update the variable, or to assign to it another variable. In the first scenario, the program calls the function ‘varupdatesim()’, and in the second one it calls the function ‘simpleassignsim()’.   
  To fully understand how the program works, it is essential to mention that the program has a global variable which is ‘nextLine’. This variable is updated by each handler function to keep track of which line the program has reached so far. This variable proved to be very essential for the loop which exists in the main function, and which iterates over the lines of the algorithm to process them. 


    Algortithm's Pseudo-code specificiations:
While implementing the parser side of our program, one key decision I faced was to decide about the syntax I would like the user to use in his algorithm’s pseudo-code. In other words, I needed to set the constraints I would put on the user. 
These specifications are the following:
  a)	The array of numbers that are subject to swapping must be addressed as ‘a[int or expression]’. If the user uses an array name different than ‘a’, the program would consider it as a variable. Such decision comes from the fact that I wanted to make it very generic, but I put ‘a’ instead of ‘array’ to make it less cumbersome.
  b)	The loop must be written like Python’s way of writing it. Also, it must end with the line ‘end of for’. Also, the for-loop is the only way that we implemented for loops, so the user cannot use the while or the do-while.
  c)	The decision must be ‘if decision’. Also, it must end with the line ‘end of if’.
  d)	Between each two words, there must be a space.
  e)	To make a swapping of two elements, the user must use the syntax: swap ‘1st element’ ‘2nd element’.

