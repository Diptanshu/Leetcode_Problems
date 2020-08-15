# push the box 
	
	
# x b p
# x - |


# push constraints 
# (x,y) (x,y+1)
# 

# Question 1: In which direction should I be moving my box to?

# It won't add in the first place.

# Q 2. Maybe the question is about pushing the box 

# By the time it would have come and pushed the box; that state was already visited.

# (player state space, box state space)


# (box push, player state adj to box push);  (box state space same, remaining player state spaces)

# visited state spaces v/s non visited state spaces. maybe the visited state space is some unique combination of (box state space, player state space)

# box  <-  player

#  (x-1,y-1)  | (x-1,y)	 |  (x-1,y+1)
#-------------------------------------
#   (x,y-1)   | (x,y) box   |  (x,y+1)
#-------------------------------------
# (x+1,y-1)   | (x+1,y)	 |  (x+1,y+1)


# What is the time and space complexity?


from collections import defaultdict
from collections import deque

class Solution(object):
    def minPushBox(self, grid):
    	# Not the correct Solution
    	# Needs Improvement
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return self.constrained_bfs(grid)
    
    def check_valid_pos(self, grid, x, y):
        row_len = len(grid)
        col_len = len(grid[0])
        if 0 <= x < row_len and 0 <= y < col_len:
            return True
        return False
    
    def make_pairs(self, grid):
        row = len(grid)
        col = len(grid[0])
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == "T":
                    target_loc = (i,j)
                    continue
                elif grid[i][j] == "B":
                    box_loc = (i,j)
                    continue
                elif grid[i][j] ==  "S":
                    player_loc = (i,j)
                    continue
        return (target_loc, box_loc, player_loc)
    
    def box_push_directions(self, grid, box_x, box_y, player_x, player_y):
        # Assumption is that box and player can never be at the same coordinates
        row_len = len(grid)
        col_len = len(grid[0])
        if box_x == player_x:
        	if box_y - 1 == player_y:
        		if self.check_valid_pos(grid, box_x, box_y+1):
        			if grid[box_x][box_y+1] != "#":
        				return (0,1)
        	elif box_y + 1 == player_y:
        		if self.check_valid_pos(grid, box_x, box_y-1):
        			if grid[box_x][box_y-1] != "#":
        				return (0,-1)
        elif box_y == player_y:
        	if box_x - 1 == player_x:
        		if self.check_valid_pos(grid, box_x+1, box_y):
        			if grid[box_x+1][box_y] != "#":
        				return (+1,0)
        	elif box_x + 1 == player_x:
        		if self.check_valid_pos(grid, box_x-1, box_y):
        			if grid[box_x-1][box_y] != "#":
        				return (-1,0)
        return (float("-inf"), float("-inf"))
    
    def constrained_bfs(self, grid, level=0):
        player_mov = [(-1,0), (1,0), (0,-1), (0,1)]  # Player direction 
        visited_set = set()
        target_loc, box_loc, player_loc = self.make_pairs(grid)
        state_space = box_loc + player_loc
        queue_dict = defaultdict(deque)
        visited_set.add(state_space)
        queue_dict[level].append(state_space)
        # while queue_dict is not empty:
        while queue_dict:
            if queue_dict[level]:
                search_space = queue_dict[level].popleft()
                box_x, box_y = search_space[0], search_space[1]
                player_x, player_y = search_space[2], search_space[3]
                delta_x, delta_y = self.box_push_directions(grid, box_x, box_y, player_x, player_y)
                if grid[box_x][box_y] == "T":
                    # Termination Condition
                    return level # return the minimum number of steps
                else:
                	for x,y in player_mov:
                		if delta_x != x and delta_y != y:
                			new_player_x = player_x + x
                			new_player_y = player_y + y
                			if self.check_valid_pos(grid, new_player_x, new_player_y):
                				if not((grid[new_player_x][new_player_y] == "T") or (grid[new_player_x][new_player_y] == "#") or ((new_player_x == box_x) and (new_player_y == box_y))):
                					new_state_space = (box_x, box_y) + (new_player_x, new_player_y)
                					if new_state_space not in visited_set:
                						queue_dict[level].append(new_state_space)
                						visited_set.add(new_state_space)
                	if delta_x != float("-inf") and delta_y != float("-inf"):
                		new_box_x = box_x + delta_x
                		new_box_y = box_y + delta_y
                		new_player_x, new_player_y = box_x, box_y
                		new_state_space = (new_box_x, new_box_y) + (new_player_x, new_player_y)
                		if new_state_space not in visited_set:
                			queue_dict[level+1].append(new_state_space)
                			visited_set.add(new_state_space)
            else:
            	queue_dict.pop(level)
            	level += 1
            	continue
    	return -1


if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    move_box_min_steps = Solution()
    grid = 	[  ["#","#","#","#","#","#"],
               ["#","T","#",".",".","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
    print move_box_min_steps.constrained_bfs(grid)
    









