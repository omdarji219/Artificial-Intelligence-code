from collections import deque
def is_goal(state, target):
return target in state
def get_next_states(state, A, B):
x, y = state
next_states = set()
# Fill jug1
next_states.add((A, y))
# Fill jug2
next_states.add((x, B))
next_states.add((0, y))
next_states.add((x, 0))
transfer = min(x, B - y)
next_states.add((x - transfer, y + transfer))
transfer = min(y, A - x)
next_states.add((x + transfer, y - transfer))
return next_states
def bfs_water_jug(A, B, target):
start = (0, 0)
queue = deque()
queue.append((start, [start]))
visited = set()
visited.add(start)
while queue:
current, path = queue.popleft()
if is_goal(current, target):
return path
for next_state in get_next_states(current, A, B):
if next_state not in visited:
visited.add(next_state)
queue.append((next_state, path + [next_state]))
return None
A = int(input("Enter capacity of Jug 1: "))
Enrolment Number (2201202022) 2
B = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target volume: "))
result = bfs_water_jug(A, B, target)
if result:
print("Solution path:")
for step in result:
print(step)
else:
print("No solution possible.")