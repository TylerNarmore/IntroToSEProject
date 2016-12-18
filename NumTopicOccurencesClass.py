

class TopicOccurrence:
    def __init__(self, topicList, descList):
        self.topicList = topicList
        self.descList = descList
        self.occurrences = []

    def searchList(self):
        topicNum = 0
        testNum = 0
        for topic in self.topicList:
            self.occurrences.append(0)
            for desc in self.descList:
                if any(topicWord in desc for topicWord in topic):
                    self.occurrences[topicNum] += 1
                testNum+=1
            topicNum += 1

    def getOccurrences(self):
        return self.occurrences
