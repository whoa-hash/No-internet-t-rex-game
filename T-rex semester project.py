#"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity poicy of the CS department.”
import Draw
import math
import random
Draw.setCanvasSize(700, 500)
             
#below-makes a cactus middle and sides(the verticle cylinder-like parts, not the parts that join the middle to the side parts)
def filledRoundedRect(x, y, wide, high):
       coords=[x, y+wide/2, x, y+high+wide/2, x+wide, y+high+wide/2, x+wide, y+wide/2]
       for angle in range(3, 180, 6):
              rad=math.radians(angle)
              newx=math.cos(rad)*wide/2
              newy=math.sin(rad)*wide/2
              coords+=[x+wide/2+newx, y+wide/2-newy]
       Draw.filledPolygon(coords)

#below-makes my cacti list             
def listobstacles():
       obstacles=[]
       x=random.randint(640, 1000) #first cactus's starting point
       for i in range(100):
              obstacles+=[(x, 223)] #corresponds to (the x coordinate, the y(which is always the same))
              x=x+random.randint(100, 400) #increments the space in between each next cactus
       return obstacles


#below-makes my ground dashes list                                         
def listground():
       ground=[]
       xbasedon=random.randint(50,51) #first dash's starting point
       for i in range(2000):
              ybasedon=random.randint(253, 256) #the height of the dashes
              ground+=[(xbasedon, ybasedon, xbasedon+5,ybasedon)] #corresponds to (x, y(which is the same as height so that the line is straight), width, height)
              xbasedon+=random.randint(10,70) #increments the space in between each dash
       return ground

#below-makes my ground made of dots list
def listdots():
       dots=[]
       xbasedon=random.randint(50, 51) #first dot's starting pt.
       for i in range(2000):
              ybasedon=random.randint(253, 256) #the differing heights of the dots
              widthandheight=random.random() #the differing widths and heights that make up my dots
              dots+=[(xbasedon, ybasedon, widthandheight, widthandheight)] #corresponds to (x, y, width, height)
              xbasedon+=random.randint(10,60) #increments the space in between each next dot
       return dots

#below creates my t-rex               
def dino(dinoY):
                #below is the body
              Draw.filledRect(110, 231+dinoY, 9, 10)
              Draw.filledRect(108, 233+dinoY, 9, 10)
              Draw.filledRect(106, 235+dinoY, 9, 10)
              Draw.filledRect(102, 239+dinoY, 4, 8)
              Draw.filledRect(103, 246+dinoY, 4,3)#the 'thigh' on the left
              Draw.filledRect(108, 246+dinoY, 4,3)#the 'thigh' on the right
              Draw.filledRect(103, 246+dinoY, 2, 9)#the left 'leg'
              Draw.filledRect(108, 246+dinoY, 2, 9)#the right 'leg'
                #below are the 'feet'
              Draw.filledRect(108, 254+dinoY, 4,2)#the 'foot' on the right
              Draw.filledRect(103, 254+dinoY, 4,2)#the 'foot' on the left
                #below is the tail
              Draw.filledRect(95, 230+dinoY, 2, 10)
              Draw.filledRect(97, 233+dinoY, 2, 10)
              Draw.filledRect(99, 235+dinoY, 2, 10)
              Draw.filledRect(101, 238+dinoY, 2, 10)
              Draw.filledRect(103, 238+dinoY, 3, 11)
                #below are the units of the head=[110, 235, 125, 235, 125, 225, 110, 225] but are able to 'jump'(+ dinoY) along with the whole t-rex
              head=[110, 233+dinoY, 122, 233+dinoY, 121, 231+dinoY, 125, 231+dinoY, 125, 225+dinoY, 123, 225+dinoY, 123, 223+dinoY, 112, 223+dinoY, 112, 223+dinoY, 110, 225+dinoY]
              Draw.filledPolygon(head)
              Draw.setColor(Draw.WHITE)
                #below is the 'eye'
              Draw.filledRect(113, 226+dinoY, 3, 3)
              Draw.setColor(Draw.BLACK)
              
def arrow():#draws the white arrow that's part of the black game over sign
       Draw.setColor(Draw.WHITE)
       Draw.filledRect(326,220, 2, 7)
       Draw.filledRect(341, 220, 2, 7)
       Draw.filledRect(328, 227, 13, 2)
       Draw.filledRect(328,218, 4,2)
       Draw.filledRect(332, 216,2,6)
       Draw.filledRect(334, 217,1, 4)
       Draw.filledRect(334,218, 1,2)
       Draw.filledRect(335,217.5,1,1)
       Draw.setColor(Draw.BLACK)# for the words after arrow() is called to return to black
              
#below stops my game when a cactus is hit by the t-rex(or there's a win-a score of 6000)
def hitcactus(dinox, dinoY, obstacles, score): 
       WindowLeft=dinox-100
       for i in range(len(obstacles)): #using the cacti list:
              xcoordinate=obstacles[i][0]-WindowLeft #uses the same x-coordinate as the cacti' respective to the changing WindowLeft
                  #below-stops the game, game over, once the cactus is hit
                  #if the t-rex's x coordinate is more than the cactus's left x-coordinate and less than the cactus's right x coordinate and the height is not above the cactus or the score is at 6000:
              if dinox>xcoordinate+WindowLeft-33 and dinoY>= -50 and dinox<xcoordinate+WindowLeft+11 or score==6000:
                     Draw.setFontFamily('OCR A Extended')#for the game over(or win)
                     Draw.setFontBold(True)#sets the game over words(or win) to a strong black 
                     if score==6000: #if the score is at 6000 it'll only write 'You Won'
                            Draw.string('You Won', 295, 180)
                     else:
                            Draw.string('G A M E  O V E R', 260, 180) 
                     Draw.setFontBold(False)#sets the playagain words
                     Draw.setFontFamily('Courier') #also sets the playagain words
                     Draw.string('Press space to continue playing', 306, 20)
                     gameover=[320, 208, 321,207, 349, 207, 350, 208, 350, 238, 349,238, 320, 238]
                     Draw.setColor(Draw.DARK_GRAY) #sets the game over square to dark gray
                     Draw.filledPolygon(gameover)#black gameover square  
                     arrow()
                     return True                

#below-draws the ground made up of lines
def draw(ground, dinox, dinoY):
       WindowLeft=dinox-100
       for i in range(len(ground)):
              linexcoordinate=ground[i][0]-WindowLeft #the xcoordinate of each ground/dash respective to the window that's changing
              if linexcoordinate>49 and linexcoordinate<640: #the ground has to be within the parameters of the center line and not past it
                     Draw.line(linexcoordinate, ground[i][1], linexcoordinate+5, ground[i][3]) #corresponds to (x, y(same), width, height(same, because it's a straight line))
                     
#below-draws the list of dots as they appear according to the window that moves to the right (so the dots keep on being drawn more to the left)
def drawalsodots(dots,dinox,dinoY):
       WindowLeft=dinox-100
       for i in range(len(dots)): #the list of dots is being used
              dotxcoordinate=dots[i][0]-WindowLeft #the dot's x-coordinate respective to the moving window
              if dotxcoordinate>49 and dotxcoordinate<640: #if the dot's x-coordinate spans the length of the center line:
                     Draw.filledOval(dotxcoordinate, dots[i][1],2, 2) #corresponds to (x, y, width, height)
                     
#below-draws the cacti
def drawobstacles(dinox, dinoY, obstacles):
       WindowLeft=dinox-100
       for i in range(len(obstacles)): #the list of cacti are being used
              xcoordinate=obstacles[i][0]-WindowLeft #the xcoordinate of each cacti respective to the changing window
              if xcoordinate<649 and xcoordinate>49: #if the xcoordinate falls into the parameter of the length of the center line:
                            #Draw.setColor(Draw.DARK_GRAY)#sets the cacti to dark gray
                            filledRoundedRect(xcoordinate, obstacles[i][1]-6, 6, 33)
                            filledRoundedRect((xcoordinate-8), obstacles[i][1]+6, 3.5, 10)
                            filledRoundedRect((xcoordinate+10), obstacles[i][1]+2, 3.5, 10)
                            #below-is the left conndecting side part
                            Draw.filledRect((xcoordinate-4.5),obstacles[i][1]+19, 6,3)
                            Draw.filledRect((xcoordinate-5.5),obstacles[i][1]+17, 9, 3)
                            Draw.filledRect((xcoordinate-6.5),obstacles[i][1]+18,9,3)
                            #below-the right connecting side part
                            Draw.filledRect((xcoordinate+6),obstacles[i][1]+12,9,3)
                            Draw.filledRect((xcoordinate+5),obstacles[i][1]+13,8,3)
                            Draw.filledRect((xcoordinate+5),obstacles[i][1]+15,7,2)   

#below-draws the no-internet screen background with the center line across the screen
def background():
       Draw.setFontFamily('Calibri')
       Draw.setColor(Draw.BLACK)
         #below-the three bullet points
       Draw.filledOval(58, 367, 4,4)
       Draw.filledOval(58, 397, 4, 4)
       Draw.filledOval(58, 427, 4, 4)
       Draw.setFontSize(16)
       Draw.string('No internet', 50, 290)
       Draw.setFontBold(False)
       Draw.setColor(Draw.DARK_GRAY)
       Draw.setFontSize(12)
       Draw.string('Try:', 50,320)
       Draw.string('    Checking the network cables, modem, and router', 55, 360)
       Draw.string('    Reconnecting to Wi-Fi', 55, 390)
       Draw.setColor(Draw.BLUE)
       Draw.string('    Running Windows Network Diagnostics', 55, 420)
       Draw.setColor(Draw.DARK_GRAY)
       Draw.setFontSize(11)
       Draw.string('DNS_PROBE_FINISHED_NO_INTERNET', 50, 460) 
       Draw.line(650, 250, 50, 250)#center line       
       
            
#below-draws the complete board             
def Drawboard(dinox, dinoY, obstacles, ground, draw, score, dots):
              Draw.clear() #starts a new frame
              #below-sets the background words of the no-internet screen and the center line
              background()
              draw(ground, dinox, dinoY) #draws the dashes of the ground
              drawalsodots(dots,dinox,dinoY) #draws the dots of the ground
              dino(dinoY) #draws the t-rex in each frame
              Draw.setFontBold(True)
              Draw.setFontFamily('OCR A Extended')
              Draw.string('Score  '+str(score), 515, 40)#draws the score while the game is still playing              
              Draw.setColor(Draw.DARK_GRAY)
              drawobstacles(dinox, dinoY, obstacles) #draws the cacti
              hitcactus(dinox, dinoY, obstacles, score) #accounts for cacti that are touched/hit
              if score>=4000:
                     Draw.show(.01)
              elif score>=1000:
                     Draw.show(.3)#board moves faster once the score hits 1000
              else:
                     Draw.show(.5) #draws the frame on the screen at the .5 speed
                     
#below-plays the game with user input
def playgame(Hiscore):
       obstacles=listobstacles() 
       dots=listdots()
       ground=listground()
       dinoJump=0           #sets the time that the t-rex will stay in the air for, here it's 0
       dinoY=0              #the height of the t-rex is set here, to 0
       dinox=100            #the x-coordinate of the t-rex is set here, to 100
       WindowLeft=dinox-100 #the Window Left is set here according to the t-rex's x-coordinate, here it's 0
       score=0              #the score is set here, to 0
       GameOver=False       #sets the GameOver to False
       while not GameOver: #as long as the person doesn't hit a cactus/get to 6000(the hitcactus function resets the GameOver to be True(and hence change while not GameOver to = while GameOver):
              score+=1     #increments the score
              if Draw.hasNextKeyTyped(): #if the user typed a key
                     newKey=Draw.nextKeyTyped() #get the key
                     if dinoJump>0: #this makes sure you cannot stay in the air for multiple key presses
                            dinoY=-53 #'jumps' the t-rex
                     elif newKey=='Up'or newKey=='space'or dinoJump<=0: #jumping the dino if the user pressed the space bar or the up arrow
                            dinoJump=80 #keeps the dino in the air for a (80) length of time
              if dinoJump<=0: #makes sure the dinoJump does not go into the negatives
                     dinoJump=0
              else:
                     dinoJump-=1 #decreases the dinoJump by 1
              if dinoJump>0:     #makes the dino 'Jump'-stay at its increased height according to the length of time
                     #dinoY= a height of 177
                     dinoY = -53
              else: #if there's no input from the user that caused the dinoJump to go up:
                     #dinoY=a lower height of 230
                     dinoY = 0  #keeps the dino on the 'ground'
              dinox+=1 #increases the xcoordinate of the dino which will increase/move the window one more to the right 
              Drawboard(dinox, dinoY, obstacles, ground, draw, score, dots) #draws the whole board
              GameOver=hitcactus(dinox, dinoY, obstacles, score)#stops the game
       Draw.string('Hi '+str(Hiscore), 4, 50)

#below-allows for the game to be played again according to user input of the up arrow or spacebar                
def playagain(Hiscore):
       score=0
       if Draw.hasNextKeyTyped():
                     newKey=Draw.nextKeyTyped()
                     if newKey=='Up'or newKey=='space':
                            playgame(Hiscore)       
                     
#main plays the complete game with another game able to be played right after              
def main():
       score=0
       Hiscore=0
       playgame(Hiscore)
       while True: #checks the whole time once the game is finished if the user pressed an up arrow or a space according to the rule that runs the game again in the playagain function
              if score>Hiscore:
                     Hiscore=score              
              playagain(Hiscore)
                         
main()

