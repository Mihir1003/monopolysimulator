import random
from random import randint
import sqlite3

dog = 0
barrow = 0
cannon = 0
boot = 0
ship = 0
hat = 0
iron = 0
bell = 0
horse = 0
car = 0


go=      {'count':0, 'position':0,}
br1=     {'count':0, 'position':1,'owner':None}
cc1=     {'count':0, 'position':2}
br2=     {'count':0, 'position':3,'owner':None}
tax1=    {'count':0, 'position':4}
station1={'count':0, 'position':5,'owner':None}
b1=      {'count':0, 'position':6,'owner':None}
chance1= {'count':0, 'position':7}
b2=      {'count':0, 'position':8,'owner':None}
b3=      {'count':0, 'position':9,'owner':None}
jail=    {'count':0, 'position':10}
p1=      {'count':0, 'position':11,'owner':None}
utility1={'count':0, 'position':12,'owner':None}
p2=      {'count':0, 'position':13,'owner':None}
p3=      {'count':0, 'position':14,'owner':None}
station2={'count':0, 'position':15,'owner':None}
o1=      {'count':0, 'position':16,'owner':None}
cc2=     {'count':0, 'position':17}
o2=      {'count':0, 'position':18,'owner':None}
o3=      {'count':0, 'position':19,'owner':None}
free=    {'count':0, 'position':20}
r1=      {'count':0, 'position':21,'owner':None}
chance2= {'count':0, 'position':22}
r2=      {'count':0, 'position':23,'owner':None}
r3=      {'count':0, 'position':24,'owner':None}
station3={'count':0, 'position':25,'owner':None}
y1=      {'count':0, 'position':26,'owner':None}
y2=      {'count':0, 'position':27,'owner':None}
utility2={'count':0, 'position':28,'owner':None}
y3=      {'count':0, 'position':29,'owner':None}
gotojail={'count':0, 'position':30}
g1=      {'count':0, 'position':31,'owner':None}
g2=      {'count':0, 'position':32,'owner':None}
cc3=     {'count':0, 'position':33}
g3=      {'count':0, 'position':34,'owner':None}
station4={'count':0, 'position':35,'owner':None}
chance3= {'count':0, 'position':36}
db1=     {'count':0, 'position':37,'owner':None}
tax2=    {'count':0, 'position':38}
db2=     {'count':0, 'position':39,'owner':None}

blocks= [go,br1,cc1,br2,tax1,station1,b1,chance1,b2,b3,jail,p1,utility1,p2,p3,station2,o1,cc2,o2,o3,free,r1,chance2,r2,r3,station3,y1,y2,utility2,y3,
gotojail,g1,g2,cc3,g3,station4,chance3,db1,tax2,db2]

blockss= ["go","br1","cc1","br2","tax1","station1","b1","chance1","b2","b3","jail","p1","utility1","p2","p3","station2","o1","cc2","o2","o3","free","r1","chance2","r2","r3","station3","y1","y2","utility2","y3",
"gotojail","g1","g2","cc3","g3","station4","chance3","db1","tax2","db2"]



def rolldie(var):
    var = var + randint(2,12)
    return var

def check(var):
    if var == 30:
        var=10
        return var

    elif var > 39:
        var= var - 40
        return var
    else: return var
def chance(var):
    if var==7 or var==22 or var==33:

        chancelist=[0,10,11,"spaces",15,25,39,None,None,None,None,None,None,None,None,None]
        ccrandom= randint(0,15)
        if chancelist[ccrandom] is None:
            return var
        elif chancelist[ccrandom] =="spaces" :
            var = var - 3
            return var
        else:
            var= chancelist[ccrandom]
            return var
    else: return var
def cc(var):
        if var==2 or var==17 or var==36:
            cclist=[1,0,10,None,None,None,None,None,None,None,None,None,None,None,None,None]
            ccrandom= randint(0,15)
            if cclist[ccrandom] is None:
                return var
            else:
                var= cclist[ccrandom]
                return var
        else: return var





turn=1000

while turn>0:
    hat = rolldie(hat)

    hat= cc(hat)
    hat= chance(hat)
    hat= check(hat)
    blocks[hat]['count']= blocks[hat]['count'] + 1
    
    turn=turn-1
for block in blocks:
    print block

brown=float((br1['count'] + br2['count'])/2)
blue=float((b1['count'] + b2['count'] + b3['count'])/3)
pink=float((p1['count'] + p2['count'] + p3['count'])/3)
orange=float((o1['count'] + o2['count'] + o3['count'])/3)
red=float((r1['count'] + r2['count'] + r3['count'])/3)
yellow=float((y1['count'] + y2['count'] + y3['count'])/3)
green=float((g1['count'] + g2['count'] + g3['count'])/3)
darkblue=float((db1['count'] + db2['count'])/2)
utilities=float((utility1['count'] + utility2['count'])/2)
stations=float((station1['count'] + station2['count']+station3['count'] + station4['count'])/4)











print brown,blue,pink,orange,red,yellow,green,darkblue,utilities,stations




conn= sqlite3.connect('monopoly.sqlite')
cur=conn.cursor()

cur.execute('''

CREATE TABLE IF NOT EXISTS Colorcounts(
brown INTEGER,
blue INTEGER,
pink INTEGER,
orange INTEGER,
red INTEGER,
yellow INTEGER,
green INTEGER,
darkblue INTEGER,

utilities INTEGER,
stations INTEGER
)''')

cur.execute(''' INSERT INTO Colorcounts(brown,blue,pink,orange,red,yellow,green,darkblue,utilities,stations) VALUES (?,?,?,?,?,?,?,?,?,?) ''',(brown,blue,pink,orange,red,yellow,green,darkblue,utilities,stations))

conn.commit()
