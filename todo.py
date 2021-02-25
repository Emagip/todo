import os # for clearing the console
from time import sleep # to pause the program


#  (☐)
#  (▣)
# todo_name_done = {"Task_name": "(▣)", "Task_name": "(☐)"}
# (▣) = completed, (☐) = not completed

todo_name_done = {} # dict holding the task name as key and the square as value

completed_tasks = [] # list holding tasks that are completed

not_completed_tasks = [] # list holding tasks that aren't completed

no_tasks = False # # for conditionals later on to determine if dict is empty or not

	
def view_tasks(): # to view all your tasks and how many are completed/uncompleted (and total number of tasks)
	  

	print("Total number of tasks: " + str(len(todo_name_done)))
	
	print("Number of uncompleted tasks: " + str(len(not_completed_tasks)))

	print("Number of completed tasks: " + str(len(completed_tasks)))

	print("\n=== Your Tasks ===\n")


	for n, i in enumerate(todo_name_done): # outputs each task
		
		# condtionals to determine if task is complete or not
		# and then puts colors according to that
		if todo_name_done[i] == "(▣)":
			
			print(str(n+1) + ") " + todo_name_done[i] + "  " + i)
		
		elif todo_name_done[i] == "(☐)":
			
			print(str(n+1) + ") " + todo_name_done[i] + "  " + i)

	print("\n")



	
	

def new_task(): # for making a new task

	print("=== New Task ===")


	while True: 

		new_task_name = input("New task? Let's add a name!\n¬ ")

	
		if new_task_name in todo_name_done: # if user already used this task name
			
			print("Sorry, you already used this task name!")
			pass
		
		else:
			
			todo_name_done[new_task_name] = "(☐)" # default (☐) not done 

			print("Creating...")

			sleep(0.4)

			os.system('clear') # clears console

			print("Alrighty, new task created!")
			
			sleep(1.3)


			not_completed_tasks.append(new_task_name) # appends that new task to the not completed list

			break # breaks while true loop and exits to main menu



def delete_task(): # to remove/delete tasks

	print("=== Delete Task ===")

	view_tasks() # calls function to see all tasks
	

	while True:

		remove_task_name = input("\nTask too difficult? Which task do you want to delete\n¬")
 
			
		if remove_task_name in todo_name_done: # if the task that the user wants to delete is a valid one

			del todo_name_done[remove_task_name] # deletes that key

			print("Deleting...")
			sleep(0.4)

			os.system('clear')

			print("Bye! Task deleted.")

			sleep(1.3)
			
			# removes that key from the completed/uncompleted lists
			# I used try and and except because the task the user wants to delete may be in one of those 2 lists
			# we don't know, that's why if the first one doesn't work, then it must be in the second list.
			try:
				
				completed_tasks.remove(remove_task_name) 
			
			except:
				
				not_completed_tasks.remove(remove_task_name)





			break # exits back to menu
		
		else:
			
			print("Hum, I can't seem to find that task. Typo?")
			pass

				



def edit_task(): # to edit a task


	print("=== Edit Task ===")


	view_tasks() # shows user all their tasks

	while True:
		task_to_edit = input("\nMade a typo? No problem! Which task name to edit?\n¬ ")

		if task_to_edit in todo_name_done: # checks if task user wants to delete is a valid one

			break

		else:
			
			print("Oh no, I can't seem to find that task. Make sure it's the correct name!")
			pass


	while True:

		new_task_name = input("\nChange " + str(task_to_edit) + " to\n¬ ")

		if new_task_name in todo_name_done: # if user chose to edit their task to a name already used
			
			print("Heads up, you already used this task name!")
			pass
		
		else:

			print("Editing...")
			sleep(0.4)

			os.system('clear')

			print(str(task_to_edit) + " edited to " + str(new_task_name))

			sleep(1.3)
			

			todo_name_done[new_task_name] = todo_name_done[task_to_edit] # makes item with different new task name and same value (box)
			del todo_name_done[task_to_edit] # deletes old key name

			# for loop to replace the name of the key in the completed/uncompleted lists
			# uses enumerate for the index of the list
			for n, i in enumerate(completed_tasks):
				if i == task_to_edit:
					
					completed_tasks[n] = new_task_name
			
			for n, i in enumerate(not_completed_tasks):
				if i == task_to_edit:
					
					not_completed_tasks[n] = new_task_name

	
			break # exits back to main menu

	




def complete_task(): # to complete a task

	print("=== Complete Task === ")

	view_tasks() # shows user their tasks


	while True: 

		if len(todo_name_done) == 0:

			print("You don't have any tasks. Create one!")
			no_tasks = True
			sleep(2)
			break
		
		else:

			no_tasks = False

		task_to_complete = input("Hurrah! Which task did you complete?\n¬ ")

		
		if task_to_complete in todo_name_done: # checks if task user wants to complete is a valid one
		
			break

		else:
			
			print("You sure that's the correct task name? I can't find it.")
			pass

	

	
	if no_tasks == False:

		print("Completing...")
		sleep(0.4)
		os.system('clear')
		
		# try and except to see if that task is already completed
		try:
			
			todo_name_done[task_to_complete] = "(▣)" # replaces empty square with the full square to indicate completed

			not_completed_tasks.remove(task_to_complete) # removes task from not completed list

			completed_tasks.append(task_to_complete) # and adds it in the completed list

			print(str(task_to_complete) + " completed!\nWell done!")

			sleep(2)

		except: # if task already completed
		
			print("Hey, you already completed this task!")
			sleep(2)

	else:
		
		pass



def un_complete_task(): # to uncomplete a task


	print("=== Un-Complete Task === ")

	view_tasks() # shows user their tasks

	while True: 

		if len(todo_name_done) == 0:
			
			print("You have 0 tasks. Go back and start one!")
			no_tasks = True
			sleep(2)
			break
		
		else:

			no_tasks = False
			


		task_to_un_complete = input("Changed your mind? Which task did you not complete?\n¬ ")

		if task_to_un_complete in todo_name_done: # checks if task that user wants to un_complete is valid
			
			break

		else: 
			
			print("I can't seem to find that task. Try again!")
			pass
	
	if no_tasks == False:

		print("Un-Completing...")
		sleep(0.4)
		
		os.system('clear')

		# try and except to see if that task is already uncompleted
		try:

			todo_name_done[task_to_un_complete] = "(☐)" # replaces full square with empty square to indicate not completed

			completed_tasks.remove(task_to_un_complete) # removes task from completed list

			not_completed_tasks.append(task_to_un_complete) # and adds it to not completed list

			print(str(task_to_un_complete) + " Un-Completed!\nMake sure to complete it!")

			sleep(2)
			
		except: # if task is already uncompleted
			
			print("Wait a minute, you already un-completed this task!")
			sleep(2)


	else:
		
		pass
		
	


def main_menu(): # main menu with different choices

	os.system('clear') # clears console
	
	view_tasks() # outputs all the user's task

	# outputs different choices 
	print("""                           
                        
 (1) New Task               
 (2) Delete Task         
 (3) Edit Task           
                      
 (4) Complete Task       
 (5) Un-Complete Task                    
                            
	""")

	menu_choice = input("¬ ") # main menu choice for user
	
	os.system('clear')


	# conditionals to determine what user wants to do
	if menu_choice == "1":

		new_task()

	if menu_choice == "2":

		delete_task()

	elif menu_choice == "3":

		edit_task()

	elif menu_choice == "4":
		
		complete_task()

	elif menu_choice == "5":
		
		un_complete_task()
	



while True: # actual running of everything
	
	main_menu()
