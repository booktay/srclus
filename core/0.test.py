from srcluslib.utility.io import io
from srcluslib.model.preprocess import preprocess

preprocess = preprocess()
io = io()
url = "https://ptdev03.mikelab.net/kratoo/"+"37716032"
data = io.requestURL(url=url, security=False)
if data['found'] : 
    title = data['_source']['title']
    desc = data['_source']['desc']
    word = title + " " + desc
    # word = word.encode('ascii', "backslashreplace")
    procdata = preprocess.filterOnlyTHENG(data=word)
    procdata = preprocess.removeSpecialcharacter(data=procdata)
    io.print(procdata)
else : io.print(f'[Error] No data at %s' % url)