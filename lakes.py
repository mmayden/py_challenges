#https://www.algoexpert.io/questions/River%20Sizes
'''
You are given a 2D array (matrix) of potentially unequal height and width containing
only 0s and 1s. Each 0 represents land, and each 1 represents part of a lake.
A lake consists of any number of 1s that are either horizontally or vertically
adjacent (but not diagonally). The number of adjacent 1s forming a lake determine its size.
Write a function that returns an array of the sizes of all lakes represented in the input matrix.
Note that these sizes do not need to be in any particular order.
'''
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
        self.adj_coord = adj_coord
        self.size = len(self.adj_coord)
    def update_Size(self):
        size = len(self.adj_coord)
    def print_adj(self):
        print (self.adj_coord)
    def get_adj(self):
        return (self.adj_coord)
    def set_adj(self, new_coord):
        self.adj_coord.append(new_coord)

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
        x = -1    #As we transition to the next y axis (next row) we must reset our x axis
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
    delete = []
    
    for possibility in adjacency:
        if ((not(possibility in coordinates))):
             delete.append(possibility)
        if (coordinates.get(possibility) is 0):
             delete.append(possibility)
    
    for d in delete:
        adjacency.remove(d)
    print (adjacency)
    return adjacency
    


#Check a coordinate for adjacency with it's 4 non-diagonal neighbors
def adj_Check(coord_checking):

    #Possibilities represents a string of 2-4 sets of coordinates
    #these coordinates are the coordinates for elements adjacent to our input 
    #List is created from the function, adjacent(), which returns all adjacent coords
    adjacent_coords = adjacent(coord_checking)
    print ('coord we are checking: {}'.format(coord_checking))
    
    if (len(lakes) is 0):
        lakes.append(Lake(adjacent_coords))
        lakes[0].adj_coord.append(coord_checking)
    else:
        add = False
        print ('Number of lakes: %s ' % (len(lakes)))
        for lake in lakes:
            for x in adjacent_coords:
                if not(len(adjacent_coords) is 0):
                    if (not(x in lake.get_adj())):
                        add = True
        if add is True:
            lakes.append(Lake(adjacent_coords))
            lakes[len(lakes)-1].set_adj(adjacent_coords)
            lakes[len(lakes)-1].set_adj(coord_checking)
        for lake in lakes:
            print ('Hey here are some lakes: '.format(lake.get_adj()))

#Main loop
def run():
    make_Grid_Tangible(grid_input)    #First make the input grid tangible
    print(coordinates)

    #Then loop through all coordinates and check for adjacency
    for coord in coordinates:    
        if not (coordinates[coord] == 0):
            adj_Check(coord)

    update_Lakes()

    print ('There are %s total lakes!\nHere are the sizes:\n' % (len(lakes)))
    for lake in lakes:
        print ('Size of Lake [%s]: %s' % (lake, lake.size))
run()
