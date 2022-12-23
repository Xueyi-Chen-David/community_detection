import networkx as nx
import re
import os
from utils.data import data_preprocess
import matplotlib.pyplot as plt


train = data_preprocess("\Training")
train_list, train_dict = train.train_data()
files = train.files

colors =  ['green', 'yellow', 'pink', 'purple', '#DEB887', '#8B8378', '#00FFFF', '#7FFFD4', '#76EEC6', '#66CDAA', '#458B74'
,'#F0FFFF', '#E0EEEE', '#C1CDCD', '#838B8B', '#E3CF57', '#F5F5DC', '#FFE4C4', '#EED5B7', '#CDB79E', '#8B7D6B', '#FFEBCD', '#0000FF'
,'#0000EE', '#0000CD', '#00008B', '#8A2BE2', '#A52A2A', '#FF4040' , '#EE3B3B', '#CD3333', '#8B2323']

def draw(egonet_file):
    G = nx.Graph()
    node = []
    for line in open(egonet_file):
        e1, es = line.split(':')
        es = es.split()
        for e in es:
            if e == e1: continue
            G.add_edge(int(e1),int(e))
        node.append(e1)
        
    # for ego user's friends
    e1 = re.sub('\D', '', egonet_file.split('\\')[-1])
    for e in node:
        G.add_edge(int(e1),int(e))
        
    return G

def plot(user):
    target = int(files[user].split('.')[0])
    test_file = os.getcwd()+"\egonets\\" + str(target) + '.egonet'
    node_groups = []

    for i in range(len(train_list[user])):
        node_groups.append(list(map(int, train_list[user][i])))
    
    G = draw(test_file)

    color_map = []

    for node in G:
        temp = len(color_map)
        for i in range(len(node_groups)):
            if node in node_groups[i]:
                color_map.append(colors[i])
                break

        # if no element add, then the node is not in any list         
        if temp == len(color_map):
            color_map.append("red")
            
    print("ego_user: ", target)
    nx.draw(G, node_color=color_map, with_labels=True)
    plt.show()