#input
grid_input = [                 
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
]

#Dictionary for representing a set of key values
#keys representing the coordinates for 1s and 0s in (x, y) form
#values of keys represent whether the coordinate holds a 1 or 0
coordinates = {}

#list containing Lake objects which represent groups of adjacent 1s
lakes = []



class Lake:
    'Lake object to represent a group of adjacent 1s'
    def __init__(self, adj_coord):
        self.adj_coords = adj_coord
        self.size = len(self.adj_coords)

    def update_Size(self):
        size = len(self.adj_coords)


def update_Lakes():
    for lake in lakes:
        lake.update_Size()

#Make the gridinput tangible by creating a dictionary with accessible coordinates
def make_Grid_Tangible(original_input):
    
    #Starting coordinates 
    y = -1
    x = -1
    #begin looping through every element from gridinput
    for each_element in original_input:
        y+=1    #This value represents current y axis (which row) we are working wit
        for b in each_element:
            x+=1    #This value represents current x axis (which col) we are working wit
            coordinates[(x, y)] = b;    #add a new key:value pair to the coords dictionary
        x=-1    #As we transition to the next y axis (next row) we must reset our x axis
    #as we are returning back to the 0th column of the grid



#Return a list of all adjacent coordinates
def adjacent(x):
    adjacency = []    #list that will be returned

    #Create all 4 possible adjacent coordinates and add to possible_adjacency
    while (True):
        adjacency.append((x[0]-1, x[1]))    #LEFT
        adjacency.append((x[0]+1, x[1]))    #RIGHT
        adjacency.append((x[0], x[1]+1))    #UP
        adjacency.append((x[0], x[1]-1))    #DOWN
        break

    #For every coordinate in the list, remove those that do not exist in the coordinates dict
    for possibility in adjacency:
        if ((not(possibility in coordinates)) or (coordinates[possibility] == 0)):
            adjacency.remove(possibility)
    
    print (adjacency)
    return adjacency
    


#Check a coordinate for adjacency with it's 4 non-diagonal neighbors
def adj_Check(coord_checking):

    #Possibilities represents a string of 2-4 sets of coordinates
    #these coordinates are the coordinates for elements adjacent to our input 
    #List is created from the function, adjacent(), which returns all adjacent coords
    adjacent_coords = adjacent(coord_checking)
    #print (adjacent_coords)
    
    if (len(lakes) is 0):
        lakes.append(Lake(adjacent_coords))
        lakes[0].adj_coords.append(coord_checking)
    else:
        for lake in lakes:
            for x in adjacent_coords:
                if x in lake.adj_coords:
                    lake.adj_coords.append(x)
                

#Main loop
def run():
    make_Grid_Tangible(grid_input)    #First make the input grid tangible
    
    #Then loop through all coordinates and check for adjacency
    for coord in coordinates:    
        if not (coordinates[coord] == 0):
            adj_Check(coord)

    update_Lakes()

    print ('There are %s total lakes!\nHere are the sizes:\n' % (len(lakes)))
    for lake in lakes:
        print ('Size of Lake [%s]: %s' % (lake, lake.size))
run()
