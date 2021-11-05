from tkinter import *
from time import sleep,strftime

#create an empty list
button=[]

#create another empty list
state=[]

#create a variable to store the player 
#winner
winner=""

#create a two-dimensional list of zeros
for i in range(3):
	button.append([0,0,0])
	#Add another two-dimensional list that 
	#will store the current player state to
	#avoid re-editing a cell that has 
	#already been altered
	state.append([0,0,0])

#Create a callback function that will
#change the cells accordingly
def callback(r,c):
	#use a  global variable to alter the 
	#value of the original variable
	global current_player
	global winner
	#If the stop game variable is true
	#none of the conditional statements 
	#will execute!
	
	if current_player=="X" and state[r][c]==0 and stop_game!=True:
		button[r][c].configure(text="X")
		current_player="O"
		#store the current state
		#to avoid re-editing
		state[r][c]="X"
		winner="X"
	
	elif current_player=="O" and state[r][c]==0 and stop_game!=True:
		button[r][c].configure(text="O")
		current_player="X"
		#store the current_state
		#to avoid re-editing
		state[r][c]="O"
		winner="O"
	#call the check_winner function
	check_winner()

#Create a Function To check for the winner
def check_winner():
	#make the stop game variable global
	global stop_game
	
	"""Check for horizontal match in all 3 horizontal cells
	"""
	for i in range(3):
		if state[i][0]==state[i][1]==state[i][2]!=0:
			button[i][0].configure(bg="grey")
			button[i][1].configure(bg="grey")
			button[i][2].configure(bg="grey")
			"""once they match,set the stop game variable to True"""
			stop_game=True
			
	"""check for vertical match in all 
3 vertical cells"""
	for i in range(3):
		if state[0][i]==state[1][i]==state[2][i]!=0:
			button[0][i].configure(bg="grey")
			button[1][i].configure(bg="grey")
			button[2][i].configure(bg="grey")
			stop_game=True
			
	"""check for right diagonal match"""
	if state[0][0]==state[1][1]==state[2][2]!=0:
			button[0][0].configure(bg="grey")
			button[1][1].configure(bg="grey")
			button[2][2].configure(bg="grey")
			stop_game=True
			
	"""check for left diagonal match"""
	if state[0][2]==state[1][1]==state[2][0]!=0:
			button[0][2].configure(bg="grey")
			button[1][1].configure(bg="grey")
			button[2][0].configure(bg="grey")
			stop_game=True
			
	if stop_game==True:
		winner_label.configure(text="Winner is player {}".format(winner))

#create a restart function,to restart the
#game
def restart():
		#create a global variable to be able
		#to edit the stop game variable
		global stop_game
		#we need to reset everything back
		#to default
		
		#return stop game back to false
		stop_game=False
		
		for i in range(3):
			for j in range(3):
				#reset state list
				state[i][j]=0
				#reset the button visuals
				button[i][j].configure(text="",bg="green",command=lambda r=i,c=j:callback(r,c))

#Time function
#it configures the label with the string 
#variable every 1second

def time_display():
	time_string=strftime("%H:%M:%S %p")
	time_label.config(text=time_string)
	time_label.after(1000,time_display)
		
root=Tk()
root.title("Tic Tac Toe Game")
#Make 9 buttons and display them on the grid
for i in range(3):
	for j in range(3):
		button[i][j]=Button(text="",bg="green",font=("courier",20),width=2,height=2,command=lambda r=i,c=j:callback(r,c))
		button[i][j].grid(row=i,column=j)

#create a label to show the winner
winner_label=Label(text="Winner:",font=("courier",10))
#create an exit button
exit_button=Button(text="Exit",font=("courier",6),width=5,command=exit)

#create a restart button
restart_button=Button(text="Restart",width=5,font=("courier",6),command=restart)

#time label
time_label=Label(font=("courier",10),bg="black",fg="green",width=12,height=2)
time_label.grid(row=5,column=0,columnspan=2,rowspan=2)


time_display()


#Grid the winner label,restart button
#and exit_button
winner_label.grid(row=4,column=0,columnspan=3)
restart_button.grid(row=5,column=2)
exit_button.grid(row=6,column=2)


#create a player variable to start as the
#first player
current_player="X"
#create a stop game boolean variable,to stop
#the game once the 3 cells match
stop_game=False

root.mainloop()
