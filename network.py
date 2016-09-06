# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import csv
import copy 
import difflib 
import pandas as pd

with open('1.csv', 'rb') as f:
    reader = csv.reader(f)
    source_0 = map(list, reader)
del source_0[0]  
source = copy.deepcopy(source_0)

with open('2.csv', 'rb') as f:
    reader = csv.reader(f)
    target_0 = map(list, reader)
del target_0[0]  
target = copy.deepcopy(target_0)

G=nx.Graph()


G.add_nodes_from(["Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"])
pos=nx.random_layout(G)
friends = {'Rachel': 1, 'Monica': 2, 'Phoebe': 3, 'Joey': 4, 'Chandler': 5, 'Ross': 6}
numbers = {1 :'Rachel', 2: 'Monica', 3: 'Phoebe', 4: 'Joey', 5: 'Chandler', 6: 'Ross'}
w, h = 7, 7
matrix = [[0 for x in range(w)] for y in range(h)] 

for i in range(len(source)-1):
	x = source[i][0]
	y = target[i][0]
	if x == 'Rachel' or x == 'Monica' or x == 'Phoebe' or x == 'Joey' or x == 'Chandler' or x == 'Ross':
		if y == 'Rachel' or y == 'Monica' or y == 'Phoebe' or y == 'Joey' or y == 'Chandler' or y == 'Ross':
			if x!= y:
				first = min(friends[x],friends[y])
				last = max(friends[x],friends[y])
				matrix[first][last] += 1

for x in range(1,7):
	for y in range(1,7):
		if matrix[x][y]!=0:
			print numbers[x] + " and " + numbers[y] + ": " + str(matrix[x][y])

G.add_edge('Rachel', 'Monica', weight=matrix[1][2])
G.add_edge('Rachel', 'Phoebe', weight=matrix[1][3])
G.add_edge('Rachel', 'Joey', weight=matrix[1][4])
G.add_edge('Rachel', 'Chandler', weight=matrix[1][5])
G.add_edge('Rachel', 'Ross', weight=matrix[1][6])

G.add_edge('Monica', 'Phoebe', weight=matrix[2][3])
G.add_edge('Monica', 'Joey', weight=matrix[2][4])
G.add_edge('Monica', 'Chandler', weight=matrix[2][5])
G.add_edge('Monica', 'Ross', weight=matrix[2][6])

G.add_edge('Phoebe', 'Joey', weight=matrix[3][4])
G.add_edge('Phoebe', 'Chandler', weight=matrix[3][5])
G.add_edge('Phoebe', 'Ross', weight=matrix[3][6])

G.add_edge('Joey', 'Chandler', weight=matrix[4][5])
G.add_edge('Joey', 'Ross', weight=matrix[4][6])

G.add_edge('Chandler', 'Ross', weight=matrix[5][6])


nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
labels = nx.get_edge_attributes(G,'weight')
nx.draw(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("1.png") # save as png
plt.show() # display