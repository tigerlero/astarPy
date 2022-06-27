import heapq
#Define priority queue
class PriorityQueue:
    # initialization
    def __init__(self):
        self.elements = []
# clears the queue
    def empty(self):
        return len(self.elements) == 0

    # add new item to the queue
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    # getter
    def get(self):
        return heapq.heappop(self.elements)[1]
#Reconstruct agent's path to target
def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)  # optional
    path.reverse()  # optional
    return path
# heuristic distance calculation
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

#A*Star Search Algo
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    print("A*star cost so far: ",cost_so_far)
    return came_from, cost_so_far
