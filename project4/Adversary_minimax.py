# keys in the ethiopia_coffee_location represents a city
# where as the corresponding values are neighbors or successors
ethiopia_coffee_location = {
    "Addis Ababa": {"Ambo", "Buta Jirra", "Adama"},
    "Ambo": {"Gedo", "Nekemte"},
    "Buta Jirra": {"Worabe", "Wolkite"},
    "Adama": {"Dire Dawa", "Mojo"},
    "Gedo": {"Shambu", "Fincha"},
    "Nekemte": {"Gimbi", "Limu"},
    "Worabe": {"Hosana", "Durame"},
    "Wolkite": {"Benchi Naji", "Tepi"},
    "Mojo": {"Dilla", "Kaffa"},
    "Dire Dawa": {"Chiro", "Harar"}
}

# the dict terminal_with_utilities represents terminal cities with their utility
terminal_with_utilities = {
    "Shambu": 4, "Fincha": 5, "Gimbi": 8, "Limu": 8, "Hosana": 6, "Durame": 5,
    "Benchi Naji": 5, "Tepi": 6, "Kaffa": 7, "Dilla": 9, "Chiro": 6, "Harar": 10
}

# the fun minimax_search 
# state represents current city
# is_maximizer checks the current state is minizing or maximizing player & returns bool
def minimax_search(state, is_maximizer):
    if state not in ethiopia_coffee_location:
        # will return state & utility, if the node is terminal_node
        return [state], terminal_with_utilities[state]
    
    #initialization
    neighbors = ethiopia_coffee_location[state]
    best_path = []
    best_utility = float('-inf') if is_maximizer else float('inf')

    #iterating over the successors or neighboring cities 
    for neighbor in neighbors:
        #recursively calls minimax_search on each neighbor
        path, neighbor_utility = minimax_search(neighbor, not is_maximizer)
        if is_maximizer:
            if neighbor_utility > best_utility: # if true it will return best_path & best_utility
                best_utility = neighbor_utility
                best_path = [state] + path
        else:
            if neighbor_utility < best_utility:
                best_utility = neighbor_utility
                best_path = [state] + path

    # the function will return best path & with its best utility
    return best_path, best_utility

start_city = "Addis Ababa"

best_path, utility = minimax_search(start_city, True)

if best_path:
    print(f"The best achievable destination for Coffee Quality from {start_city} is:")
    print(" -> ".join(best_path))
    print(f" have a Utility of: {utility}")
else:
    print(f"No reachable destination found from {start_city}.")

'''
the minimax considers Addis Ababa as inital and explores the terminal nodes &
# will find the best path & utility value from the given dict
above by maximizing & minimizing players. 
'''