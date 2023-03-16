import datetime
import os
import time
import linecache

# hosts path for windows (uncomment the code according to your system)
hostsPath = "C:\Windows\System32\drivers\etc\hosts"

# #hosts path for linux/mac (uncomment the code according to your system)
# hostspath = "/etc/hosts"

#storing websites to be blocked
webLists = []

#localhost
localRedirect = "127.0.0.1"

#we set unblock time to placeholding(1 year in minutes) value that is so long just so it's viable for the outer "if conditions" to work
#this is just to make the code run long enough to reach the asking of user input for the minutes
unblock_time = datetime.datetime.now() + datetime.timedelta(minutes=525600)

#This is just a variable to make sure that the function of inputting a list again does not go back while waiting for time to unblock
doneInputting = False;

def timeSet():

    global interval
    global start_time
    global unblock_time
        #ask user for time interval in minutes to block the websites 
    while True:
        try:
            interval = float(input("How long are the websites going to be blocked (in minutes): "))
            break
        except ValueError:
            print("Invalid input. Enter a valid time interval in minutes.")

    #initialization of start and end time are done outside of funtion so that their values will not be altered in each sleep iteration
    start_time = datetime.datetime.now()
    unblock_time = start_time + datetime.timedelta(minutes=interval)      

    print("Proceeding will exit all browsers. Unsaved progress will be lost.")
    killDecision = input("Do you wish to proceed or exit browsers manually? (Y/N) ")

    if killDecision.upper() == "Y":
        os.system("taskkill /im firefox.exe /f")
        os.system("taskkill /im chrome.exe /f")
        os.system("taskkill /im opera.exe /f")
        os.system("taskkill /im msedge.exe /f") 
        os.system("taskkill /im brave.exe /f")
    #upon the very moment of killing the browsers, we need a new current time var to be subtracted by the start time var
    #and we need to add it to the unblock time var to make up for the time that was taken while the user was still inputting data
    inputTime = datetime.datetime.now() - start_time
    #we need to update unblock time to make up for the time taken by user while inputting
    unblock_time += inputTime

def inputSites(siteList):
    global toBlock
    global doneInputting
    while True:
        toBlock = input("Type in the website url to block. EX.(www.google.com): ")
        #if there is white space, validate it
        if " " in toBlock:
            print("Please enter a valid input.")
            continue
        #append also a version without "www." and vice versa
        if toBlock != "exit" and "www." in toBlock:
            siteList.append(toBlock)
            siteList.append(toBlock.replace("www.",""))
        elif toBlock != 'exit' and "www." not in toBlock:
            siteList.append(toBlock)
            siteList.append("www." + toBlock)
        else: 
            break

def writeToHost(siteList):
    #opening the file using append + read mode
    with open (hostsPath, 'a+') as f:
        f.seek(0)
        fileContent = f.read()
        #code to avoid duplication
        for web in siteList:
            if web in fileContent:
                print(web + " is already listed.")
                #pass is removed here, tests if naa jd siyay pulos last time
            else:
                f.write("\n")
                f.write(localRedirect + " " + web)

def unBlock(siteList):
    with open (hostsPath, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            #statement to know if there are no words in the line that belong to the weblists, 
            # because if there are none found, the line would be written back to the hostfile, and not removed
            if not any(web in line for web in siteList):
                f.write(line)
        #cuts of all lines that were not written in line 72
        print("/n")
        print(siteList)
        f.truncate()

def webBlock():
        while True:
            try: 
                presetChoice = int(input("Press 1 to create new list. Press 2 to choose presets: "))
                if presetChoice != 1 and presetChoice != 2:
                    print("Please enter a valid input.")
                else: 
                    while True:
                        global webLists
                        global start_time
                        global doneInputting
                        global unblock_time
                        current_time = datetime.datetime.now()
                        if current_time < unblock_time and doneInputting == False and presetChoice == 1:
                            #false isPreset for unblock func to know which list to look at
                            isPreset = False
                            #calling of inputSites func
                            inputSites(webLists)
                            #While True loop for overall --
                            while True:
                                doneInputting = True;
                                print("Blocking sites...")
                                #write to hosts in weblists list
                                writeToHost(webLists)
                            # #this block of code is for the saving of lists          
                                print("WEBLISTS: ", webLists)
                                #dict is used to remove the commas that separates the elements from Weblists
                                #list() is used to turn the separated elements into a list
                                webStore = list(dict.fromkeys(webLists))
                                print("WEBSTORES: ", webStore)
                                #this opens a webstores file to store the inputted websites so that they will be made as a preset.
                                with open ("webstores.txt", "a+") as f:
                                    f.seek(0)
                                    f.writelines(' '.join(webStore))
                                    f.write("\n")
                                    print(f.read())   
                                #calling of function to for timesetting
                                timeSet()  
                                break
                        #block of code for the choice of looking at presets.
                        elif current_time < unblock_time and doneInputting == False and presetChoice == 2:
                            #variable to let unblock func know if "webLists" or "presetLists" is the one to be checked when unblocking
                            isPreset = True    
                            with open ("webstores.txt", "r") as f:
                                # f.seek(0)
                                #validating if txt file for presets is empty or not
                                if os.stat("webstores.txt").st_size == 0:
                                    print("There are no presets yet. Please create one.")
                                    break
                                #this is for displaying the lines and adding a number in them
                                #enumerate is a faster way of having a counter right beside element of an object or list
                                for i, line in enumerate(f):
                                    print(f'{i+1}. {line}'.strip())
                                #for choosing which preset to read
                                while True:
                                    try:
                                        presetNum = int(input("Enter the number of the preset you want to choose: "))
                                        if presetNum > i+1:
                                            print("Your input exceeds the available choices of presets.")
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print("Invalid input.")
                                #imported linecache to get specific line without having for loops
                                presetLine = linecache.getline("webstores.txt", presetNum)
                                #split automatically splits content of presetLine with commas and into a list
                                presetList = presetLine.split()
                                print(presetList)
                                while True: 
                                    try:
                                        presetDecision = int(input("Press 1 to block selected wesbites. Press 2 to add more websites to the presets. Press 3 to delete preset. "))
                                        if presetDecision != 1 and presetDecision != 2 and presetDecision != 3:
                                            print("Please enter a valid input.")
                                        else: 
                                            break
                                    except ValueError:
                                        print("Invalid input.")
                                if presetDecision == 1:
                                    while True:
                                        doneInputting = True;
                                        #automatic write to host with preset list
                                        writeToHost(presetList)
                                        #time setting
                                        timeSet()
                                        break
                                elif presetDecision == 2:
                                    inputSites(presetList)
                                    #While True loop for overall --
                                    while True:
                                        doneInputting = True;
                                        print("Blocking sites...")
                                        writeToHost(presetList)
                                        timeSet()
                                        break
                                elif presetDecision == 3:
                                    # list to store file lines
                                    lines = []
                                    # read file
                                    with open("webstores.txt", 'r') as fp:
                                        # read an store all lines into list
                                        lines = fp.readlines()

                                    # Write file
                                    with open("webstores.txt", 'w') as fp:
                                        # iterate each line
                                        for number, line in enumerate(lines):
                                            # delete line 5 and 8. or pass any Nth line you want to remove
                                            # note list index starts from 0
                                            if number not in [presetNum-1]:
                                                fp.write(line)
                                    break
                        #block of code just for checking if block time is still on
                        elif current_time < unblock_time and doneInputting == True:
                            print("Blocking time is still on. (prints every 10 secs)   ", current_time)
                        elif current_time >= unblock_time and doneInputting == True:
                            #we reset done inputting to false to be able to return to inputting if ever the user wants.
                            doneInputting = False
                            #reset unblock time, webLists, webStores, presetList
                            unblock_time = datetime.datetime.now() + datetime.timedelta(minutes=525600)
                            print("BLOCK TIME PASSED. ALL SITES UNBLOCKED.")
                            if isPreset == True:
                                unBlock(presetList)
                            else:
                                unBlock(webLists)
                            webLists = []
                            webStore = []
                            presetList = []
                            break
                        time.sleep(10)
            except ValueError:
                print("Invalid input. Please enter a number.")



#main function
if __name__ == "__main__":
    webBlock()
    # print("start time: ", start_time)
    # print("end time: ", unblock_time)
        
