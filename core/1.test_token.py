from srcluslib.utility.io import io
from srcluslib.model.preprocess import preprocess
from srcluslib.model.tokenize import tokenize

def preprocessdata(word=""):
    procdata = preprocess.replaceURL(data=word)
    procdata = preprocess.filterOnlyTHENG(data=procdata)
    procdata = preprocess.removeSpecialcharacter(data=procdata)
    procdata = tokenize(data=str(procdata).lower()).run()
    procdata = preprocess.removeStopword(procdata)
    return procdata

preprocess = preprocess()
io = io()
url = "https://ptdev03.mikelab.net/kratoo/"+"38047105"
data = io.requestURL(url=url, security=False)
if data and data['found'] : 
    word = data['_source']['title'] + " " + data['_source']['desc']
    procdata = preprocessdata(word=word)
    # io.print(procdata)
else : io.print(f'[Error] No data at %s' % url)