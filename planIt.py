__author__ = "Arhaan Ahmad"
__license__ = "Apache 2.0"
__version__ = "v1.0.1"
__email__ = "arhaan.ahmad2003@gmail.com"
__status__ = "Beta"

###Imports
import datetime
###Imports End

data = "usrData.txt"
tt = "timeTable.txt"
commandFile = open("commands.txt","r")
commandArray = commandFile.readlines()

class commands:
	#Stores the various commands
	setCommand = commandArray[0].split(" ")[1].strip()
	quitCommand = commandArray[1].split(" ")[1].strip()
	deleteCommand = commandArray[2].split(" ")[1].strip()
	displayCommand = commandArray[3].split(" ")[1].strip()
	helpCommand = commandArray[4].split(" ")[1].strip()
	changeCommandShortcut = commandArray[5].split(" ")[1].strip()
	nowCommand = commandArray[6].split(" ")[1].strip()
class bcolors(object):
	#Stores the various colours for output formatting
    HEADER = '\033[95m'
    BLUEDEB = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#I/O formatting start
def inp(): #Takes Input from the user
	s = input('>>>>')
	return s
def pr(s): #Prints to the console
	print(' >>>>',s)
def deb(s): #For debug statments
	print(bcolors.BLUEDEB,'>>>>',s,bcolors.ENDC)#debug statements
def err(s): #For error and warning statments to the user
	print(bcolors.WARNING,">>>>",s,"For assistance type 'help'",bcolors.ENDC)
def sendInfoToUser(s): #Other warnings
	print(bcolors.WARNING,">>>>",s,bcolors.ENDC)
def success(s): #For a positive feedback
	print(bcolors.OKGREEN,">>>>",s,bcolors.ENDC)
#IO formatting end
def checkIfTimingIsFree(start , end): #Checks if we the timing of the new event is free
	with open(tt, "r") as fl:
		arr = fl.readlines()
		for a in arr:
			i = a.split(" ")
			if(len(a) == 0):continue
			s2 = i[1]
			e2 = i[2]
			if((start>=s2 and e2>start) or (s2<end and e2>=end)or(start>=s2 and e2>=end)):
				err("Timings of " + i[0] +" clashes with the inputted timing.")
				err("Delete "+i[0]+" to schedule this event[Y/N]?")
				ch = inp()
				if(ch == 'Y'):
					deleteEvent(i[0],s2)
					return True
				else:
					return False

	return True
def sortTimeTable():
	with open(tt,"r") as fl:
		arr = fl.readlines()
	#Sort the array
	def sortSecond(val):
		return val.split(" ")[1]
	arr.sort(key = sortSecond)
	with open(tt, "w") as fl:
		for a in arr:
			fl.write(a)
def deleteEvent(name, start):
	deleted = False
	with open(tt, "r") as fl:
		arr = fl.readlines()
	with open(tt,"w") as f2:
		for a in arr:
			i = a.split(" ")
			if(not(i[0] == name and i[1] == start)):
				f2.write(a)
			else:
				deleted = True
	if(not deleted):
		err("Event to delete not present in timetable")
	else:
		success("Event deleted")
	sortTimeTable()
def formatHHMM(s):
	if(len(s) == 1):
		s = "0"+s+"00"
	elif(len(s) == 2):
		s = s + "00"
	elif (len(s) == 3):
			s = "0"+s
	return s
def display():
	sortTimeTable()
	with open(tt, "r") as fl:
		f = fl.readlines()
		for i in f:
			success(i)
def helpCommand():
	commandFile = open("commands.txt","r")
	commandArray = commandFile.readlines()
	for i in commandArray:
		sendInfoToUser(i)
	sendInfoToUser("To report a bug contact arhaan.ahmad2003@gmail.com")
def changeCommandShortcut(name, newName):
	if(name == 'help'):
		sendInfoToUser("This event can't be changed")
		return
	done = False
	with open("commands.txt","r") as commandFile:
		commandArray = commandFile.readlines()
	with open("commands.txt","w") as commandFile:
		for a in commandArray:
			if(a.split(" ")[0].strip() == name +":"):
				commandFile.write(a.split(" ")[0].strip()+ " "+ newName + " ")
			elif (a.split(" ")[1].strip() == name):
				commandFile.write(a.split(" ")[0].strip()+ " "+ newName + " ")
			else:
				commandFile.write(a)

			if(a.split(" ")[1].strip() == name or a.split(" ")[0].strip() == name +":"):
				k = -1
				try:
					commandFile.write(a.split(" ")[2].strip())
				except:
					commandFile.write("\n")
				for b in a.split(" "):
					k = k+1
					if(k<3):
						continue
					commandFile.write(" "+b)
				done = True
	if(done):
		success("Command changed successfuly!!!")
	else:
		err("Invalid Input")

def now():
	t= datetime.datetime.now()
	t.strftime("%H%M")
	t = str(t.hour)+str(t.minute)
	success("Present time is "+t)
	sortTimeTable()
	with open(tt, "r") as fl:
		f = fl.readlines()
		found = False
		for i in f:
			starti = i.split(" ")[1].strip()
			endi = i.split(" ")[2].strip()
			if(found):
				success("Next event is "+i.split(" ")[0].strip()+" from "+starti +" to "+endi)
				break
			if(t>=starti and t<=endi):
				success("The event scheduled at this moment is "+i.split(" ")[0].strip())
				success("It will end at "+endi)
				found = True
			elif(t>starti):
				success("No event scheduled at this time")
				success("Next event is "+i.split(" ")[0].strip()+" from "+starti +" to "+endi)
				break
		
		if(not found):
			for i in f:
				success("No event scheduled at this time")
				success("Next event is "+i.split(" ")[0].strip()+" from "+starti +" to "+endi)
				break

	return


def takeCommand():
	comm1 = inp()
	comm = comm1.split(" ")
	c = comm[0]
	if(c== commands.setCommand):
		try:
			name = comm[1]
			start = comm[2]
			end = comm[3]
		except:
			err("Wrong input")
			return
		#Format start correctly HHMM
		start = formatHHMM(start)
		#Format end HHMM
		end = formatHHMM(end)
		#Check if inputs are valid
		if((start>=end)or(start>"2400")or(end>"2400")or(start[2]+start[3]>"59")or(end[2]+end[3]>"59")):
			err("Invalid timing")
			return
		if(not checkIfTimingIsFree(start,end)):
			return 0
		with open(tt,"a") as f:
    			f.write(name+" "+start+" "+end+"\n")
		pr(bcolors.OKGREEN+"Event Set!!"+bcolors.ENDC)
		sortTimeTable()
		return
	elif (c == commands.deleteCommand):
		try:
			deleteEvent(comm[1], formatHHMM(comm[2]))
		except:
			err("Wrong Input")
			return
	elif(c == commands.quitCommand):
		return -1
	elif (c == commands.displayCommand):
		display()
	elif(c == commands.helpCommand):
		helpCommand()
	elif(c == commands.changeCommandShortcut):
		try:
			name = comm[1]
			newName = comm[2]
			changeCommandShortcut(name, newName)
		except:
			err("Wrong Input")
	elif(c == commands.nowCommand):
		now()
	else: err("Wrong Input!!!")
while(takeCommand()!=-1):
	pass
