def display(grid):
	for y in grid:
		for x in y:
			print(x + " ",end="")
		print("")

#(x1,y1) starting position, (x2,y2) ending position
def findPath(grid, solid, x1, y1, x2, y2):
	xDim = len(grid[0])
	yDim = len(grid)
	nodes = []
	row = []
	for y in range(yDim):
		row.append(".")
	for x in range(xDim):
		nodes.append([])
		nodes[x] = row.copy()
	
	nodes[y2][x2] = "END"#START NODE
	'''LEGEND FOR NODE GRID
	  '. Nothing
	  'L means left
	  'R right
	  'U up
	  'D down
	  'LO left open
	  'RO right open
	  'UO up open
	  'DO down open
	'''
	
	#Create nodes
	closed = ["U", "D", "L", "R", "END"]
	if (grid[y1][x1] in solid):
		return None
	while(nodes[y1][x1] == "."):
		display(nodes)##################################################
		for y in range(1,yDim-1):#1 and dim-1 so it doesn't go out of range. This means this function won't work if the path must go to the edge of the grid
			for x in range(1,xDim-1):
				if(grid[y][x] not in solid and nodes[y][x] not in closed):
					if(nodes[y-1][x] in closed): #Length to make sure it is open
						nodes[y][x] = "UO"
					elif(nodes[y+1][x] in closed): #Length to make sure it is open
						nodes[y][x] = "DO"
					elif(nodes[y][x-1] in closed): #Length to make sure it is open
						nodes[y][x] = "LO"
					elif(nodes[y][x+1] in closed): #Length to make sure it is open
						nodes[y][x] = "RO"

		#Close nodes
		terminate = True
		for y in range(yDim):
			for x in range(xDim):
				if(len(nodes[y][x]) == 2): #this does not modify the end value because it is 3 characters long
					nodes[y][x] = nodes[y][x][0]
					terminate = False
		#end function if no new nodes were created
		if(terminate):
			return None
		
	#Make path to end
	pathX = x1
	pathY = x1
	path = []
	for i in nodes:
		print(i)
	while(nodes[pathY][pathX] != "END"):
		#print(path)
		path.append(nodes[pathY][pathX])
		if(nodes[pathY][pathX] == "U"):
			pathY -= 1
		elif(nodes[pathY][pathX] == "D"):
			pathY += 1
		elif(nodes[pathY][pathX] == "L"):
			pathX -= 1
		elif(nodes[pathY][pathX] == "R"):
			pathX += 1

	return path


