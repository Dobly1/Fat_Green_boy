class Player:
	x_pos = 1
	y_pos = 1
	color = 1
	memory = {-1:[[1,1]]}
	recent_memory = [1,1]
	def move(self,dir):
	
		self.recent_memory=[self.y_pos,self.x_pos]
		if dir == "d":
			self.x_pos+=1
		if dir == "a":
			self.x_pos-=1
		if dir == "s":
			self.y_pos+=1
		if dir == "w":
			self.y_pos-=1
		coordinate = [self.y_pos,self.x_pos]
		if coordinate not in self.memory[-1]:
			self.memory[-1].append(coordinate)
		
	
from SimpleGraphics import *
import random
import math


def get_color(color_number):
	if (color_number==0):
		return "green"
	if (color_number==1):
		return "red"
	if (color_number==2):
		return "black"
	if (color_number==4):
		return "yellow"
	if (color_number==5):
		return "blue"
def create_grid (x,y): #Makes grid of dimmensions X*Y

	
	

	circle_color = [] #Creates Matrix
	#Decide Colour)
	
	for i in range(x):
		circle_color.append([])
		for j in range(y):
				circle_color[i].append(2) #Fill MAtrix with Wall Values
				
					
	'''
	for i in range(1,11,2):
		create_path(circle_color,0,i,10,i)
	create_path(circle_color,1,0,1,10)
	create_path(circle_color,9,0,9,10)
	'''
	
	for i in range(1,y):
		random_x = random.randint(1,10)
		random_y = random.randint(2,9)
		create_path (circle_color,1,i,random_x,random_y) #
	
	for i in range(1,x):

		for j in range(1,y):
			if circle_color[i][j] == 1:
				random_chance = random.randint(1,10)

				if random_chance>9:
					circle_color[i][j] = 0
	
	
	return circle_color

def valid_move(grid,p,move):
	player_x = p.x_pos
	player_y = p.y_pos
	
	
	if move == "d":
		player_x += 1
	if move == "a":
		player_x -=1
		move_dir = 1
	if move == "s":
		player_y +=1
	if move == "w":
		player_y -=1
	
	if grid[player_x][player_y] == 2:
		return False
	
	if player_x > len(grid) -2 or player_x < 1:
		return False
		
	if player_y < 1 or player_y > len(grid[0])-2:
		return False
	
	
	return True
		
		

def create_path (circle_color,x_spot,y_spot,x,y,color = 1):
	while True:

		circle_color[x_spot][y_spot] = color

		x_distance = x - x_spot
		y_distance = y - y_spot
		
		
		
		
		
		if (x_distance>0):
			x_spot+=1
			
		if (x_distance<0):
			x_spot-=1
			
		if (y_distance>0):
			y_spot+=1
			
		if (y_distance<0):
			y_spot-=1
			
		
		if (y_distance==0 and x_distance==0):
			break
	return circle_color
	
def draw_map (circle_color, player):
	
	
	setColor("black")
	rect(55,15,1055,1055)
	wall_sprite = loadImage("wall1.gif")
	floor_sprite = loadImage("floor.gif")
	chest_sprite = loadImage("chest.gif")

	for i in range( player.x_pos, player.x_pos+3):
		for j in range(player.y_pos, player.y_pos+3):
			if circle_color[i-1][j-1] == 2:
				drawImage(wall_sprite,i*55,j*55-40)
			elif circle_color[i-1][j-1] == 1:
				drawImage(floor_sprite,i*55,j*55-40)
			elif circle_color[i-1][j-1] == 0:
				drawImage(floor_sprite,i*55,j*55-40)
				drawImage(chest_sprite,i*55,j*55-40)
			else:
				setColor(get_color(circle_color[i-1][j-1]))
				rect(i*55,j*55-40, 50,50)
				setColor("white")
				text(i*55,j*55-40,str(i)+" "+str(j))
	

	setColor(get_color(player.color))
	rect ((player.x_pos+1)*55,(player.y_pos+1)*55-40,50,50)
	

	
def update_map (map,player):

	
	
	wall_sprite = loadImage("wall1.gif")
	floor_sprite = loadImage("floor.gif")
	chest_sprite = loadImage("chest.gif")
	
	
	
	
	if len( player.memory[-1] ) > 1:
		recent_memory = player.recent_memory
		current_coord = player.memory[-1][-1]
		
		
		if map[recent_memory[1]][recent_memory[0]] == 1:
			img = floor_sprite
		else:
			img = chest_sprite
		
		
		
		
		
		drawImage(img, (recent_memory[1]+1)*55, (recent_memory[0]+1)*55-40)
		
		delta_y = (current_coord[0] - recent_memory[0])
		delta_x = (current_coord[1] -recent_memory[1])
		
		if (abs(delta_x)) > (abs(delta_y)):
			for i in range(-1,2):
			
				y = player.y_pos+1
				x = player.x_pos+i
			
				current_spot = map[y][x]
				
				if current_spot == 2:
					img = wall_sprite
				if current_spot == 1:
					img = floor_sprite
				if current_spot == 0:
					img = chest_sprite
				
				drawImage ( img,(x+1)*55,(y+1)*55-40)
				
		else:
			for i in range(-1,2):
				current_spot = map[player.y_pos+1][player.x_pos+i]
				
				if current_spot == 2:
					img = wall_sprite
				if current_spot == 1:
					img = floor_sprite
				if current_spot == 0:
					img = chest_sprite
				
				drawImage(img,(player.x_pos+2)*55,(player.y_pos+i+1)*55-40)
			
			
	setColor(get_color(player.color))
	rect ((player.x_pos+1)*55,(player.y_pos+1)*55-40,50,50)
	
	
def path_find (grid,player,x_final,y_final,sleep_time = 0.5):
	if (player.y_pos < y_final):

		if valid_move(grid,player,"s"):
			sleep(sleep_time)
			player.move("s")
			draw_map(grid,player)
			path_find(grid,player,x_final,y_final)
			return False
		else:
			sleep(sleep_time)
			player.move("d")
			draw_map(grid,player)
			path_find(grid,player,x_final,y_final)
			return False
	if (player.y_pos > y_final):
		if valid_move(grid,player,"w"):
			sleep(sleep_time)
			player.move("w")
			draw_map(grid,player)
			path_find(grid,player,x_final,y_final)
			return False
		else:
			sleep(sleep_time)
			player.move("d")
			draw_map(grid,player)
			path_find(grid,player,x_final,y_final)
			return False
	
	if (player.x_pos < x_final and player.y_pos == y_final):
		if valid_move(grid,player,"d"):
			sleep(sleep_time)
			player.move("d")
			draw_map(grid,player)
			path_find(grid,player,x_final,y_final)
			return False
	if (player.x_pos > x_final and player.y_pos == y_final):
		if valid_move(grid,player,"a"):
			sleep(sleep_time)
			player.move("a")
			draw_map(grid,player)
			path_find(grid,player,x_final,y_final)
			return False
	if (player.y_pos == y_final and player.x_pos == x_final):
		return False
		
def path_find_help(maze,p,x,y):
	while path_find(maze,p,x,y):
		draw_map(maze,p)

def main():
	resize(800,800)
	maze = create_grid(11,11)
	
	
	maze2 = [
			 [2,2,2,2,2,2,2,2,2,2,2,2],
			 [2,1,1,1,1,1,1,1,1,1,1,2],
			 [2,1,2,1,1,1,1,2,1,1,1,2],
			 [2,2,2,1,2,2,2,2,2,2,1,2],
			 [2,1,2,1,2,1,1,1,2,1,1,2],
			 [2,1,2,1,2,1,1,1,2,1,1,2],
			 [2,1,2,2,2,2,1,1,2,1,1,2],
			 [2,1,2,1,1,1,1,1,2,2,1,2],
			 [2,0,2,1,1,1,1,1,1,1,1,2],
			 [2,1,2,1,1,1,1,1,1,1,1,2],
			 [2,1,1,1,1,1,1,1,1,1,1,2],
			 [2,2,2,2,2,2,2,2,2,2,2,2]
			 ]
	
	
	
	
	rows = []
	columns = []
	memory_cache = [rows,columns]
	
	
	#create_path(maze,0,0,10,10)
	#create_path(maze,0,10,10,0)
	#create_path(maze,5,5,10,5)
	#create_path(maze,0,2,10,6)
	#create_path(maze,5,5,5,1)
	#create_path(maze,0,0,0,10)
	
	
	
	p = Player()
	p.x_pos = 1
	p.y_pos = 1
	p.color = 4
	
	setAutoUpdate(False)
	draw_map(maze2,p)
	
	
	
	
	while not closed():
		
		keys = list ( getHeldKeys() )
		input = ""
		if keys:
			input = keys[0]
		if input and valid_move(maze2,p,input):
			
			
			p.move(input)
				
		
			update_map(maze2 , p)
			update()
			sleep(0.2)
	
	#path_find_help(maze,p,5,5)
	
	
if __name__ == "__main__":
	main()
	
	