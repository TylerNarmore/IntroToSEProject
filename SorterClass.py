import openpyxl
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


class ExcelFileReader:
    def __init__(self, excelFile):
        self.excelFile = excelFile
        self.bugs = []
        self.enhancements = []

    def openFile(self):
        #Opens the excel document
        self.wb = openpyxl.load_workbook(self.excelFile, read_only=True)
        self.sheet = self.wb.active

    def sort(self):
        rowcount = self.sheet.max_row
        i = 0
        #Reads through the excel document
        for row in self.sheet.rows:
            rowVals = []
            i+=1
            temp = []
            for cell in row:
                rowVals.append(cell.value)

            if (rowVals[2] in ['trivial','minor','normal','major','critical']):
                #Checks if the description cell is empty
                if(type(rowVals[1]) == str):
                    #Writes the description it to the bugs.txt file
                    self.bugs.append([rowVals[1],rowVals[2],rowVals[3]])
                    
                #if it is empty prints the line number of it
                else:
                    pass

            elif (rowVals[2]  == 'enhancement'):
                #Checks if the description cell is empty
                if(type(rowVals[1]) == str):
                    #Writes the description it to the enhancements.txt file
                    self.enhancements.append([rowVals[1],rowVals[2],rowVals[3]])
                #if it is empty prints the line number of it
                else:
                    pass

    def getEnhancements(self):
        return self.enhancements

    def getBugs(self):
        return self.bugs

    def closeFile(self):
        self.wb.save(self.excelFile)


