import random
from random import randint
import sqlite3



playerss=["hat","car","ship"]


class player(object):
    position=0
    money=1500

    buy1=0
    brown=0
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
    properties=brown+blue+pink+orange+red+yellow+green+darkblue+stations+utilities
    mcent=(money/1500)*100
    pcent=(properties/28)*100
    count=0
    brownset=0
    blueset=0

    pinkset=0
    orangeset=0
    redset=0
    yellowset=0
    greenset=0
    darkblueset=0
    stationsset=0
    bancrupcy=False
    condition=False

    def bankrupt(self):
        if money<0:
            self.bancrupcy=True
            for block in blocks:
                if block["owner"]==self.name:
                    block["owner"]=None

    def set(self):
        if self.brown == 2:
            self.brownset=1

        if self.blue == 3:
            self.blueset=1

        if self.pink == 3:
            self.pinkset=1

        if self.orange == 3:
            self.orangeset=1

        if self.red == 3:
            self.redset=1

        if self.yellow == 3:
            self.yellowset=1

        if self.green == 3:
            self.greenset=1

        if self.darkblue == 3:
            self.darkblueset=1

        if self.stations == 4:
            self.stationsset=1



    def __init__(self, name):
        self.name = name
        self.aggression = randint(1,300)
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

            print("go to jail")

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
                    self.brown = int(self.brown) + 1
                    print("donenjkadfkjnsdkjnfkjdsbnkjbgf")

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
                if blocks[self.position]['group']=="utility":
                    self.utilities= self.utilities+1
                if blocks[self.position]['group']=="station":
                    self.stations= self.stations+1





            else:
                print self.aggression
                print("not bought")
                print(float(blocks[self.position]['value']) * self.playerstatus)
                print(blocks[self.position] )








    def propertysum(self):
        self.properties=self.brown+self.blue+self.pink+self.orange+self.red+self.yellow+self.green+self.darkblue+self.stations+self.utilities

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
            self.tradeshortlist()



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

    def tradeshortlist(self):

        for block in blocks:

            self.condition=False
            if block["owner"]!=self.name and block["owner"]!="np" and block["owner"]!=None:
                x= playerss.index(block["owner"])
                #print("player:"+self.name)
                #print ("property held by:"+playerss[x])


                #this first checks wether the property does not belong to a set
                if block["group"]=="brown":
                    if players[x].brown ==2:
                        #print("brown success")
                        players[x].brownset=1
                        condition=True
                if block["group"]=="blue":
                    if players[x].blue==3:
                        #print("blue success")
                        players[x].blueset=1
                        condition=True
                if block["group"]=="pink":
                    if players[x].pink==3:
                        #print("pink success")
                        players[x].pinkset=1
                        condition=True
                if block["group"]=="orange":
                    if players[x].orange==3:
                        #print("orange success")
                        players[x].orangeset=1
                        condition=True
                if block["group"]=="red":
                    if players[x].red==3:
                        #print("red success")
                        players[x].redset=1
                        condition=True
                if block["group"]=="yellow":
                    if players[x].yellow==3:
                        #print("yellow success")
                        players[x].yellowset=1
                        condition=True
                if block["group"]=="green":
                    if players[x].green==3:
                        #print("green success")
                        players[x].greenset=1
                        condition=True
                if block["group"]=="darkblue":
                    if players[x].darkblue==2:
                        #print("darkblue success")
                        players[x].darkblueset=1
                        condition=True
                if block["group"]=="station":
                    if players[x].stations==4:
                        #print("stations success")
                        condition=True

                if block["group"]=="utility":
                    if players[x].utilities==2:
                        #print("stations success")
                        condition=True

                if  self.condition == False:

                    #if it does not then it proceeds to check wether it itself owns 2 properties in that set

                    x= playerss.index(self.name)
                    tradeshortlist(x,1,block)

                    if self.condition==True:
                        #print("triple success")




                        x= playerss.index(block["owner"])

                        if players[x].brown==1:
                            if players[playerss.index(self.name)].brown==1:
                                if blocks[1]["owner"]==self.name:
                                    if blocks[1]["group"] != block["group"]:
                                        blocks[1]["owner"]=players[x].name
                                        print("Trade done")
                                        print("brown to "+    block["group"])
                                        print("To"+ playerss[x] +"from"+self.name)
                                        block["owner"]=self.name
                                        players[x].brown=players[x].brown+1
                                        player.brown=player.brown-1
                                else:
                                    if blocks[1]["owner"]==self.name:
                                        blocks[3]["owner"]=players[x].name
                                        print("Trade done")
                                        print("brown to "+    block["group"])
                                        print("To"+ playerss[x] +"from"+self.name)
                                        block["owner"]=self.name
                                        players[x].brown=players[x].brown+1
                                        player.brown=player.brown-1
                                        player.

                        if players[x].blue==2:
                            if players[playerss.index(self.name)].blue==1:
                                for prop in bluel:
                                    if blocks[prop]["owner"]==self.name:
                                        if blocks[prop]["group"] != block["group"]:
                                            blocks[prop]["owner"]=players[x].name
                                            print("Trade done")
                                            print("blue to "+    block["group"])
                                            print("To"+ playerss[x] +"from"+self.name)
                                            block["owner"]=self.name
                                            players[x].blue=players[x].blue+1
                                            players[x].blueset=1
                                            player.blue=player.blue-1













def tradeshortlist(x,n,block):
#this general function checks the number of properties for a given player in a particular set
    if block["group"]=="brown":
        if players[x].brown ==2-n:
            #print("brown success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="blue":
        if players[x].blue==3-n:
            #print("blue success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="pink":
        if players[x].pink==3-n:
            #rint("pink success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="orange":
        if players[x].orange==3-n:
            #print("orange success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="red":
        if players[x].red==3-n:
            #print("red success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="yellow":
        if players[x].yellow==3-n:
            #print("yellow success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="green":
        if players[x].green==3-n:
            #print("green success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="darkblue":
        if players[x].darkblue==2-n:
            #print("darkblue success1")

            players[x].condition=True
            return players[x].condition
    if block["group"]=="station":
        if players[x].stations==4-n:
            #print("stations success1")
            players[x].condition=True
            return players[x].condition
    if block["group"]=="utility":
        if players[x].utilities==2-n:
            #print("stations success1")
            players[x].condition=True
            return players[x].condition







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

brownl=(1,3)
bluel=(6,8,9)
pinkl=(11,13,14)
orangel=(16,18,19)
redl=(21,23,24)
yellowl=(26,27,29)
greenl=(31,32,34)
darkbluel=(37,39)
sets=()

blockss= ["go","br1","cc1","br2","tax1","station1","b1","chance1","b2","b3","jail","p1","utility1","p2","p3","station2","o1","cc2","o2","o3","free","r1","chance2","r2","r3","station3","y1","y2","utility2","y3",
"gotojail","g1","g2","cc3","g3","station4","chance3","db1","tax2","db2"]

hat= player('hat')
car= player('car')
ship= player('ship')







players=[hat,car,ship]
turn=50
while turn>0:


    for player1 in players:
        player1.turn()


    #print blocks[hat.position]['count']
    turn=turn-1
sumcount=int()
for block in blocks:
    print block
    sumcount= block["count"]+sumcount

print ("total movement")
print sumcount


for player1 in players:
    print int(player1.money)
    print (player1.aggression)
    print "properties:" +str(player1.properties)
    print "sets:"+str(player1.brownset+player1.blueset+player1.pinkset+player1.orangeset+player1.redset+player1.yellowset+player1.greenset+player1.darkblueset)
