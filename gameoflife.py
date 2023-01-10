import pygame, sys
pygame.init()
size = width , height = 800 , 600
screen = pygame.display.set_mode(size)
black = 0,0,0
grid_y = height//10
grid_x = width//10
celllist=[]
delaytick = 3
white = 255,255,255
screen.fill(black)
simflag=0

# Initialize grid
def initialize_grid():
    global celllist
    celllist = []
    for l in range(0,grid_x):
        celllist.append([[0,0,l,i] for i in range(grid_y)])

def simulationloop():
    global celllist
    if event.type==pygame.QUIT: sys.exit()

    # Step 1 of simulation logic, checking how many adjacent cells are alive

    for column in celllist:
        for cell in column:
            counter=0
            try:
                if celllist[cell[2]+1][cell[3]+1][0]==1:
                    counter+=1
            except:
                None
            try:
                if cell[2]>0:
                    if celllist[cell[2]-1][cell[3]+1][0]==1:
                        counter+=1
            except:
                None
            try:
                if celllist[cell[2]][cell[3]+1][0]==1:
                    counter+=1
            except:
                None
            try:
                if celllist[cell[2]+1][cell[3]][0]==1:
                    counter+=1
            except:
                None
            try:
                if cell[2] > 0 and cell[3] > 0:
                    if celllist[cell[2]-1][cell[3]-1][0]==1:
                        counter+=1
            except:
                None
            try:
                if cell[2]>0:
                    if celllist[cell[2]-1][cell[3]][0]==1:
                        counter+=1
            except:
                None
            try:
                if cell[3]>0:
                    if celllist[cell[2]][cell[3]-1][0]==1:
                        counter+=1
            except:
                None
            try:
                if cell[3]>0:
                    if celllist[cell[2]+1][cell[3]-1][0]==1:
                        counter+=1
            except:
                None
            celllist[cell[2]][cell[3]][1]=counter

    # step 2 of simulation logic, setting alive or dead status to cell, resetting the cell counter and drawing the cells

    for column in celllist:
        for cell in column:
            if cell[1]==3:
                celllist[cell[2]][cell[3]][0]=1
            elif cell[1]==2 and cell[0]==1:
                celllist[cell[2]][cell[3]][0]=1
            else:
                celllist[cell[2]][cell[3]][0]=0
            if cell[0]==1:
                pygame.draw.rect(screen,white,(cell[2]*10,cell[3]*10,10,10))
            elif cell[0]==0:
                pygame.draw.rect(screen,black,(cell[2]*10,cell[3]*10,10,10))
            celllist[cell[2]][cell[3]][1]=0
    
    # throwing new frame on screen, calling event queue to prevent windows from declaring the program unresponsive

    pygame.display.flip()
    pygame.event.pump()
    
        
initialize_grid()
while True:
    pygame.time.wait(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            tempx,tempy=pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
            tempx=tempx//10
            tempy=tempy//10
            if celllist[tempx][tempy][0]==0:
                celllist[tempx][tempy][0]=1
                pygame.draw.rect(screen,white,(tempx*10,tempy*10,10,10))
                pygame.display.flip()
            else:
                celllist[tempx][tempy][0]=0
                pygame.draw.rect(screen,black,(tempx*10,tempy*10,10,10))
                pygame.display.flip()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            simflag=1
        while simflag==1:
            pygame.time.wait(80)
            simulationloop()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    simflag=0
                if event.type==pygame.KEYDOWN and event.key==pygame.K_BACKSPACE:
                    simflag=0
                    initialize_grid()
                    screen.fill(black)
                    pygame.display.flip()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_BACKSPACE:
            initialize_grid()
            screen.fill(black)
            pygame.display.flip()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
            simflag=1
        while simflag==1:
            pygame.time.wait(80)
            simulationloop()
            for event in pygame.event.get():
                if event.type==pygame.KEYUP and event.key==pygame.K_s:
                    simflag=0

