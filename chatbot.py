import sqlite3
import pyttsx
engine=pyttsx.init()
conn = sqlite3.connect('chatdata2.db')
c=conn.cursor()
print("connceted")
voices = engine.getProperty('voices')
rep='reply'
que='query'
while True:
    engine.setProperty('voice' ,voices[1].id)
    
    request=(input('You: ')).lower()
    c.execute("select reply from parent_reply2 where query='{q}'".format(r=rep,qu=que,q=request))
    jo = c.fetchone()
    if jo != None:
        print(jo[0])
      #  engine.say(jo[0])
      #  engine.runAndWait()
    else:
        
        ans=input('I dont know the answer , so please provide the answer of this query: ')
        
        conn.execute("insert into parent_reply2  values(? , ?)",(request,ans))
        conn.commit()
       
