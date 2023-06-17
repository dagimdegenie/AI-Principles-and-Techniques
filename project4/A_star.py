# the dict consists key, successors & path cost
travelling_cities = {'Addis Ababa': {'Adama':3, 'Ambo':5, 'Debre Berhan':5,'Debre Markos':13},
             'Adama': {'Matahara':3, 'Asella':4, 'Batu':4, 'Addis Ababa':3}, 
             'Ambo': {'Wolkite':6, 'Addis Ababa':5, 'Nekemte':8}, 
             'Debre Berhan': {'Addis Ababa':5, 'Debre Sina':2},
             'Debre Markos':{'Addis Ababa':13,'Debre Sina':17,'Finote Selam':3},
                               
             'Matahara': {'Adama':3, 'Awash':1}, 
             'Asella': {'Adama':4, 'Assasa':4}, 
             'Batu': {'Adama':4, 'Buta Jirra':2, 'Shashamene':3}, 
             'Wolkite': {'Ambo':6, 'Worabe':5, 'Jimma':8,'Hossana':5,'Buta Jirra':4}, 
             'Nekemte': {'Ambo':9, 'Bedelle':5, 'Gimbi':4}, 
             'Debre Sina': {'Debre Berhan':2, 'Kemise':7, 'Debre Markos':17}, 
             'Finote Selam': {'Debre Markos':3, 'Bahirdar':6, 'Injibara':2},
                               
             'Awash': {'Chiro':4, 'Gobi Rasu':5, 'Matahara':1}, 
             'Assasa': {'Asella':4, 'Dodolla':1}, 
             'Buta Jirra': {'Batu':2,'Wolkite':4, 'Worabe':2}, 
             'Shashamene': {'Batu':3,'Dodolla':3, 'Hawassa':1, 'Hossana':7,'Worabe':6}, 
             'Worabe': {'Wolkite':5, 'Hossana':2,'Shashamene':6, 'Buta Jirra':2}, 
             'Jimma': {'Wolkite':8, 'Bonga':4, 'Bedelle':7}, 
             'Hossana': {'Shashamene':7, 'Worabe':2, 'Wolkite':5, 'Wolaita Sodo':4}, 
             'Bedelle': {'Nekemte':5, 'Gore':6, 'Jimma':7}, 
             'Gimbi': {'Nekemte':4, 'Dambidollo':6,'Assosa':8}, 
             'Kemise': {'Debre Sina':6, 'Dessie':4}, 
             'Bahirdar': {'Finote Selam':6, 'Injibara':4, 'Metekel':11, 'Azezo':7, 'Debre Tabor':4},
             'Injibara': {'Bahirdar':4, 'Finote Selam':2},
                               
                               
             'Chiro': {'Awash':4, 'Dire Dawa':8}, 
             'Gobi Rasu': {'Awash':5, 'Samara':10}, 
             'Dodolla': {'Assasa':1, 'Shashamene':3, 'Robe':13}, 
             'Hawassa': {'Shashamene':1, 'Dilla':3}, 
             'Bonga': {'Jimma':4, 'Dawro':10, 'Tepi':8, 'Mizan Teferi':4}, 
             'Wolaita Sodo': {'Arba Minchi':4, 'Dawro':6, 'Hossana':4}, 
             'Gore': {'Tepi':9, 'Gambella':5, 'Bedelle':6}, 
             'Dambidollo': {'Gimbi':6, 'Assosa':12, 'Gambella':4}, 
             'Assosa': {'Gimbi':8, 'Dambidollo':12}, 
             'Dessie': {'Kemise':4, 'Woldia':6},
             'Metekel': { 'Bahirdar':11},
             'Azezo': {'Gondar':1, 'Bahirdar':7, 'Metema':7}, 
             'Debre Tabor': {'Lalibella':8, 'Gondar':6, 'Bahirdar':4},
             
             'Dire Dawa': { 'Chiro':8, 'Harar':4}, 
             'Samara': { 'Gobi Rasu':10, 'Fanti Rasu':7, 'Alamata':11, 'Woldia':8},
             'Robe': {'Liben':11, 'Dodolla':13, 'Goba':18, 'Sof Oumer':23}, 
             'Dilla': {'Hawassa':3, 'Bulehora':4}, 
             'Dawro': { 'Bonga':10, 'Wolaita Sodo':6}, 
             'Tepi': {'Gore':9, 'Bonga':8, 'Mizan Teferi':4}, 
             'Mizan Teferi': {'Tepi':4, 'Bonga':4}, 
             'Gambella': {'Gore':5, 'Dambidollo':4}, 
             'Arba Minchi': {'Wolaita Sodo':5, 'Konso':4, 'Basketo':10},
             'Woldia': {'Dessie':6, 'Lalibella':7, 'Samara':8, 'Alamata':3},
             'Gondar': { 'Azezo':1, 'Humera':9, 'Metema':7, 'Debarke':4,'Debre Tabor':6},
             'Metema': { 'Azezo':7, 'Gondar':7}, 
             'Lalibella': {'Woldia':7, 'Debre Tabor':8, 'Sekota':6},
              
              
             'Harar': { 'Dire Dawa':4, 'Babile':2}, 
             'Fanti Rasu': {'Samara':7, 'Kilbet Rasu':6}, 
             'Alamata': {'Samara':11, 'Woldia':3, 'Mekelle':5, 'Sekota':6}, 
             'Liben': {'Robe':11}, 
             'Goba': {'Robe':18, 'Sof Oumer':6, 'Babile':28}, 
             'Sof Oumer': {'Goba':6, 'Robe':23, 'Gode':23}, 
             'Bulehora': { 'Dilla':4, 'Yabello':3}, 
             'Konso': {'Arba Minchi':4, 'Yabello':3}, 
             'Basketo': { 'Arba Minchi':10, 'Bench Maji':5}, 
             'Humera': { 'Shire':8, 'Gondar':9},
             'Debarke': { 'Gondar':4, 'Shire':7},
             'Sekota': {'Alamata':6, 'Mekelle':9, 'Lalibella':6}, 
             
             'Babile': { 'Harar':2, 'Jigjiga':3,'Goba':28}, 
             'Kilbet Rasu': {'Fanti Rasu':6}, 
             'Mekelle': {'Alamata':5, 'Adigrat':4, 'Adwa':7, 'Sekota':9},
             'Gode': { 'Dollo':17, 'Kebri Dehar':5, 'Sof Oumer':23 }, 
             'Yabello': { 'Bulehora':3, 'Konso':3, 'Moyale':6},
             'Bench Maji': { 'Basketo':5}, 
             'Shire': { 'Axum':2, 'Humera':8, 'Debarke':7},
                               
             'Jigjiga': { 'Babile':3, 'Dega Habur':5}, 
             'Adigrat': { 'Mekelle':4, 'Adwa':4},
             'Adwa': { 'Mekelle':7, 'Axum':1, 'Adigrat':4},
             'Dollo':{'Gode':17,'Moyale':18},
             'Kebri Dehar': {'Gode':5, 'Dega Habur':6, 'Werdez':6}, 
             'Moyale': { 'Dollo':18,'Liben':11,'Yabello':6}, 
             'Axum': {'Shire':2, 'Adwa':1},
             'Dega Habur': {'Jigjiga':5, 'Kebri Dehar':6}, 
             'Werdez': { 'Kebri Dehar':6}
                      }

# the heuristic_costs dict consists key & heuristic cost
heuristic_costs = {
             'Addis Ababa':26,
             'Adama':23,
             'Ambo':31,
             'Debre Berhan':31,
             'Debre Markos':39,
             'Matahara':26,
             'Asella':22, 
             'Batu':19,  
             'Wolkite':25,  
             'Nekemte':39, 
             'Debre Sina':33,
             'Finote Selam':42,
             'Awash':27, 
             'Assasa':18, 
             'Buta Jirra':21, 
             'Shashamene':16, 
             'Worabe':22, 
             'Jimma':33,
             'Hossana':21,
             'Bedelle':40, 
             'Gimbi':43, 
             'Kemise':40,  
             'Bahirdar':48, 
             'Injibara':44,
                               
             'Chiro':31,
             'Gobi Rasu':32, 
    
              'Dodolla':19, 
             
              'Hawassa':15, 
             
              'Bonga':33,
              'Wolaita Sodo':17, 
              'Gore':46,  
              'Dambidollo':49,
              'Assosa':51, 
              'Dessie':44, 
              'Metekel':59, 
              'Azezo':55, 
              'Debre Tabor':52,
             
                               
                               
             'Dire Dawa':31, 
             'Samara':42, 
              'Robe':13, 
             'Dilla':12, 
             'Dawro':23, 
             'Tepi':41,
             'Mizan Teferi':37, 
             'Arba Minchi':13, 
             'Gambella':51,  
              
             
             'Woldia':50,
             'Gondar':56, 
             'Metema':62, 
             'Lalibella':57,
             
             'Harar':35, 
             'Fanti Rasu':49, 
             'Alamata':53, 
             'Liben':11, 
             'Goba':40, 
             'Sof Oumer':45, 
              'Bulehora':8, 
              
              'Konso':9, 
             'Basketo':23,
             'Bench Maji':28,
    
             
             'Humera':65, 
             'Debarke':60,
             
             'Sekota':59,
              
              
             'Babile':37, 
             'Kilbet Rasu':55, 
             'Mekelle':58, 
            
             
             'Gode':35, 
             'Yabello':6, 
             'Shire':67, 
             
             
             
            
              'Adigrat':62,
             'Adwa':65, 
              'Dollo':18,
             'Kebri Dehar':40, 
             'Moyale':0,
             
             'Axum':66, 
                               
             'Jigjiga':40,
             'Dega Habur':45, 
             
            
             
             'Kebri Dehar': 40,
             'Werdez':4
        }




# to create and manipulate priority queues
import heapq

def astar_search(graph, heuristic_costs, initial_state, goal_state):
    # Create a priority queue to store the states to be explored
    queue = []    # Create a dictionary to store the total cost from the initial state to each state
    total_cost = {}    # Create a dictionary to store the backward cost from the initial state to each state
    backward_cost = {}    # Create a dictionary to store the path from the initial state to each state
    path = {}

    total_cost[initial_state] = 0      # Initialize the cost of the initial state as 0
    backward_cost[initial_state] = 0   # Initialize the backward cost of the initial state as 0
    path[initial_state] = []           # Initialize the path of the initial state as empty

    # Push the initial state to the priority queue with a priority of 0 (total cost + heuristic cost)
    heapq.heappush(queue, (heuristic_costs[initial_state], initial_state))

    while queue:
        # Pop the state with the lowest priority from the priority queue
        current_priority, current_state = heapq.heappop(queue)
        
        if current_state == goal_state:
            print(f"Total | optimal cost: {backward_cost[current_state]}")
            return path[current_state]  # Return the path to the goal state

        for next_state, cost in graph[current_state].items():
            # Calculate the new backward cost from the initial state to the next state
            new_backward_cost = backward_cost[current_state] + cost

            # Calculate the new total cost from the initial state to the next state
            new_total_cost = new_backward_cost + heuristic_costs[next_state]

            # Check if the next state has not been visited yet or the new total cost is lower than the existing cost
            if next_state not in backward_cost or new_backward_cost < backward_cost[next_state]:
                backward_cost[next_state] = new_backward_cost   # Update the backward cost of the next state
                total_cost[next_state] = new_total_cost         # Update the total cost of the next state
                path[next_state] = path[current_state] + [(current_state, next_state)]    # Update the path to the next state
                
                # Push the next state to the priority queue with the new priority
                heapq.heappush(queue, (new_total_cost, next_state))

    # If the goal state is not reached
    #print("No path found")
    return []




initial_state = input('enter initial city: ')
goal_state = input('destination city: ')

path = astar_search(travelling_cities, heuristic_costs, initial_state, goal_state)
print(path)
print('number of cities through the optimal path are: ', len(path))

'''
A* search algorithm will find the optimal path between two cities in a graph
'''