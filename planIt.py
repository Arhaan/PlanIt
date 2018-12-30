data = "usrData.txt"
tt = "timeTable.txt"
commandFile = open("commands.txt","r")
commandArray = commandFile.readlines()

class commands:
	
	setCommand = commandArray[0].split(" ")[1].strip()
	quitCommand = commandArray[1].split(" ")[1].strip()
	deleteCommand = commandArray[2].split(" ")[1].strip()
	displayCommand = commandArray[3].split(" ")[1].strip()
	helpCommand = commandArray[4].split(" ")[1].strip()
	changeCommand = commandArray[5].split(" ")[1].strip()
class bcolors:
    HEADER = '\033[95m'
    BLUEDEB = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def inp():
	s = input(">>>>")
	return s
def pr(s):
	print(">>>>",s)
def deb(s):
	print(bcolors.BLUEDEB,">>>>",s,bcolors.ENDC)#debug statements
	pass
def err(s):
	print(bcolors.WARNING,">>>>",s,"For assistance type 'help'",bcolors.ENDC)
def sendInfoToUser(s):
	print(bcolors.WARNING,">>>>",s,bcolors.ENDC)
def success(s):
	print(bcolors.OKGREEN,">>>>"+s+bcolors.ENDC)
def checkIfTimingIsFree(start , end):
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
def formatHHMM(s):
	if(len(s) == 1):
		s = "0"+s+"00"
	elif(len(s) == 2):
		s = s + "00"
	elif (len(s) == 3):
			s = "0"+s
	return s
def display():
	with open(tt, "r") as fl:
		f = fl.readlines()
		for i in f:
			pr(i)
def help():
	commandFile = open("commands.txt","r")
	commandArray = commandFile.readlines()
	for i in commandArray:
		sendInfoToUser(i)
def changeCommand(name, newName):
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

				done= True
			elif (a.split(" ")[1].strip() == name ):
				commandFile.write(a.split(" ")[0].strip()+ " "+ newName + " ")
				try:
					commandFile.write(a.split(" ")[2].strip())
				except:
					commandFile.write("\n")
				for b in a.split(" "):
					k = k+1
					if(k<3):
						continue
					commandFile.write(" "+b)
			else:
				commandFile.write(a)
	if(done):
		success("Event chnaged successfuly!!!")
	else:
		err("Invalid Input")
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
		help()
	elif(c == commands.changeCommand):
		try:
			name = comm[1]
			newName = comm[2] 
			changeCommand(name, newName)
		except:
			err("Wrong Input")
	else: err("Wrong Input!!!")
while(takeCommand()!=-1):
	pass
	