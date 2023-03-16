from dashboard import Dashboard_start

#switch window from beginning warnprompt to dashboard while copying host file
def change(newwin):
    from LogicFunctions import copyHosts
    copyHosts()
    newwin.destroy()
    Dashboard_start()