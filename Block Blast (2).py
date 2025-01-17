#Block Blast
from pygame import *
from random import*
font.init()
init()
width,height=1300,800
BLACK=(0,0,0)
WHITE=(255,255,255)
GRIDBLUE=(37,47,96)
LINEBLUE=(23,35,77)
BGBLUE=(53,72,131)
ELLOW=(255,192,46)
screen=display.set_mode((width,height))
myClock=time.Clock()
running=True
#text
arielbig=font.SysFont("Ariel",60)
arielsmall=font.SysFont("Ariel",40)
arielsettings=font.SysFont("Ariel",80)
infotitle=font.SysFont("Ariel",100)
info=font.SysFont("Ariel",40)
Font=font.SysFont("Arial Black",100) #loading font
smallFont=font.SysFont("Arial Black",20)

#variables
currentscore=64
highscore=6724
modeyn=1
musicSwitch=-1
instructyn=-1
scorerun=False
add=20 #change later to more variables cuz points added differs
store=0
nrows=1 #number of rows broken
streak=2 #streak achieved if 3 without breaking it goes back to 0
numb=2 #number of blocks in shape
broken=True#if a row is broken
newgridRect=[Rect(370,150,350,350),Rect(370,150,490,490),Rect(370,150,540,540),Rect(370,150,420,420)]
gx=0
gy=0

currentShape="SLShape"
shapes1=["ThreeByThree","TwoByTwo","OneByOne","SLShape","SLShapeInvert","SLShapeUpsideD","SLShapeInvertUpsideD",
         "TShape","TShapeUpsideD","TShapeInvertLeft","TShapeInvertRight","ThreeByTwo","TwoByThree","LShape","LShapeUpsideD",
         "LShapeInvert","LShapeInvertUpsideD","LSShape","LSShapeUpsideD","LSShapeInvert"
         ,"LSShapeInvertUpsideD","FiveRow","FiveCol","FourRow","FourCol","ThreeRow","ThreeCol","TwoRow","TwoCol,Lightning",
         "LightningUpsideD","ZShape,ZShapeInvert"]
gridList=[[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
 [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
 [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)],
 [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)],
 [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)],
 [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)],
 [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
 [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]]
start=True
placed=-1

#rects
gridRect=Rect(370,150,560,560)
homeRect=Rect(125,125,400,150)
musicRect=Rect(125,325,450,150)
restartRect=Rect(125,525,400,150)
instructionsRect=Rect(575,125,550,150)
soundRect=Rect(575,325,550,150)
modeRect=Rect(575,525,615,150)
settingsRect=Rect(1210,20,70,70)
instructcloseRect=Rect(1100,120,50,50)


ThreeByThree=[[(row,col) for row in range(3)] for col in range (3)]
TwoByTwo=[[(row,col) for row in range(2)] for col in range (2)]
OneByOne=[[(row,col) for row in range(1)] for col in range (1)]

SLShape=[[(0,col) for col in range(3)]+[(1,2)]]
SLShapeInvert=[[(0,0)]+[(1,col) for col in range(-2,1)]]
SLShapeUpsideD=[[(0,col) for col in range(3)]+[(1,0)]]
SLShapeInvertUpsideD=[[(0,0)]+[(1,col) for col in range(3)]]

TShape=[[(row,0) for row in range(3)]+[(1,1)]]
TShapeUpsideD=[[(row,0) for row in range(3)]+[(1,-1)]]
TShapeInvertLeft=[[(0,col) for col in range(3)]+[(1,1)]]
TShapeInvertRight=[[(0,0)]+[(1,col) for col in range(-1,2)]]

ThreeByTwo=[[(row,col) for row in range(3)] for col in range(2)]
TwoByThree=[[(row,col) for row in range(2)] for col in range(3)]

LShape=[[(0,col) for col in range(3)]+[(row,2) for row in range(3)]] 
LShapeUpsideD=[[(row,0) for row in range(3)]+[(0,col) for col in range(3)]] 
LShapeInvert=[[(row,0) for row in range(3)]+[(2,col) for col in range(3)]] 
LShapeInvertUpsideD=[[(row,0) for row in range(3)]+[(2,col) for col in range(3)]] 

#LS is L, small shape
LSShape=[[(0,col) for col in range(2)]+[(row,1) for row in range(2)]] 
LSShapeUpsideD=[[(row,0) for row in range(2)]+[(0,col) for col in range(2)]] 
LSShapeInvert=[[(row,0) for row in range(2)]+[(2,col) for col in range(2)]] 
LSShapeInvertUpsideD=[[(row,0) for row in range(2)]+[(1,col) for col in range(2)]] 

FiveRow=[[(row,col) for row in range(5)] for col in range(1)]
FiveCol=[[(row,col) for row in range(1)] for col in range(5)]

FourRow=[[(row,col) for row in range(4)] for col in range(1)]
FourCol=[[(row,col) for row in range(1)] for col in range(4)]

ThreeRow=[[(row,col) for row in range(3)] for col in range(1)]
ThreeCol=[[(row,col) for row in range(1)] for col in range(3)]

TwoRow=[[(row,col) for row in range(2)] for col in range(1)]
TwoCol=[[(row,col) for row in range(1)] for col in range(2)]

#these aren't really row and col, it's two 2x1 rectangles
Lightning=[[(0,row) for row in range(2)]+[(1,col+1) for col in range(2)]]  #1st 2x1 is higher #****
LightningUpsideD=[[(0,row+1) for row in range(-1,1)]+[(1,col) for col in range(-1,1)]]  #1st 2x1 is lower #***
ZShape=[[(row,0) for row in range(2)]+[(col+1,1) for col in range(2)]]  #both z shapes go top to bottom #*****
ZShapeInvert=[[(row+1,0) for row in range(-1,1)]+[(col,1) for col in range(-1,1)]]  #1st 2x1 is lower #*** #[[(row+1,0) for row in range(2)]+[(col,1) for col in range(2)]] #************

WLShape=[[(row,1) for row in range(3)]+[(0,0)]] #WL is wide L shape
WLShapeInvert=[[(row,1) for row in range(3)]+[(0,2)]]
WLShapeUpsideD=[[(row,0) for row in range(3)]+[(0,1)]]
WLShapeInvertUpsideD=[[(row,0) for row in range(3)]+[(2,1)]]



#FUNCTIONS

#loading all images
settingsPic=image.load("images/settings.png")
settingsPic2=image.load("images/settingsbig.png")
crownPic=image.load("images/crown.png")
darklightPic=image.load("images/darklight.png")
darkPic=image.load("images/dark.png")
homePic=image.load("images/home.png")
instructionsPic=image.load("images/instructions.png")
instructclosePic=image.load("images/instructclose.png")
musicPic=image.load("images/music.png")
restartPic=image.load("images/restart.png")
soundPic=image.load("images/sound.png")
closePic=image.load("images/close.png")
onPic=image.load("images/on.png")
offPic=image.load("images/off.png")
info1Pic=image.load("images/info1.png")
info2Pic=image.load("images/info2.png")
menuimg=image.load("images/bg.png")

menuimg=image.load("images/bg.png")

squareani=image.load("images/sqrani.png")

highScoreimg=image.load("images/highscore bg.jpg")

scoreimg=image.load("images/score bg.jpg")




yellowRect=image.load("blocks/yellow.png")
darkBlueRect=image.load("blocks/darkBlue.png")
lightBlueRect=image.load("blocks/lightBlue.png")
greenRect=image.load("blocks/green.png")
redRect=image.load("blocks/red.png")
purpleRect=image.load("blocks/purple.png")
orangeRect=image.load("blocks/orange.png")

colours=[yellowRect,darkBlueRect,lightBlueRect,greenRect,redRect,purpleRect,orangeRect]

shapes=[ThreeByThree,TwoByTwo,OneByOne,SLShape,SLShapeInvert,SLShapeUpsideD,SLShapeInvertUpsideD,TShape,TShapeUpsideD,TShapeInvertLeft,TShapeInvertRight,ThreeByTwo,TwoByThree,LShape,LShapeUpsideD,LShapeInvert,LShapeInvertUpsideD,LSShape,LSShapeUpsideD,LSShapeInvert,LSShapeInvertUpsideD,FiveRow,FiveCol,FourRow,FourCol,ThreeRow,ThreeCol,TwoRow,TwoCol,Lightning,LightningUpsideD,ZShape,ZShapeInvert,WLShape,WLShapeInvert,WLShapeUpsideD,WLShapeInvertUpsideD]

ThreeSet=[]

ins=False

num=0

#parameters
m=1
m1=1
mu=(onPic)
mu1=(onPic)
modepic=darklightPic

def menu(page):
    running=True
    print("menu")
    buttons=[Rect(100+x*150,300,80,40) for x in range(4)]
    deg=0
    while running:
        for evt in event.get():
            if evt.type=="QUIT":
                return page=="exit"##
        screen.fill((0,0,0)) #black bg
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        playButton=Rect(445,445,480,80)
        draw.rect(screen,(0,0,0),playButton)
        screen.blit(menuimg,(0,0))

        if playButton.collidepoint(mx,my) and mb[0]:
            return page=="game"

        square=transform.rotate(squareani,deg)
        screen.blit(square, (625-square.get_width()//2,645-square.get_height()//2))
        #from rotate 2 file
        deg+=1
        display.flip()
        
def onoff(var,on,off):
        if var==-1:
                var==on
        if var==1:
                var=off
        return var
                
def drawScene():
        screen.fill(BGBLUE)
        draw.rect(screen,LINEBLUE,(370,150,560,560))
        #horizontal lines
        for i in range(9):
            draw.line(screen,GRIDBLUE,(370+i*70,150),(370+i*70,710),2)
        #vertical lines
        for i in range(9):
            draw.line(screen,GRIDBLUE,(370,150+i*70),(930,150+i*70),2)
        #settings button
        screen.blit(settingsPic,(1210,20))
        #crown high score
        screen.blit(crownPic,(20,20))
        high=arielsmall.render(f"{highscore}",True,WHITE)
        screen.blit(high,(80,35))
        #currentscore
        score=arielbig.render(f"{currentscore}",True,WHITE)
        screen.blit(score,(610,55))#if extra time center score as the len goes up
        #hovering
        if settingsRect.collidepoint(mx,my):
                draw.rect(screen,LINEBLUE,settingsRect,3,10,10,10,10)

        #hovering over grid
        #finding which small section of grid it's in
        column=(mx-370)//70
        row=(my-150)//70
##        gridSpot=gridList.index((row,column))
##        print(gridSpot)
        gxm=mx%70
        gym=my%70
        
        gx=mx-gxm+21
        gy=my-gym+11
##        border=[((gx,gy),(210+gx,gy),(210+gx,210+gy),(gx,210+gy),(gx,gy)),
##                ((gx,gy),(140+gx,gy),(140+gx,140+gy),(gx,140+gy),(gx,gy)),
##                ((gx,gy),(70+gx,gy),(70+gx,70+gy),(gx,gy+70),(gx,gy)),
##                ((gx,gy),(gx+70,gy),(gx+70,gy+140),(gx+140,gy+140),(gx+140,gy+210),(gx,gy+210),(gx,gy)),
##                ((gx+70,gy),(gx+140,gy),(gx+140,gy+210),(gx,gy+210),(gx+70,gy)),
##                ((gx,gy),(gx+140,gy),(gx+140,gy+70),(gx+70,gy+70),(gx+70,gy+210),(gx,gy+210),(gx,gy)),
##                ((gx,gy),(gx+140,gy),(gx+140,gy+210),(gx+70,gy+210),(gx+70,gy+70),(gx,gy+70),(gx,gy)),
##                ((gx,gy),(gx+210,gy),(gx+210,gy+70),(gx+140,gy+70),(gx+140,gy+140),(gx+70,gy+140),(gx+70,gy+70),(gx,gy+70),(gx,gy)),
##                ((gx+70,gy),(gx+140,gy),(gx+140,gy+70),(gx+210,gy+70),(gx+210,gy+140),(gx,gy+140),(gx,gy+70),(gx+70,gy+70),(gx+70,gy)),
##                ((gx,gy),(gx+70,gy),(gx+70,gy+70),(gx+140,gy+70),)]

        if ins and mb[0] and gridRect.collidepoint(mx,my):
            Index_Zero=ThreeSet[num][0]
            idx=Index_Zero[5]
            
            if gridRect.collidepoint(mx,my):
                    #CurrentShape=shapes[idx]
                    #print(CurrentShape)
                    CurrentShape=ThreeSet[num]
                    #print(CurrentShape)
                    for j in CurrentShape:
                        #print(CurrentShape[j])
                        #for i in CurrentShape[0]:
                        print(j[0],j[1])
                        draw.rect(screen,(19,30,69),(j[0]*70+gx,j[1]*70+gy,70,70))
                    Shape=ThreeSet[num]
                    

##                        for i in range(len(CurrentShape)):
            if placed==1:
                for j in range(len(Shape)):

                    screen.blit(colours[Shape[j][-2]],(Shape[j][0]*70+gx,Shape[j][1]*70+gy))
                    print("cool")

                    #placed=False
        if len(ThreeSet)==0: #why is the largest number possible here the num of squares - 1
                for s in range(3): #the shape
                    colour=randint(0,6) #random index for choosing a colour, i need to store this for when i want to drag
                    block=colours[colour] #assigning the block for the shape
                    shapeidx=randint(0,36)
                    TupleShape=shapes[shapeidx] #this shape is made in a list of tuples, but later on we will need it to be a 2D list so that we can manipulate the variables
                   
                    shape=[] #changing the tuple to a 2D list since we need the mutability for selecting
                    for r in range (len(TupleShape)): #every individual square of the shape
                        for c in range (len(TupleShape[r])):
                            sq=[]
                            #empty list #each var needed (e.g. x,y,width,len)
                            
                            for pt in range (len(TupleShape[r][c])): #for every variable we need
                                p=TupleShape[r][c][pt]
                                #print(p)
                                sq.append(p)
                            sq.append(colour)
                            sq.append(shapeidx)
                            #    x, y   exact locations                 colour, shape
                            sq=sq[0:2]+[100+sq[0]*30,200+sq[1]*30+200*s]+sq[2:]
                            #print(sq)
        ##                    print("\n\n)
                            shape.append(sq)
        ##            print("This Is",len(shape))
                    
                    pBlock=transform.scale(block,(30,30)) #preview blocks
                    for sqr in range(len(shape)):
                        #shape[sqr][1]+=s*200
                        screen.blit(pBlock,(100+shape[sqr][0]*30,200+shape[sqr][1]*30+200*s))
                        print("hi")
                    ThreeSet.append(shape)
                    #pprint(ThreeSet)
                    #print(len(ThreeSet))
##                    print(len(ThreeSet[0]))
##                    print(len(ThreeSet[1]))
##                    print(len(ThreeSet[2]))
        if len(ThreeSet)==3:
            for s1 in range(3):
                shape1=ThreeSet[s1]
                #print(shape1[0][-2])
                pBlock=transform.scale(colours[shape1[0][-2]],(30,30))
                for sqr1 in range(len(shape1)):            
                        screen.blit(pBlock,(100+shape1[sqr1][0]*30,200+shape1[sqr1][1]*30+200*s1))

        for piece in ThreeSet: #we only have variables
                for square in piece:
                    if num == ThreeSet.index(piece):
                        if mb[0] and ins:
                            for bit in piece: #blitting just like previously
                                screen.blit(colours[bit[-2]],(mx+bit[0]*70,my+bit[1]*70))
                                
                
        display.flip()

                 
def settings():
        #close icon
        draw.rect(screen,BGBLUE,(0,0,1300,800))
        screen.blit(closePic,settingsRect)
        #screen
        draw.rect(screen,LINEBLUE,(100,100,1100,600),500,50,50,50,50)
        #icons
        screen.blit(homePic,(150,150))
        screen.blit(instructionsPic,(600,150))
        screen.blit(musicPic,(150,350))
        screen.blit(mu,(475,360))
        screen.blit(soundPic,(600,350))
        screen.blit(mu1,(925,360))
        screen.blit(restartPic,(150,550))
        screen.blit(modepic,(600,550))
        #text
        home=arielsettings.render("Home",True,BLACK)
        screen.blit(home,(270,175))
        instructions=arielsettings.render("Instructions",True,BLACK)
        screen.blit(instructions,(720,175))
        music=arielsettings.render("Music",True,BLACK)
        screen.blit(music,(270,375))
        effects=arielsettings.render("Sound",True,BLACK)
        screen.blit(effects,(720,375))
        restart=arielsettings.render("Restart",True,BLACK)
        screen.blit(restart,(270,575))
        mode=arielsettings.render("Dark/Light Mode",True,BLACK)
        screen.blit(mode,(720,575))

        #hovering
        if homeRect.collidepoint(mx,my):
                draw.rect(screen,WHITE,homeRect,3,30,30,30,30)
        if instructionsRect.collidepoint(mx,my):
                draw.rect(screen,WHITE,instructionsRect,3,30,30,30,30)
        if musicRect.collidepoint(mx,my):
                draw.rect(screen,WHITE,musicRect,3,30,30,30,30)
        if soundRect.collidepoint(mx,my):
                draw.rect(screen,WHITE,soundRect,3,30,30,30,30)
        if modeRect.collidepoint(mx,my):
                draw.rect(screen,WHITE,modeRect,3,30,30,30,30)
        if restartRect.collidepoint(mx,my):
                draw.rect(screen,WHITE,restartRect,3,30,30,30,30)
        #instructions
        if instructyn==1:
                draw.rect(screen,GRIDBLUE,(100,100,1100,600),500,50,50,50,50)
                screen.blit(instructclosePic,instructcloseRect)
                title=infotitle.render("HOW TO PLAY",True,WHITE)
                screen.blit(title,(200,200))
                text1=info.render("1. Drag and drop blocks onto grid.",True,WHITE)
                screen.blit(text1,(200,350))
                text2=info.render("2. If you fill the any row or column it will dissapear.",True,WHITE)
                screen.blit(text2,(200,450))
                text3=info.render("3. Get the highest score without running out of moves!",True,WHITE)
                screen.blit(text3,(200,550))
                screen.blit(info1Pic,(750,200))
                screen.blit(info2Pic,(1000,425))
                

        display.flip()
        
            



yes=-1#if yes=1 then settings if open if it's negative 1 settings is not open
page="menu"
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONUP and settingsRect.collidepoint(mx,my):
                yes=yes*-1
        #if settings buttons are pressed
        if evt.type==MOUSEBUTTONUP and modeRect.collidepoint(mx,my) and page=="settings":
                modeyn=modeyn*-1
                if modeyn==-1:
                        BGBLUE=(13,25,77)
                        modepic=darkPic
                if modeyn==1:
                        BGBLUE=(53,72,131)
                        modepic=darklightPic
        if evt.type==MOUSEBUTTONUP and musicRect.collidepoint(mx,my) and page=="settings":
                m=m*-1
                if m==1:
                        mu=onPic
                        musicSwitch=-1
                if m==-1:
                        mu=offPic
                        musicSwitch=0
##                onoff(m,onPic,offPic)
        if evt.type==MOUSEBUTTONUP and soundRect.collidepoint(mx,my) and page=="settings":
                m1=m1*-1
                if m1==1:
                        mu1=(onPic)
                if m1==-1:
                        mu1=(offPic)
        if evt.type==MOUSEBUTTONUP and restartRect.collidepoint(mx,my) and page=="settings":
                yes=-1
                currentscore=0                
        if evt.type==MOUSEBUTTONUP and instructionsRect.collidepoint(mx,my) and page=="settings":
                instructyn=instructyn*-1
        if evt.type==MOUSEBUTTONUP and gridRect.collidepoint(mx,my) and page=="game":
                scorerun=True
                if broken:
                        if streak==0:
                                add=numb+((2)*10*(nrows))
                        else:
                                add=numb+((2**(streak-1))*10*(nrows))
                else:
                        add=numb
                store=currentscore+add
                placed=1
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                if len(ThreeSet)==3:
                    for i in ThreeSet:
                        for j in i:
                            rect=Rect(j[2],j[3],30,30)
                            if rect.collidepoint(mx,my):
                                num=ThreeSet.index(i)
                                ins=True
        if evt.type==MOUSEBUTTONUP:
            ins=False

        
                

                
                
                
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

##    print(mx,my)
    if scorerun:
        currentscore+=1
    if currentscore>=store:
            scorerun=False



    if currentscore>=highscore:
            highscore=currentscore
    if page=="menu":
        menu(page)
    if yes==1 and start:
        page="settings"
    if yes==-1 and start:
        page="game"
    if page=="game":
        drawScene()
##        mixer.music.load("bgmusic.mp3")
##        mixer.music.play(loops=musicSwitch)
    if page=="settings":
        scorerun=False
        settings()

    myClock.tick(60)
    display.flip()
            
quit()
