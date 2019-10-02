import tkinter as tk
import math
import random 
import os
import playsound as ps
import threading



class Ball:
	def __init__(self, master=None, size=60):
		#Ball coords + direction
		self.master = master 
		
		self.size = size
		self.xpos = 300
		self.ypos = 300
		self.dir = 315 #directly right = 0 degrees
		#Create ball using canvas.create_polygon(x1, y1... xn, yn) 
		coords = []
		
		#Calculate 360 coordinates to create the shape of the ball
		for i in range(360):
			rad_angle = (i) * (math.pi / 180)
			rel_y = self.xpos + size*math.sin(rad_angle)
			rel_x = self.ypos + size*math.cos(rad_angle)
			coords.append(rel_x)
			coords.append(rel_y)
		
		#unpack coords array into create_polygon
		self.id = self.master.create_polygon(*coords, fill='white')
	
	def move_ball(self, angle, speed):
		#Method to move the ball given an angle and a speed
		x_comp = speed*math.cos(math.radians(angle)) #x-component of the velocity vector: a*cos(angle)
		y_comp = speed*math.sin(math.radians(angle)) #y-component of the velocity vector: a*sin(angle)
		#update xpos and ypos and move ball by that much in the x and y directions
		self.xpos = self.xpos + x_comp
		self.ypos = self.ypos + y_comp
		self.master.move(self.id, x_comp, y_comp)

class Bar:
	def __init__(self, master=None, width=250):
		self.master = master 
		self.width = width 
		self.xpos = 100
		self.ypos = 1000
		self.height = 100
		
		self.id = self.master.create_rectangle(100, 1000, 100+self.width, 1000-self.height, fill='white')
	
	def move_bar(self, dist):
		self.xpos += dist 
		self.master.move(self.id, dist, 0)

		
main = tk.Tk()
root = tk.Canvas(main, bg='black', width=1000, height=1000)
ball = Ball(root)
rect = Bar(master=root)
move_angle = 45
speed = 8
sounds_dir = '/Users/TheBestKid/Desktop/Programming/Graphics/Sounds'

def play_sound():
	rand_index = random.randint(0, len(os.listdir(sounds_dir))-1)
	print(os.listdir(sounds_dir)[rand_index][-4:])
	if os.listdir(sounds_dir)[rand_index][-4:] == '.wav':
		ps.playsound(os.path.join(sounds_dir, os.listdir(sounds_dir)[rand_index]), False)

def move_rect(event):
	if event.char == 'f':
		rect.move_bar(-100)
		
	elif event.char == 'j':
		rect.move_bar(100)
		
	else:
		print(event.char)

root.bind('<Key>', move_rect)
root.focus_set()
root.pack()
#main loop; loops until infinity
counter = 0
x = True 
score = 0
while x == True:
	ball.move_ball(move_angle, speed)
	root.update_idletasks()
	root.update()
	counter += 1
	
	if counter > 3:
		if (ball.xpos >= (1000-ball.size)):
			counter = 0
			play_sound()
			if (move_angle < 90) or (move_angle < 270):
				move_angle = move_angle + 90
				ball.move_ball(move_angle, speed / 5)
			else:
				move_angle = move_angle - 90
				ball.move_ball(move_angle, speed / 5)
		elif ball.xpos <= (ball.size):
			play_sound()
			counter = 0
			play_sound()
			if (move_angle > 180):
				move_angle = move_angle + 90
				ball.move_ball(move_angle, speed / 5)
			else:
				move_angle = move_angle - 90
				ball.move_ball(move_angle, speed / 5)
		
		elif ball.ypos >= (1000-(ball.size+rect.height)):
			play_sound()
			counter = 0
			play_sound()
			if (ball.xpos >= rect.xpos and ball.xpos <= rect.xpos + 300):
				if move_angle > 90:
					i = random.randint(0, 3)
					move_angle = 225 + i*10
				else:
					i = random.randint(6, 9)
					move_angle = 225 + i*10
				speed += 1
				score += 1
			else:
				x = False 
				break

		elif ball.ypos <= (ball.size):
			play_sound()
			counter = 0
			play_sound()
			if (move_angle > 270):
				move_angle = move_angle - 270
				ball.move_ball(move_angle, speed / 5)
			else: 
				move_angle = move_angle - 90
				ball.move_ball(move_angle, speed / 5)

print('loop broken')
root.create_text((500, 500), fill='white', font=('Arial', 125), text='You got ' + str(score) + ' hits')
print('packed')
main.mainloop()

		



