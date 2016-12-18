def severityOccurrence(bugList):
    countList = [0,0,0,0,0]
    dicKeySevere = {"trivial":0,"minor":1,"normal":2,"major":3,"critical":4}
    
    for bug in bugList:
        #just pulls the value from a dictionary
        countList[dicKeySevere[bug[1]]]+=1 
    return countList
