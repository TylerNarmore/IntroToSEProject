import plotly.plotly as py
import plotly.graph_objs as go
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot as py
from plotly.graph_objs import Bar, Scatter, Figure, Layout

from SeverityCount import severityOccurrence

def occurrenceBarChart(myFile, topicList, occurrences):
        layout = dict(title = 'Topic Occurences', #8th attribute in topic_name is the graph title
        xaxis = dict(title = 'Topics'), #9th attribute in topic_name is the graph title
        yaxis = dict(title = 'Amount of Occurances'), #10th attribute in topic_name is the graph title
        )
        xAxis = []
        for topic in topicList:
                xAxis.append( str(topic[0]+', '+topic[1]+', '+topic[2]))
        data = [go.Bar(x=xAxis,y=occurrences.getOccurrences())]

        fig = dict(data=data, layout=layout)
        plot(fig, data, filename = "topic_occurrence.html")

def severityBarChart(myFile):
        sev = ['Trivial','Minor','Normal','Major','Critical']
        sevCount = severityOccurrence(myFile.getBugs())

        layout = dict(title = 'Bugs Severity Occurences', #8th attribute in topic_name is the graph title
        xaxis = dict(title = 'Bugs Severity'), #9th attribute in topic_name is the graph title
        yaxis = dict(title = 'Amount of Occurances'), #10th attribute in topic_name is the graph title
        )  

        data = [go.Bar(x=sev,y=sevCount)]

        fig = dict(data=data, layout=layout)
        
        #Graphing severity bar chart
        plot(fig, data, filename = "severity_occurrence.html")
        
def enhanOverTime(months, topicOcc, topicList):
    data = []
    count = 0
    
    for topic in topicList:
        data.append(go.Scatter(
            x = months,
            y = topicOcc[count],
            name = str(topic[0]+', '+topic[1]+', '+topic[2])
        ))
        count+=1

    # Edit the layout
    layout = dict(title = 'Enhancements Over Time', #8th attribute in topic_name is the graph title
    xaxis = dict(title = 'Dates (Month/ Year)'), #9th attribute in topic_name is the graph title
    yaxis = dict(title = 'Amount of Occurances'), #10th attribute in topic_name is the graph title
    )             
                       
    fig = dict(data=data, layout=layout)
    plot(fig, go.Data(data), filename = 'enhanOverTime.html')


def bugsOverTime(months, sevOcc, topic):
    occurrences = [[],[],[],[],[]]
    count = 0
    data = []
    for sevMonth in sevOcc[0]:
        occurrences[0].append(sevMonth[0])
        occurrences[1].append(sevMonth[1])
        occurrences[2].append(sevMonth[2])
        occurrences[3].append(sevMonth[3])
        occurrences[4].append(sevMonth[4])
    for severity in ["trivial", "minor", "normal" , "major", "critical"]:
        
        data.append(go.Scatter(
            x = months,
            y = occurrences[count],
            name = severity
        ))
        count += 1

    # Edit the layout
    layout = dict(title = str(topic[0]+"'s Severity Over Time"), #8th attribute in topic_name is the graph title
    xaxis = dict(title = 'Dates (Month/ Year)'), #9th attribute in topic_name is the graph title
    yaxis = dict(title = 'Amount of Occurances'), #10th attribute in topic_name is the graph title
    )             
                       
    fig = dict(data=data, layout=layout)
    plot(fig, go.Data(data), filename = 'bugsOverTime.html')
