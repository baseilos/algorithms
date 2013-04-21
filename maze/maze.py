# A breadth-first search algorithm implementation
# Jozef Lang <developer@jozeflang.com>

import sys

class PythonSolver:
	FREE_SIGN = ' '
	PATH_SIGN = '.'
	WALL_SIGN = '#'
	START_SIGN = 'S'
	FINISH_SIGN = 'F'
	POSITION_NOT_VISITED = -1
	maze = [];
	path = []

	def read_maze(self):
		for line in sys.stdin:
			self.maze.append(list(line))

		self.path = [self.POSITION_NOT_VISITED for i in xrange(len(self.maze))]
		for i in xrange(len(self.path)):
			self.path[i] = [self.POSITION_NOT_VISITED for j in xrange(len(self.maze[i]))]

	def print_maze(self):
		for line in self.maze:
			sys.stdout.write(''.join(line))

	def print_maze_solved(self, start, end):
		pos = end
		while pos != start:
			if self.is_path(pos) and self.is_finish(pos) == False:
				self.set_maze_path(pos)
			pos = self.next_path(pos)
		self.print_maze()

	def print_path(self):
		for row in xrange(len(self.path)):
			row_str = ""
			for col in xrange(len(self.path[row])):
				row_str += '%3s' % self.path[row][col]
			print row_str

	def find_start_end(self):
		start = (-1,-1)
		end = (-1,-1)
		for line in range(len(self.maze)):
			for row in range(len(self.maze[line])):
				if self.maze[line][row] == self.START_SIGN:
					start = (line,row)
				if self.maze[line][row] == self.FINISH_SIGN:
					end = (line,row)
		return start, end

	def solve(self, start, end):
		self.set_path_value(start, 1)
		queue = [start]
		while len(queue) > 0:
			pos = queue.pop(0)
			if self.is_finish(pos):
				return True
			next = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]),(pos[0], pos[1]-1),(pos[0], pos[1]+1)]
			for p in next:
				if self.is_valid_position(p) and self.is_path(p) and self.is_visited(p) == False:
					queue.append(p)
					self.set_path_value(p, self.path_value(pos) + 1)
		return False

	def path_value(self, position):
		return self.path[position[0]][position[1]]

	def set_path_value(self, position, value):
		self.path[position[0]][position[1]] = value

	def is_path(self, position):
		return self.maze[position[0]][position[1]] == self.FREE_SIGN or self.maze[position[0]][position[1]] == self.FINISH_SIGN 

	def is_finish(self, position):
		return self.maze[position[0]][position[1]] == self.FINISH_SIGN		

	def is_visited(self, position):
		return self.path[position[0]][position[1]] != self.POSITION_NOT_VISITED

	def is_valid_position(self, position):
		return position[0] > 0  and position[0] < len(self.maze) and position[1] > 0 and position[1] < len(self.maze[position[0]])

	def set_maze_path(self, position):
		self.maze[position[0]][position[1]] = self.PATH_SIGN

	def next_path(self, position):
		choices = [(position[0]-1, position[1]), (position[0]+1, position[1]),(position[0], position[1]-1),(position[0], position[1]+1)]
		for choice in choices:
			if self.path_value(choice) == self.path_value(position) - 1:
				return choice
		return (-1, -1)

if __name__ == "__main__":
	solver = PythonSolver()
	solver.read_maze()
	start, end = solver.find_start_end()
	solver.solve(start, end)
	solver.print_maze_solved(start, end)