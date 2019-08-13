import random
from random import randint
import sqlite3

count=0
while count<200:
    playerss=["hat","car","ship"]


    class player(object):
        position=0
        money=1500

        buy1=0
        brown1=0
        blue=0
        pink=0
        orange=0
        red=0
        yellow=0
        green=0
        darkblue=0
        stations=0
        utilities=0
        dice1=0
        dice2=0
        roll=0
        properties=brown1+blue+pink+orange+red+yellow+green+darkblue+stations+utilities
        mcent=(money/1500)*100
        pcent=(properties/28)*100
        count=0
        brownset=False
        blueset=0

        pinkset=0
        orangeset=0
        redset=0
        yellowset=0
        greenset=0
        darkblueset=0
        stationsset=0
        bancrupcy=False

        def bankrupt(self):
            if money<0:
                self.bancrupcy=True
                for block in blocks:
                    if block["owner"]==self.name:
                        block["owner"]=None

        def set(self):
            if self.brown1 == 2:
                brownset=True
                #print("ahoy")

            if self.blue == 3:
                blueset=True
                #print("ahoy")
            if self.pink == 3:
                pinkset=True
                #print("ahoy")
            if self.orange == 3:
                orangeset=True
                #print("ahoy")
            if self.red == 3:
                redset=True
                #print("ahoy")
            if self.yellow == 3:
                yellowset=True
                #print("ahoy")
            if self.green == 3:
                greenset=True
                #print("ahoy")

            if self.darkblue == 3:
                darkblueset=True
                #print("ahoy")
            if self.stations == 4:
                stationsset=True
                #print("ahoy")



        def __init__(self, name):
            self.name = name
            self.aggression = randint(1,200)
        def ps(self):
            if self.pcent==0:
                self.pcent=1
            if self.mcent==0:
                self.mcent=1
            self.playerstatus= float(self.mcent/self.pcent)
        def rolldie(self):

            roll=0
            count=0
            while True:

                dice1=randint(1,6)
                dice2=randint(1,6)
                if dice1 == dice2:
                    roll= roll+dice1+dice2

                    count = count+1
                    if count>=3:
                        continue
                        self.position=10
                        print("jailed")
                    continue
                else:
                    roll= dice1+dice2
                    break
            self.position = self.position + roll

        def check(self):
            if self.position == 30:
                self.position=10
                self.money=self.money - 50


            elif self.position > 39:
                self.position= self.position - 40
                self.money=self.money + 200

        def chance(self):
            if self.position==7 or self.position==22 or self.position==33:

                chancelist=[0,10,11,"spaces",15,25,39,None,None,None,None,None,None,None,None,None]
                ccrandom= randint(0,15)
                if chancelist[ccrandom] is None:
                    self.position=self.position
                elif chancelist[ccrandom] =="spaces" :
                    self.position = self.position - 3

                else:
                    self.position= chancelist[ccrandom]


        def cc(self):
                if self.position==2 or self.position==17 or self.position==36:
                    cclist=[1,0,10,None,None,None,None,None,None,None,None,None,None,None,None,None]
                    ccrandom= randint(0,15)
                    if cclist[ccrandom] is None:
                        self.position=self.position
                    else:
                        self.position = cclist[ccrandom]
        def buy(self):
            self.buy1=self.buy1+1
            #print(self.buy1)
            self.ps()
            if blocks[self.position]['owner'] is None and blocks[self.position]['owner'] != 'np':
                if float(blocks[self.position]['value']) * self.playerstatus + self.aggression >= blocks[self.position]['cp']:

                    self.money=self.money- blocks[self.position]['cp']

                    blocks[self.position]['owner']=self.name

                    if blocks[self.position]['group']=="brown":
                        self.brown1 = int(self.brown1) + 1
                        print "done"
                    if blocks[self.position]['group']=="blue":
                        self.blue= self.blue+1
                    if blocks[self.position]['group']=="pink":
                        self.pink= self.pink+1
                    if blocks[self.position]['group']=="orange":
                        self.orange= self.orange+1
                    if blocks[self.position]['group']=="red":
                        self.red= self.red+1
                    if blocks[self.position]['group']=="yellow":
                        self.yellow= self.yellow+1
                    if blocks[self.position]['group']=="green":
                        self.green= self.green+1
                    if blocks[self.position]['group']=="darkblue":
                        self.darkblue= self.darkblue+1




                #else:
                    #print self.aggression
                    #print("not bought")
                    #print(float(blocks[self.position]['value']) * self.playerstatus)
                    #print(blocks[self.position] )








        def propertysum(self):
            self.properties=self.brown1+self.blue+self.pink+self.orange+self.red+self.yellow+self.green+self.darkblue+self.stations+self.utilities

        def turn(self):
            if self.bancrupcy==False:
                self.propertysum()
                self.rolldie()
                self.cc()
                self.chance()
                self.check()
                self.rent()
                self.buy()
                self.set()



            blocks[self.position]['count']= blocks[self.position]['count'] + 1
        def rent(self):
            if blocks[self.position]['owner'] is not None and blocks[self.position]['owner'] != 'np':
                if blocks[self.position]['rent']=="special":
                    rent= self.roll*4
                    players[playerss.index(blocks[self.position]['owner'])].money=players[playerss.index(blocks[self.position]['owner'])].money + rent
                    self.money= self.money - rent
                else:
                    #print (players[playerss.index(blocks[self.position]['owner'])].money)
                    players[playerss.index(blocks[self.position]['owner'])].money=players[playerss.index(blocks[self.position]['owner'])].money + blocks[self.position]['rent']
                    self.money= self.money - blocks[self.position]['rent']
                    #print("after pay")
                    #print ( players[playerss.index(blocks[self.position]['owner'])].money)




    go=      {'count':0, 'position':0,'owner':'np'}
    br1=     {'count':0, 'position':1,'owner':None,'value':0.7,'cp':60,'rent':2,'group':'brown'}
    cc1=     {'count':0, 'position':2,'owner':'np'}
    br2=     {'count':0, 'position':3,'owner':None,'value':1.4,'cp':60,'rent':4,'group':'brown'}
    tax1=    {'count':0, 'position':4,'owner':'np'}
    station1={'count':0, 'position':5,'owner':None,'value':3.125,'cp':200,'rent':25,'group':'station'}

    b1=      {'count':0, 'position':6,'owner':None,'value':1.2,'cp':100,'rent':6,'group':'blue'}
    chance1= {'count':0, 'position':7,'owner':'np'}
    b2=      {'count':0, 'position':8,'owner':None,'value':1.2,'cp':100,'rent':6,'group':'blue'}
    b3=      {'count':0, 'position':9,'owner':None,'value':1.3,'cp':120,'rent':8,'group':'blue'}
    jail=    {'count':0, 'position':10,'owner':'np'}
    p1=      {'count':0, 'position':11,'owner':None,'value':2,'cp':140,'rent':10,'group':'pink'}
    utility1={'count':0, 'position':12,'owner':None,'value':2,'cp':150,'rent':"special",'group':'utility'}
    p2=      {'count':0, 'position':13,'owner':None,'value':4.85,'cp':140,'rent':10,'group':'pink'}
    p3=      {'count':0, 'position':14,'owner':None,'value':2.1,'cp':160,'rent':12,'group':'pink'}
    station2={'count':0, 'position':15,'owner':None,'value':3.125,'cp':200,'rent':25,'group':'station'}
    o1=      {'count':0, 'position':16,'owner':None,'value':2.17,'cp':180,'rent':14,'group':'orange'}
    cc2=     {'count':0, 'position':17,'owner':'np'}
    o2=      {'count':0, 'position':18,'owner':None,'value':2.17,'cp':180,'rent':14,'group':'orange'}
    o3=      {'count':0, 'position':19,'owner':None,'value':2.24,'cp':200,'rent':16,'group':'orange'}
    free=    {'count':0, 'position':20,'owner':'np'}
    r1=      {'count':0, 'position':21,'owner':None,'value':2.12,'cp':220,'rent':18,'group':'red'}
    chance2= {'count':0, 'position':22,'owner':'np'}
    r2=      {'count':0, 'position':23,'owner':None,'value':2.12,'cp':220,'rent':18,'group':'red'}
    r3=      {'count':0, 'position':24,'owner':None,'value':2.16,'cp':240,'rent':20,'group':'red'}
    station3={'count':0, 'position':25,'owner':None,'value':3.125,'cp':200,'rent':25,'group':'station'}
    y1=      {'count':0, 'position':26,'owner':None,'value':2.65,'cp':260,'rent':22,'group':'yellow'}
    y2=      {'count':0, 'position':27,'owner':None,'value':2.65,'cp':260,'rent':22,'group':'yellow'}
    utility2={'count':0, 'position':28,'owner':None,'value':4.85,'cp':150,'rent':"special",'group':'utility'}
    y3=      {'count':0, 'position':29,'owner':None,'value':2.48,'cp':280,'rent':24,'group':'yellow'}
    gotojail={'count':0, 'position':30,'owner':'np'}
    g1=      {'count':0, 'position':31,'owner':None,'value':1.9,'cp':300,'rent':26,'group':'green'}
    g2=      {'count':0, 'position':32,'owner':None,'value':1.9,'cp':300,'rent':26,'group':'green'}
    cc3=     {'count':0, 'position':33,'owner':'np'}
    g3=      {'count':0, 'position':34,'owner':None,'value':2.01,'cp':320,'rent':28,'group':'green'}
    station4={'count':0, 'position':35,'owner':None,'value':3.125,'cp':200,'rent':25,'group':'station'}
    chance3= {'count':0, 'position':36,'owner':'np'}
    db1=     {'count':0, 'position':37,'owner':None,'value':2.5,'cp':350,'rent':35,'group':'darkblue'}
    tax2=    {'count':0, 'position':38,'owner':'np'}
    db2=     {'count':0, 'position':39,'owner':None,'value':2.5,'cp':400,'rent':50,'group':'darkblue'}

    blocks= [go,br1,cc1,br2,tax1,station1,b1,chance1,b2,b3,jail,p1,utility1,p2,p3,station2,o1,cc2,o2,o3,free,r1,chance2,r2,r3,station3,y1,y2,utility2,y3,
    gotojail,g1,g2,cc3,g3,station4,chance3,db1,tax2,db2]

    blockss= ["go","br1","cc1","br2","tax1","station1","b1","chance1","b2","b3","jail","p1","utility1","p2","p3","station2","o1","cc2","o2","o3","free","r1","chance2","r2","r3","station3","y1","y2","utility2","y3",
    "gotojail","g1","g2","cc3","g3","station4","chance3","db1","tax2","db2"]

    hat= player('hat')
    car= player('car')
    ship= player('ship')







    players=[hat,car,ship]
    turn=100

    while turn>0:


        for player1 in players:
            player1.turn()
        turn=turn-1
    conn= sqlite3.connect('monopoly3.sqlite')
    cur=conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Aggression(
    aggression INTEGER,
    money INTEGER,
    properties INTEGER

      )''')

    cur.execute(''' INSERT INTO aggression(aggression,money,properties) VALUES (?,?,?) ''' ,(hat.aggression,hat.money,hat.properties))

    conn.commit()
    count=count+1
