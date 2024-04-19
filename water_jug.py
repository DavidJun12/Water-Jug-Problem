from collections import deque


def BFS(a, b, target):

	m = {}      #dictionary that keeps track of visitd states
	isSolvable = False   # bolean to indicate if a solution is found
	path = []   # store the solution path


	q = deque()    # deque to store the states to be explored

	q.append((0, 0))

	while (len(q) > 0):
		u = q.popleft() # If this state is already visited
		if ((u[0], u[1]) in m):             # if u has been visited, continue to the next iteration
			continue
		if ((u[0] > a or u[1] > b or         # if u is out of bounds continue to the next iteration
			u[0] < 0 or u[1] < 0)):
			continue

		# Filling the vector for constructing
		# the solution path
		path.append([u[0], u[1]])      # append u to solution path

		# Marking current state as visited
		m[(u[0], u[1])] = 1               # mark u as visited

		# If we reach solution state, put ans=1
		if (u[0] == target or u[1] == target):				# if current u state represents the target amount
			isSolvable = True

			if (u[0] == target):    					  # if  jug 1 contains requred amt 
				if (u[1] != 0):

					# Fill final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					# Fill final state
					path.append([0, u[1]])

			# Print the solution path
			sz = len(path)      #number of states in the solution path
			for i in range(sz):         #iterate through each state and print it
				print("(", path[i][0], ",",
					path[i][1], ")")
			break

		# If we have not reached final state
		# then, start developing intermediate
		# states to reach solution state
		q.append([u[0], b]) # Fill Jug2
		q.append([a, u[1]]) # Fill Jug1

		for ap in range(max(a, b) + 1):

			# Pour amount ap from Jug2 to Jug1
			c = u[0] + ap    #amt of water in jug 1 after pouring ap
			d = u[1] - ap

			# Check if this state is possible or not
			if (c == a or (d == 0 and d >= 0)):       # checks if pouring amt from jug 1 to jug 2 results in a valid state
				q.append([c, d])

			# Pour amount ap from Jug 1 to Jug2
			c = u[0] - ap
			d = u[1] + ap

			# Check if this state is possible or not
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])       #append new state

		# Empty Jug2
		q.append([a, 0])

		# Empty Jug1
		q.append([0, b])

	# No, solution exists if ans=0
	if (not isSolvable):
		print("No solution")


# Driver code
if __name__ == '__main__':

	Jug1, Jug2, target = 4, 3, 2

	print("Path from initial state "
		"to solution state ::")

	BFS(Jug1, Jug2, target)
