import datetime
import os
import time
# hosts path for windows (uncomment the code according to your system)
hostsPath = "C:\Windows\System32\drivers\etc\hosts"

# #hosts path for linux/mac (uncomment the code according to your system)
# hostspath = "/etc/hosts"

#localhost
localRedirect = "127.0.0.1"

#list for websites
webLists = [];

#ask user for time interval in minutes to block the websites 
while True:
    try:
        interval = int(input("How long are the websites going to be blocked (in minutes): "))
        break
    except ValueError:
        print("Invalid input. Enter a valid time interval in minutes.")

#initialization of start and end time are done outside of funtion so that their values will not be altered in each sleep iteration
start_time = datetime.datetime.now()
unblock_time = start_time + datetime.timedelta(minutes=interval)
#current time initialization just for global purpose
current_time = ""

#This is just a variable to make sure that the function of inputting a list again does not go back while waiting for time to unblock
doneInputting = False;

def webBlock():

        while True:
            global doneInputting
            global unblock_time
            current_time = datetime.datetime.now()
            if current_time < unblock_time and doneInputting == False:
                pass
            #ask for input before the while loop occurs
                while True:
                    toBlock = input("Type in the website url to block. EX.(www.google.com): ")

                    #append also a version without "www." and vice versa
                    if toBlock != "exit" and "www." in toBlock:
                        webLists.append(toBlock)
                        webLists.append(toBlock.replace("www.",""))
                    elif toBlock != 'exit' and "www." not in toBlock:
                        webLists.append(toBlock)
                        webLists.append("www." + toBlock)
                    else: 
                        break

                #While True loop for overall --
                while True:
                    doneInputting = True;
                    print("block sites")
                    #opening the file using append + read mode
                    with open (hostsPath, 'a+') as f:
                        f.seek(0)
                        fileContent = f.read()
                        #code to avoid duplication
                        for web in webLists:
                            if web in fileContent:
                                print(web + " is already listed.")
                                #pass is removed here, tests if naa jd siyay pulos last time
                            else:
                                f.write("\n")
                                f.write(localRedirect + " " + web)

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

                    print("Proceeding will exit all browsers. Unsaved progress will be lost.")
                    killDecision = input("Do you wish to proceed or exit browsers manually? (Y/N) ")

                    if killDecision.upper() == "Y":
                        os.system("taskkill /im firefox.exe /f")
                        os.system("taskkill /im chrome.exe /f")
                        os.system("taskkill /im opera.exe /f")
                        os.system("taskkill /im msedge.exe /f") 
                    #upon the very moment of killing the browsers, we need a new current time var to be subtracted by the start time var
                    #and we need to add it to the unblock time var to make up for the time that was taken while the user was still inputting data
                    inputTime = datetime.datetime.now() - start_time
                    #we need to update unblock time to make up for the time taken by user while inputting
                    unblock_time += inputTime
                    break

                
            elif current_time < unblock_time and doneInputting == True:
                print("Blocking time is still on. (prints every 10 secs)   ", current_time)
            elif current_time >= unblock_time and doneInputting == True:
                print("BLOCK TIME PASSED. ALL SITES UNBLOCKED.")
                with open (hostsPath, 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        #statement to know if there are no words in the line that belong to the weblists, 
                        # because if there are none found, the line would be written back to the hostfile, and not removed
                        if not any(web in line for web in webLists):
                            f.write(line)
                    #cuts of all lines that were not written in line 72
                    f.truncate()   
                break
            time.sleep(10)

#main function
if __name__ == "__main__":
    webBlock()
    print("start time: ", start_time)
    print("end time: ", unblock_time)
        
