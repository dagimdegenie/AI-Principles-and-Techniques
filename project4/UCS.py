
# dict consists key(cities) & correspodning path cost
ethiopia_cities = {
    'Addis Ababa': {'Adama': 3, 'Ambo': 5, 'Debre Berhan': 5},
    'Adama': {'Matahara': 3, 'Asella': 4, 'Batu': 4, 'Addis Ababa': 3},
    'Ambo': {'Wolkite': 6, 'Addis Ababa': 9, 'Nekemte': 5},
    'Debre Berhan': {'Addis Ababa': 5, 'Debre Sina': 2},
    'Matahara': {'Adama': 3, 'Awash': 1},
    'Asella': {'Adama': 4, 'Assasa': 4},
    'Batu': {'Adama': 4, 'Buta Jirra': 2, 'Shashamene': 3},
    'Wolkite': {'Ambo': 6, 'Worabe': 5, 'Jimma': 8},
    'Nekemte': {'Ambo': 9, 'Bedelle': 5, 'Gimbi': 4},
    'Debre Sina': {'Debre Berhan': 2, 'Kemise': 6, 'Debre Markos': 17},
    'Awash': {'Chiro': 4, 'Gobi Rasu': 5, 'Matahara': 1},
    'Assasa': {'Asella': 4, 'Dodolla': 1},
    'Buta Jirra': {'Batu': 2, 'Worabe': 2},
    'Shashamene': {'Batu': 3, 'Hawassa': 1, 'Dodolla': 3, 'Hossana': 7},
    'Worabe': {'Wolkite': 5, 'Hossana': 2, 'Buta Jirra': 2},
    'Jimma': {'Wolkite': 8, 'Bonga': 4, 'Bedelle': 7},
    'Bedelle': {'Nekemte': 5, 'Gore': 6, 'Jimma': 7},
    'Gimbi': {'Nekemte': 4, 'Dambidollo': 6},
    'Kemise': {'Debre Sina': 6, 'Dessie': 4},
    'Debre Markos': {'Debre Sina': 17, 'Finote Selam': 3},
    'Chiro': {'Awash': 4, 'Dire Dawa': 8},
    'Gobi Rasu': {'Awash': 5, 'Samara': 9},
    'Dodolla': {'Assasa': 1, 'Shashamene': 3, 'Bale': 13},
    'Hawassa': {'Shashamene': 1, 'Dilla': 3},
    'Hossana': {'Shashamene': 7, 'Worabe': 2, 'Wolaita Sodo': 4},
    'Bonga': {'Jimma': 4, 'Dawro': 10, 'Tepi': 8, 'Mizan Teferi': 4},
    'Gore': {'Tepi': 9, 'Gambella': 5, 'Bedelle': 6},
    'Dambidollo': {'Gimbi': 6, 'Assosa': 12, 'Gambella': 4},
    'Dessie': {'Kemise': 4, 'Woldia': 6},
    'Finote Selam': {'Debre Markos': 3, 'Bahirdar': 6, 'Injibara': 2},
    'Dire Dawa': {'Chiro': 8, 'Harar': 4},
    'Samara': {'Gobi Rasu': 9, 'Fanti Rasu': 7, 'Alamata': 11, 'Woldia': 8},
    'Bale': {'Liben': 11, 'Dodolla': 13, 'Goba': 18, 'Sof Oumer': 23},
    'Dilla': {'Hawassa': 3, 'Bulehora': 4},
    'Wolaita Sodo': {'Arba Minchi': 5, 'Dawro': 6, 'Hossana': 4},
    'Dawro': {'Bonga': 10, 'Wolaita Sodo': 10},
    'Tepi': {'Gore': 9, 'Bonga': 8, 'Mizan Teferi': 4},
    'Mizan Teferi': {'Tepi': 4, 'Bonga': 4},
    'Gambella': {'Gore': 5, 'Dambidollo': 4},
    'Assosa': {'Dambidollo': 12},
    'Woldia': {'Dessie': 6, 'Lalibela': 7, 'Samara': 8, 'Alamata': 3},
    'Bahirdar': {'Finote Selam': 6, 'Injibara': 4, 'Metekel': 11, 'Azezo': 7, 'Debre Tabor': 4},
    'Injibara': {'Bahirdar': 4, 'Finote Selam': 2},
    'Harar': {'Dire Dawa': 4, 'Babile': 2},
    'Fanti Rasu': {'Samara': 7, 'Kilbet Rasu': 6},
    'Alamata': {'Samara': 11, 'Woldia': 3, 'Mekelle': 5, 'Sekota': 6},
    'Liben': {'Bale': 11},
    'Goba': {'Bale': 18, 'Sof Oumer': 6, 'Babile': 28},
    'Sof Oumer': {'Goba': 6, 'Bale': 23, 'Gode': 23},
    'Bulehora': {'Dilla': 4, 'Yabello': 3},
    'Arba Minchi': {'Wolaita Sodo': 5, 'Konso': 4, 'Basketo': 10},
    'Basketo': {'Arba Minchi': 10, 'Benchi Maji': 5},
    'Metekel': {'Bahirdar': 11},
    'Lalibela': {'Woldia': 7, 'Debre Tabor': 8, 'Sekota': 6},
    'Debre Tabor': {'Lalibela': 8, 'Bahirdar': 4},
    'Azezo': {'Gondar': 1, 'Bahirdar': 7, 'Metema': 7},
    'Babile': {'Harar': 2, 'Jigjiga': 3, 'Goba': 28},
    'Kilbet Rasu': {'Fanti Rasu': 6},
    'Mekelle': {'Alamata': 5, 'Adwa': 7, 'Adigrat': 4, 'Sekota': 9},
    'Sekota': {'Alamata': 6, 'Mekelle': 9, 'Lalibela': 6},
    'Dega Habur': {'Jigjiga': 5, 'Kebri Dehar': 6},
    'Kebri Dehar': {'Gode': 5, 'Dega Habur': 6, 'Werdez': 6},
    'Yabello': {'Bulehora': 3, 'Konso': 3, 'Moyale': 6},
    'Konso': {'Arba Minchi': 4, 'Yabello': 3},
    'Benchi Maji': {'Basketo': 5},
    'Gondar': {'Azezo': 1, 'Humera': 9, 'Metema': 7, 'Debarke': 4},
    'Metema': {'Azezo': 7, 'Gondar': 7},
    'Jigjiga': {'Babile': 3, 'Dega Habur': 5},
    'Adwa': {'Mekelle': 7, 'Axum': 1, 'Adigrat': 4},
    'Adigrat': {'Mekelle': 4, 'Adwa': 4},
    'Gode': {'Dollo': 17, 'Kebri Dehar': 5, 'Sof Oumer': 23},
    'Werdez': {'Kebri Dehar': 6},
    'Moyale': {'Yabello': 6},
    'Debarke': {'Gondar': 4, 'Shire': 7},
    'Axum': {'Shire': 2, 'Adwa': 1},
    'Dollo': {'Gode': 17},
    'Shire': {'Axum': 2, 'Humera': 8, 'Debarke': 7},
    'Humera': {'Shire': 8, 'Gondar': 9}
}

print('\n\n solution for problem 2.1 \n')

def print_graph(graph):
    for city, connections in graph.items():
        print(city)
        for neighbor, distance in connections.items():
            print(f"  -> {neighbor}: {distance}")

print_graph(ethiopia_cities)

print('\n\n solution for problem 2.2 \n\n')


from queue import PriorityQueue


class PathFinder:
    def __init__(self, graph):
        self.graph = graph

    def uniform_cost_search(self, start_city, goal_city):
        priority_queue = PriorityQueue()
        priority_queue.put((0, [start_city]))  # (priority, path)
        visited = set()

        while not priority_queue.empty():
            cost, path = priority_queue.get()
            current_city = path[-1]

            if current_city == goal_city:
                return path, cost

            if current_city in visited:
                continue

            visited.add(current_city)

            for neighbor, distance in self.graph[current_city].items():
                new_cost = cost + distance
                new_path = path + [neighbor]
                priority_queue.put((new_cost, new_path))

        return None, None

path_finder = PathFinder(ethiopia_cities)

# Find a path from "Addis Ababa" to "Lalibela" using uniform cost search

start_city = input("Enter the start city: ")
goal_city = input("Enter the destination city: ")


path, cost = path_finder.uniform_cost_search(start_city, goal_city)

if path:
    print("\nPossible path from", start_city, "to", goal_city, ":")
    print(" -> ".join(path))
    print("Total path cost:", cost)
else:
    print("No path found between", start_city, "and", goal_city)



print('\n\n solution for problem 2.3 \n')


start_city = 'Addis Ababa' #input("Enter the start city: ")
goals = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minchi"]

while goals:
    goal_city = goals[0]
    goals = goals[1:]

    path, cost = path_finder.uniform_cost_search(start_city, goal_city)

    if path:
        print("\nPossible path from", start_city, "to", goal_city, ":")
        print(" -> ".join(path))
        print("Total path cost:", cost)
    else:
        print("No path found between", start_city, "and", goal_city)

    start_city = goal_city
	

def customized_UCS(start, goals, graph):
    path_finder = PathFinder(graph)

    goal_cost = dict()
    min_cost = float('inf')
    min_cost_city = None
    min_cost_path = None

    for goal in goals:
        path_ucs, cost_ucs = path_finder.uniform_cost_search(start, goal)
        if cost_ucs is None:
            continue
        goal_cost[goal] = cost_ucs
        if cost_ucs < min_cost:
            min_cost = cost_ucs
            min_cost_city = goal
            min_cost_path = path_ucs

    return min_cost_city, min_cost_path, min_cost


#goals = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minchi"]
#start = "Addis Ababa"
local_optimum = customized_UCS(start_city, goals, ethiopia_cities)
print('\n preserved the local optimum: ', local_optimum)





