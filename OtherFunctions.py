#Cleans junk topics
def topicCleaner(topicList):
        topic = []
        for word in topicList:
                if (len(word) >= 3 and word != "quot"):
                        topic.append(word)

                if(len(topic) >= 5):
                        break
        return topic

#Sets up needed list for parsing to find topic occurences.
def parseSetup(rowList, lda, ldaSize):
        descList = []
        for desc in rowList:
                descList.append(desc[0])

        topicList = []
        for i in range(0,ldaSize):
                topicWords = lda.print_topic(i, 20)
                topicWords = topicWords.split('"')
                topic = topicCleaner(topicWords[1::2])
                topicList.append(topic)
        return topicList, descList       
