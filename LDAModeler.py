from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


class LDAModeler:

    def __init__(self):
        self.ldaModel = None

    def loadTopicList(self, topicList):
        self.topicList = topicList

    def loadModel(self, ldaFile):
        self.ldaModel = gensim.models.ldamodel.LdaModel.load(ldaFile)

    def modelLDA(self, numTopics):
        tokenizer = RegexpTokenizer(r'\w+')
        # create English stop words list
        en_stop = get_stop_words('en')
        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()
        # list for tokenized documents in loop
        texts = []
        # loop through document list
        for x in self.topicList:
            try:
                i = x[0]
                # clean and tokenize document string
                raw = i.lower()
                tokens = tokenizer.tokenize(raw)
                # remove stop words from tokens
                stopped_tokens = [i for i in tokens if not i in en_stop]
                # stem tokens
                stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
                # add tokens to list
                texts.append(stemmed_tokens)
            except:
                pass
        # turn our tokenized documents into a id <-> term dictionary
        dictionary = corpora.Dictionary(texts)
        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(text) for text in texts]
        # generate LDA model
        self.ldaModel = gensim.models.ldamodel.LdaModel(corpus, numTopics, id2word = dictionary, passes=20)

        return self.ldaModel
    
    def genLDAByDate(self, numTopics, startDate, endDate=None):
        tempList = []
        for i in self.topicList:
            if (endDate == None):
                if( i[2] >= startDate):
                    tempList.append(i)


        dateTopics = LDAModeler()
        dateTopics.loadTopicList(tempList)
        dateTopics.modelLDA(numTopics)
        return dateTopics.ldaModel
        
    def getModel(self):
        return [self.ldaModel, self.topTopics]

    def saveModel(self, fileName):
        print(fileName)
        self.ldaModel.save(fileName)



    
     
