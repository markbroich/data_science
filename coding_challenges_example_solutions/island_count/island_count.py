# You are tasked with counting the number of islands in a 2D matrix / grid.
# Islands are represented by 1s, oceans by 0. If the 1s are connected, 
# then they count as one island. You can assume a grid has a limited 
# size up to 10x10. Try to make the search / count of number 
# of islands as efficient as possible. If no islands are found, just return 0.

        
# The goal is to find how many islands there are in the ocean, 
# regardless of its size.


# assuming:
# -a square grid
# -islands are only connected horizontally and vertically but not diagionally

# e.g. 
# grid = [[1, 0, 0],
#         [1, 0, 1],
#         [0, 1, 0]]
# the correct answer here 3 islands

# time O(columns * rows)
# explantation: time O() is proportional to the total graph's number of visited nodes and edges. 
# In that case, there are columns * rows nodes and slightly less than 4 * columns * rows edges, their sum is still O(columns * rows).
# so O(n)

# Why? b/c we call each edge exactly once in each direction (even if the call returns right away)

# space O(1) + call stack which is up to 
# columns * rows in the worth case 

def count_islands(grid):
    counter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            # if island found, count it 
            # and turn it to water
            if grid[i][j] == 1:
                counter += 1
                grid = make_water(grid, i, j)
    return counter

# recursively set to water all parts of an island to 
# avoid double counting 
# death first search approach
def make_water(grid, i, j):
    if grid[i][j] == 0:
        return grid
    else:
        # eliminate the island cell  
        grid[i][j] = 0
        # eliminate all adjacent island 
        # cells via recursion
        if loc_allowed(i-1, j, grid):
            grid = make_water(grid, i-1, j)
        if loc_allowed(i+1,j, grid):
            grid = make_water(grid, i+1, j)
        if loc_allowed(i,j-1, grid):
            grid = make_water(grid, i, j-1)
        if loc_allowed(i,j+1, grid):
            grid = make_water(grid, i, j+1)
        return grid

# check of cell is within the grid
def loc_allowed(i, j, grid):
    if i >= 0 and i < len(grid)\
    and j >= 0 and j < len(grid):
        return True
    return False


###### Example 1
grid = [[1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]
# expected: 4 islands
# (top left island has size 5; top right = 2, bottom left = 2, bottom right = 1)

print(count_islands(grid), " islands found")
print("")


###### Example 2
grid = [[1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]]

print(count_islands(grid), " islands found")
print("")


###### Example 3
grid = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

print(count_islands(grid), " islands found")
print("")


###### Example 4
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print(count_islands(grid), " islands found")
print("")


#### island count using a stack
def get_number_of_islands_loop(binaryMatrix):
  cnt = 0
  cLen = len(binaryMatrix[0])
  rLen = len(binaryMatrix)
  if rLen == 1 and cLen	 == 1:
    if binaryMatrix[0][0] == 1:
      return 1
    else: 
      return cnt
  #
  stack = []   
  for x in range(0,cLen):
    for y in range(0,rLen):
      if binaryMatrix[y][x] == 1:
        cnt += 1
        stack.append((x,y))
        while stack:
            x, y = stack.pop(0)
            binaryMatrix[y][x] = 0
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                if is_valid(x+i,y+j,cLen,rLen):
                    if binaryMatrix[y+j][x+i] == 1:
                        stack.append((x+i,y+j))
  return cnt

def is_valid(x,y,cLen,rLen):
    if (y < 0 or y >= rLen  
        or x < 0 or x >= cLen):
        return False
    return True    

###
# also in a loop bus using a dict so 
# Os(count of island cells)
def island_count_loop_dict(grid):
    landSet = pop_land_set(grid)
    #
    islandCnt = 0
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            if (r,c) in landSet:
                islandCnt +=1
                stack = [(r,c)]
                dfs(stack,landSet)
    return islandCnt

def dfs(stack,landSet):
    while stack:
        r,c = stack.pop()
        if (r,c) in landSet:
            landSet.remove((r,c))
            for rx, cx in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (r+rx,c+cx) in landSet:
                    stack.append((r+rx,c+cx))
    # print('island explored')

def pop_land_set(grid):
    landSet = set()
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == 1:
                landSet.add((r,c))
    return landSet



def testing():
    binaryMatrix =[[0]]
    exp = 0
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)
    binaryMatrix = [[1]]
    exp = 1
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)
    binaryMatrix = [[1,0,1,0]]
    exp = 2
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)
    binaryMatrix = [[1,0,1,0],[0,1,1,1],[0,0,1,0]]
    exp = 2
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)
    binaryMatrix = [[1,0,1,0],[0,1,1,1],[0,0,1,0],[1,1,0,0],[0,1,0,1]]
    exp = 4
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)    
    binaryMatrix = [[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1]]
    exp = 6
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)
    binaryMatrix = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    exp = 1
    print(island_count_loop_dict(binaryMatrix) == exp)
    print(get_number_of_islands_loop(binaryMatrix) == exp)
        

testing()


# solved again w slightly different approach. 

# just to recall: 
# time O(columns * rows)
# explantation: time O() is proportional to the total graph's number of visited nodes and edges. 
# In that case, there are columns * rows nodes and slightly less than 4 * columns * rows edges, their sum is still O(columns * rows).
# so O(n)

## X cluster counter
# 
# given an array with X and O as e.g. below:
# find the number of Xs that are either part 
# of a cluster or on their own. 
#
# [["O","O","O","X","O","O","O"]
#  ["O","X","O","O","O","X","O"], 
#  ["O","X","O","O","O","X","O"]]

# A cluster is defined as adjacent Xs in 
# horizontal or vertical direction
# own. Clusters w multiple members are 
# flagged for illustation 
# w '.' below. 

# [["O","O", "O", "X","O","O", "O"]
#  ["O","O", "O", "O","O","X.","O"], 
#  ["O","X.","X.","O","O","X.","O"]]

# the counter of all clusters in this example is: 3

class XClusterCounter:
	# @param A : list of strings
	# @return an integer
    def __init__(self):
        self._myDict = {}
        self._counter = 0

    def __explore_adj(self, A, i, j):
        # flag as visited
        self._myDict[(i,j)] = "T"
        #
        # left
        if j-1 >= 0: 
            if A[i][j-1] =='X' and not (i,j-1) in self._myDict:
                self.__explore_adj(A, i,j-1)
        # right
        if j+1 <= (len(A[i])-1):
            if A[i][j+1] =='X' and not (i,j+1) in self._myDict:
                self.__explore_adj(A, i,j+1)
        # above
        if i-1 >= 0:
            if A[i-1][j] =='X' and not (i-1,j) in self._myDict:
                self.__explore_adj(A, i-1,j)
        # below
        if i+1 <= len(A)-1:
            if A[i+1][j] =='X' and not (i+1,j) in self._myDict: 
                self.__explore_adj(A, i+1,j)

    def counter(self,A):
        #
        # loop over each list and each cell within list
        for i in range(0,len(A)):
                for j in range(0,len(A[i])):
                    if A[i][j] == 'X' and not (i,j) in self._myDict:
                        # new island found
                        self._counter += 1
                        # look for adjacent
                        self.__explore_adj(A, i, j)
        return self._counter
        


        
# ["O","O","O","X","O","O","O"]
# ["O","X","O","O","O","X","O"], 
# ["O","X","O","O","O","X","O"] 

A = [ ["O","O","O","X","O","O","O"], ["O","X","O","O","O","X","O"], ["O","X","O","O","O","X","O"] ]
XC1 = XClusterCounter()
print(XC1.counter(A))



# island count revised: 

# using either recursion or stack and while loop
def count_islands(grid, rec=True):
    iCnt = 0
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            if grid[r][c] == 1:
                iCnt += 1
                if rec: 
                    grid = dfs_rec(grid, r, c)
                else:
                    grid = dfs(grid, r, c)
    return iCnt

def dfs(grid, r, c):
    grid[r][c] = 0 # sink
    stack = [(r, c)]
    neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        r, c = stack.pop()
        for rm, cm in neigh:
            r_, c_ = r+rm, c+cm
            if (r_ >= 0 and r_ < len(grid) and
               c_ >= 0 and c_ < len(grid[0])):
                if grid[r_][c_] == 1:
                    stack.append((c_, r_))
                    grid[r_][c_] = 0 # sink
    return grid

def dfs_rec(grid, r, c):
    if grid[r][c] == 0:
        return grid
    grid[r][c] = 0 # sink
    neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for rm, cm in neigh:
        r_, c_ = r+rm, c+cm
        if (r_ >= 0 and r_ < len(grid) and
            c_ >= 0 and c_ < len(grid[0])):
            if grid[r_][c_] == 1:
                grid = dfs_rec(grid, r_, c_)
    return grid

# using recursion
# ###### Example 1
grid = [[1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]
# expected: 4 islands
# (top left island has size 5; top right = 2, bottom left = 2, bottom right = 1)
print(count_islands(grid) == 4)

###### Example 2
grid = [[1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]]
print(count_islands(grid) == 6)

###### Example 3
grid = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
print(count_islands(grid) == 1)

###### Example 4
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
print(count_islands(grid) == 0)
print()

# using loop
# ###### Example 1
grid = [[1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]
# expected: 4 islands
# (top left island has size 5; top right = 2, bottom left = 2, bottom right = 1)
print(count_islands(grid, False) == 4)

###### Example 2
grid = [[1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]]
print(count_islands(grid, False) == 6)

###### Example 3
grid = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
print(count_islands(grid, False) == 1)

###### Example 4
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
print(count_islands(grid, False) == 0)