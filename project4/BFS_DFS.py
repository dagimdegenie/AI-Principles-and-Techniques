
from collections import deque
infinity = float('inf')   

class Graph: 
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed 
        self.graph = graph_dict  #
        
    def nodes(self):        
        return list(self.graph_dict.keys())  
    #
    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} --> {', '.join(neighbors)}")
    #
    def get(self, a, b=None):
        links = self.graph_dict.get(a) 
        if b is None:
            return links
    
       
class Problem: 
    def __init__(self, start, goal=None):
       self.start = start
       self.goal = goal

    def goal_test(self, state):
        return state == self.goal
    
    def actions(self, state):
         raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError
            
    def value(self, state):
        raise NotImplementedError
  
   
class GraphProblem(Problem):  
    def __init__(self, start, goal, graph):
        Problem.__init__(self, start, goal)
        self.graph = graph
        
    def actions(self, A):        
        return self.graph.get(A)
    
    def result(self, state, action):
        return action

class Node: 
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action 
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
            
    def __repr__(self): 
        return "<Node "+ self.state + ">"
    
    def expand(self, problem): 
        children = []
        for action in problem.actions(self.state):
            x = self.child_node(problem,action)
            children.append(x)
        return children
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action )
        return next_node  
    
    def path(self): 
        node, path_back = self, []
        while node: 
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back)) 
    
    def solution(self): 
        return [node.state for node in self.path()]


visit_ethiopia = Graph(dict( {'Addis Ababa': {'Adama', 'Ambo', 'Debre Berhan'},
             'Adama': {'Matahara', 'Asella', 'Batu', 'Addis Ababa'}, 
             'Ambo': {'Wolkite', 'Addis Ababa', 'Nekemte'}, 
             'Debre Berhan': {'Addis Ababa', 'Debre Sina'}, 
             'Matahara': {'Adama', 'Awash'}, 
             'Asella': {'Adama', 'Assasa'}, 
             'Batu': {'Adama', 'Buta Jirra', 'Shashamene'}, 
             'Wolkite': {'Ambo', 'Worabe', 'Jimma'}, 
             'Nekemte': {'Ambo', 'Bedelle', 'Gimbi'}, 
             'Debre Sina': {'Debre Berhan', 'Kemise', 'Debre Markos'}, 
             'Awash': {'Chiro', 'Gobi Rasu', 'Matahara'}, 
             'Assasa': {'Asella', 'Dodolla'}, 
             'Buta Jirra': {'Batu', 'Worabe'}, 
             'Shashamene': {'Batu', 'Hawassa', 'Dodolla', 'Hossana'}, 
             'Worabe': {'Wolkite', 'Hossana', 'Buta Jirra'}, 
             'Jimma': {'Wolkite', 'Bonga', 'Bedelle'}, 
            'Bedelle': {'Nekemte', 'Gore', 'Jimma'}, 
             'Gimbi': {'Nekemte', 'Dambidollo'}, 
             'Kemise': {'Debre Sina', 'Dessie'}, 
             'Debre Markos': {'Debre Sina', 'Finote Selam'},
             'Chiro': {'Awash', 'Dire Dawa'}, 
             'Gobi Rasu': {'Awash', 'Samara'}, 
             'Dodolla': {'Assasa', 'Shashamene', 'Bale'}, 
             'Hawassa': {'Shashamene', 'Dilla'}, 
             'Hossana': {'Shashamene', 'Worabe', 'Wolaita Sodo'}, 
             'Bonga': {'Jimma', 'Dawro', 'Tepi', 'Mizan Teferi'}, 
             'Gore': {'Tepi', 'Gambella', 'Bedelle'}, 
             'Dambidollo': {'Gimbi', 'Assosa', 'Gambella'}, 
            'Dessie': {'Kemise', 'Woldia'}, 
            'Finote Selam': {'Debre Markos', 'Bahirdar', 'Injibara'}, 
             'Dire Dawa': { 'Chiro', 'Harar'}, 
             'Samara': { 'Gobi Rasu', 'Fanti Rasu', 'Alamata', 'Woldia'},
            'Bale': {'Liben', 'Dodolla', 'Goba', 'Sof Oumer'}, 
             'Dilla': {'Hawassa', 'Bulehora'}, 
             'Wolaita Sodo': {'Arba Minchi', 'Dawro', 'Hossana'}, 
             'Dawro': { 'Bonga', 'Basketo', 'Wolaita Sodo'}, 
             'Tepi': {'Gore', 'Bonga', 'Mizan Teferi'}, 
            'Mizan Teferi': {'Tepi', 'Bonga', 'Basketo'}, 
             'Gambella': {'Gore', 'Dambidollo'}, 
             'Assosa': {'Dambidollo', 'Metekel'}, 
            'Woldia': {'Dessie', 'Lalibella', 'Samara', 'Alamata'},
             'Bahirdar': {'Finote Selam', 'Injibara', 'Metekel', 'Azezo', 'Debre Tabor'}, 
             'Injibara': {'Bahirdar', 'Finote Selam'}, 
             'Harar': { 'Dire Dawa', 'Babile'}, 
             'Fanti Rasu': {'Samara', 'Kilbet Rasu'}, 
             'Alamata': {'Samara', 'Woldia', 'Mekelle', 'Sekota'}, 
             'Liben': {'Bale'}, 
             'Goba': {'Bale', 'Sof Oumer', 'Dega Habur'}, 
             'Sof Oumer': {'Goba', 'Bale', 'Kebri Dehar'}, 
            'Bulehora': { 'Dilla', 'Yabello'}, 
            'Arba Minchi': {'Wolaita Sodo', 'Konso', 'Basketo'}, 
             'Basketo': { 'Arba Minchi', 'Dawro', 'Mizan Teferi', 'Benchi Maji'}, 
             'Metekel': { 'Assosa', 'Bahirdar'},
             'Lalibella': {'Woldia', 'Debre Tabor', 'Sekota'},
             'Debre Tabor': {'Lalibella', 'Bahirdar'}, 
             'Azezo': {'Gondar', 'Bahirdar', 'Metema'}, 
             'Babile': { 'Harar', 'Jigjiga'}, 
             'Kilbet Rasu': {'Fanti Rasu' }, 
             'Mekelle': {'Alamata', 'Adwa', 'Adigrat', 'Sekota'}, 
             'Sekota': {'Alamata', 'Mekelle', 'Lalibella'}, 
            'Dega Habur': {'Goba', 'Jigjiga', 'Kebri Dehar'}, 
            'Kebri Dehar': {'Gode', 'Sof Oumer', 'Dega Habur', 'Werdez'}, 
            'Yabello': { 'Bulehora', 'Konso', 'Moyale'}, 
            'Konso': {'Arba Minchi', 'Yabello'}, 
            'Benchi Maji': { 'Basketo'}, 
            'Gondar': { 'Azezo', 'Metema', 'Debarke'},
            'Metema': { 'Azezo', 'Gondar'},  
            'Jigjiga': { 'Babile', 'Dega Habur'}, 
            'Adwa': { 'Mekelle', 'Axum', 'Adigrat'},
            'Adigrat': { 'Mekelle', 'Adwa'},
            'Axum': { 'Adwa'},
            'Gode': { 'Kebri Dehar', 'Werdez'}, 
            'Werdez': { 'Kebri Dehar', 'Gode'},
            'Moyale': { 'Yabello'} }))

print('\n solution for problem 1.1 \n')             
visit_ethiopia.print_graph()

print("\nNodes in graphs are :\n\n", visit_ethiopia.nodes())

print('\n solution for problem 1.2 \n BFS & DFS strategy \n')

# BFS strategy

def BFS(problem): 
    node = Node(problem.start)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None


# input from the user
start_city = input("Enter the starting city: ")
goal_city = input("Enter the destination: ")

print("\n successors of ", start_city, "are :", visit_ethiopia.get(start_city))

# Create the problem instance
visit_ethiopia_problem = GraphProblem(start_city, goal_city, visit_ethiopia)


print("\n\n Performing BFS strategy from ", start_city, "to", goal_city, ":\n")
finalnode = BFS(visit_ethiopia_problem)
if finalnode is not None:
    print("Possible path", visit_ethiopia_problem.start, "to", visit_ethiopia_problem.goal, finalnode.solution())
else:
    print("Path does not exist.")


# DFS strategies

def DFS(problem):
   
    frontier = [(Node(problem.start))]
    explored = set()
    
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None


print("\n\n\n Performing DFS strategy from", start_city, "to", goal_city, ":\n")
finalnode = BFS(visit_ethiopia_problem)
if finalnode is not None:
    print("Possible path", visit_ethiopia_problem.start, "to", visit_ethiopia_problem.goal, finalnode.solution())
else:
    print("Path does not exist.")