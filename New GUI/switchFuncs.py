from constants import *
from dashboard import dashboardStart


#switch window from beginning warnprompt to dashboard while copying host file
def changeToDashboard(newwin):
    from logicFunctions import copyHosts
    copyHosts()
    newwin.destroy()
    displayPage(dashboardStart)

#switch from preset/write page to ongoingBlock
def switch(pagename):
    from presetAndWriteFunctions import select
    from ongoingBlock import ongoingBlockStart
    select(pagename)
    # a.destroy()
    # root.destroy()
    displayPage(ongoingBlockStart)