from datetime import datetime
from itertools import combinations

class TopicSeverityOverTime:
    def __init__(self, topicList, rowList, topicNum):
        self.topicList = topicList
        self.rowList = rowList
        self.userTopic = topicList[topicNum]

    
    def findOldest(self):
        oldest = (self.rowList[0][2].month, self.rowList[0][2].year)
        for row in self.rowList:
            temp = (row[2].month, row[2].year)
            if (temp[1] < oldest[1] or (temp[1] == oldest[1] and temp[0] <= oldest[0])):
                oldest = temp
        self.oldest = oldest

    def findNewest(self):
        newest = (self.rowList[0][2].month, self.rowList[0][2].year)
        for row in self.rowList:
            temp = (row[2].month, row[2].year)
            if (temp[1] > newest[1] or(temp[1] == newest[1] and temp[0] >= newest[0])):
                newest = temp
        self.newest = newest

    def getUserTopic(self):
        return self.userTopic

    
    def generateList(self):
        self.findOldest()
        self.findNewest()
        monthList =[]
        date = self.oldest
        con = True
        while con:
            if (date[1] < self.newest[1] or(date[1] == self.newest[1] and date[0] <= self.newest[0])):
                monthList.append([date,[0,0,0,0,0]])
            else:
                con = False
                break

            date = (date[0]+1, date[1])
            if (date[0] >= 13):
                date = (1, date[1] + 1)

        self.monthList = monthList


    def counting(self):
        
        self.generateList()
        topicOccDates = []
        dicKeySevere = {"trivial":0,"minor":1,"normal":2,"major":3,"critical":4}
        j = 0
        combos = []
        for combo in combinations(self.userTopic,2):
                combos.append(combo)
        for row in self.rowList:
            for i in combos:
                if i[0] in row[0] and i[1] in row[0]:
                    temp = (row[2].month,row[2].year)
                    i = 0
                    for month in self.monthList:
                        if (temp == month[0]):
                            thing = self.rowList[j][1]
                            self.monthList[i][1][dicKeySevere[self.rowList[j][1]]] +=1
                            break
                        i+=1
            j+=1
        topicOccDates.append(self.monthList)

        self.topicOccDates = topicOccDates

    def getMonths(self):
        mList = []
        for month in self.monthList:
            m = str(month[0][0])
            y = str(month[0][1])
            date = (m + "/" + y)
            mList.append(date)
        return mList
    
    def getTopicOccurrences(self):
        occurrences = []
        for x in self.topicOccDates:
            temp = []
            for i in x:
                temp.append(i[1])
            occurrences.append(temp)
        return occurrences

