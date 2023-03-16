import datetime
import time
import os
import shutil
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
        f.truncate()
    #truncating of cache content
    with open(currListCacheDir, 'r+') as f:
        f.truncate(0)



def writeToBoolCache():
    global boolValCacheDir
    boolValCacheDir = "./cacheApproach/boolValCache.txt"
    with open(boolValCacheDir, 'w') as f:
        f.write("False")


def checkTime(currTime, doneTime, currList):
    global isExit
    global currListCacheDir
    from ForRootinit import root
    from OngoingBlock import UnblockedMsg
    print(doneTime)

    with open(boolValCacheDir, 'r') as f:
        for line in f:
            isExit = str(line)
    currListCacheDir = "./cacheApproach/currListCache.txt"
    # we have to store current list to a text so that we can pull it any time regardless of var scope.
    with open(currListCacheDir, 'w') as f:
        f.write(" ".join(currList))
    currTime = datetime.datetime.now()

    if isExit == "True":
        print("UNBLOCKED ALL SITES")
        with open(boolValCacheDir, 'r+') as f:
            f.truncate(0)
        root.destroy()
        return
    if currTime < doneTime and isExit != "True":
        print("BLOCK TIME STILL ON.")
        # continue
    else:
        print("UNBLOCKED ALL SITES")
        with open(boolValCacheDir, 'r+') as f:
            f.truncate(0)
        unBlock(currList)
        # with open(currListCacheDir, 'r+') as f:
        #     f.truncate(0)
        UnblockedMsg()
        root.destroy()
        return
    # If you want to update the current time in a loop and still 
    # be able to use a GUI, you can use the after method in Tkinter. 
    # The after method allows you to schedule a function to be executed after a specified number of milliseconds.
    # The update_time function is defined to get the current time using the datetime module and update the text of the label. 
    # The root.after method is used to schedule the update_time function to be executed every 1000 milliseconds (1 second), allowing the GUI to update 
    # the current time in real-time without blocking the GUI. 
    # The root.mainloop method is used to start the Tkinter event loop and keep the GUI running until it is closed by the user.
    root.after(10000, checkTime, currTime, doneTime, currList)
    #this just bruteforcing it :(
    root.withdraw()

def copyHosts(): 
    #path to be checked for copy
    path = 'hostscopy/hostscopy.txt'
    isExist = os.path.exists(path)
    print(isExist)

    #source file of host to be copied from
    src = hostsPath
    dest = path
    if isExist:
        print("Your host copy already exists, you already have a backup.")
    else:
        shutil.copyfile(src,dest)
        print("COPY COPIED")

def killBrowsers():
    browserList = ["chrome.exe", "firefox.exe", "opera.exe", "msedge.exe", "brave.exe"]
    for browser in browserList:
            os.system("taskkill /im " + browser + " /f")
