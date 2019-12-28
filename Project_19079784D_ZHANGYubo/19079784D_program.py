def main():

    #section A
    print('SECTION A: THE STATE SPACE')
    print('')

    LegalStates=[]         #form a list 'LegalStates' that filled with all legal states
    for i in genStates():
        if isAStateLegal(i):
            LegalStates.append(i)
    
    print('The set of legal states: (108)')
    format_print(isAStateLegal)

    print('(c1):The set of illegal states that violates the constraint of\nhaving the boat with at least a man: (32)')
    format_print(c1)
        
    print('(c2):The set of illegal states that violates the constraint of\npreventing Pharaoh from beating others: (252)')
    format_print(c2)

    print('(c3):The set of illegal states that violates the constraint of\npreventing Ananias from beating Ahab\'s household: (192)')
    format_print(c3)

    print('(c4):The set of illegal states that violates the constraint of\npreventing Ahab from beating Ananias\'s household: (192)')
    format_print(c4)

    print('The set of illegal states that violate both c2 and c3: (96)')
    format_print(c2c3)

    print('The set of illegal states that violate both c2 and c4: (96)')
    format_print(c2c4)

    print('The set of illegal states that violate both c3 and c4: (144)')
    format_print(c3c4)

    print('The set of illegal states that violate c2, c3 and c4: (72)')
    format_print(c2c3c4)

    print('The set of illegal states that violate only c2: (72)')
    format_print(only_c2)

    print('The set of illegal states that violate only c3: (24)')
    format_print(only_c3)

    print('The set of illegal states that violate only c4: (24)')
    format_print(only_c4)
    
    
    #section B
    print('')
    print('SECTION B: FORMING A GRAPH')
    print('')
     
    graph=genGraph(LegalStates)       #'graph' is an adjacency list for all legal states

    paths=find_all_paths(graph, 'EEEEEEEEE', 'WWWWWWWWW', path=[])        #'paths' is a list with all paths
    
    shortest_path=findShortestPath(graph, 'EEEEEEEEE', 'WWWWWWWWW', path=[])        #'shortest_path' is a shortest path

    #filter out all the shortest paths and then form a list 'shortest_paths'
    def shortest(m):
        return len(m)==len(shortest_path)
    shortest_paths=list(filter(shortest,paths))

    pathstates=[]        #'pathstates' is a list containning the nodes that are part of at least one shortest path
    for i in shortest_paths:
        for j in i:
            pathstates.append(j)

    legal_graph=dict()        #'legal_graph' including only the nodes that are part of at least one shortest path
    for i in graph:
            graph[i]=list(set(graph[i]).intersection(pathstates))
    for i in graph:
        if len(graph[i])!=0 and (i in pathstates) :
            legal_graph.update({i:graph[i]})

    #print section B
    print('There are 38 legal states that are part of at least one shortest path')
    for i in legal_graph:
        print(i,legal_graph[i])
    print('')

    def other_states(m):
        if m not in pathstates:
            return True
        else:
            return False
    print('\nThere are 70 legsl states that are NOT part of any shortest path.')
    #format print other states
    num=0
    for i in LegalStates:
        if other_states(i):
            num+=1
            if num%6!=0:
                print(i,end=' ')
            else:
                print(i)

    #section C
    print('\n')
    print('SECTION C: SHORTEST PATHS')
    print('')

    printShortestPath(shortest_path)
    

    #use matplotlib&&networkx to draw section B's graph 
    printGraph(legal_graph)



# FUNCTIONS

# Section A




#Generate a tuple of all possible states
def genStates():
    states = ["".join((i,j,k,l,m,n,o,p,q)) for i in ["E","W"] for j in ["E","W"] for k in ["E","W"] for l in ["E","W"] \
                                           for m in ["E","W"] for n in ["E","W"] for o in ["E","W"] for p in ['E','W'] \
                                           for q in ['E','W']]
    return tuple(states)

#a function to print states as 'six strings per line'
def format_print(func):  #func is a function to filt states according to the required conditions
    num=0
    for i in genStates():
        if func(i):
            num+=1
            if num%6!=0:
                print(i,end=' ')
            else:
                print(i)
    print('\n')

#This function checks whether a state is legal or not
def isAStateLegal(state):
    if((state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))or\
       (state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))or\
       (state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))or\
    #boat move only with man
       (state[0] != state[1] and state[1]==state[2]==state[3]==state[4]==state[5]==state[6]==state[7]==state[8])or\
       (state[0] != state[1] and state[0]!=state[2] and state[0]!=state[3] and state[0]!=state[6])):
        return False
    else:
        return True

#filt states according to the required conditions and print these states
def c1(state):
    if(
    #boat move only with man
       (state[0] != state[1] and state[1]==state[2]==state[3]==state[4]==state[5]==state[6]==state[7]==state[8])or\
       (state[0] != state[1] and state[0]!=state[2] and state[0]!=state[3] and state[0]!=state[6])):
        return True
    else:
        return False

def c2(state):
    if((state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))):
        return True
    else:
        return False

def c3(state):
    if(state[3] != state[6] and (state[6] == state[4] or state[6] == state[5])):
        return True
    else:
        return False

def c4(state):
    if((state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False

def c2c3(state):
    if((state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))and\
        (state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))):
        return True
    else:
        return False

def c2c4(state):
    if((state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))and\
       (state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False

def c3c4(state):
    if((state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))and\
       (state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False

def c2c3c4(state):
    if((state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))and\
       (state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))and\
       (state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False

def only_c2(state):
    if((state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))and\
       not(state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))and\
       not(state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False

def only_c3(state):
    if(not(state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))and\
       (state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))and\
       not(state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False

def only_c4(state):
    if(not(state[1] != state[2] and (state[2]==state[3]or state[2]==state[4]or state[2]==state[5]or state[2]==state[6]or state[2]==state[7]or state[2]==state[8]))and\
       not(state[3] != state[6] and (state[6] == state[4] or state[6] == state[5]))and\
       (state[6] != state[3] and (state[3] == state[7] or state[3] == state[8]))):
        return True
    else:
        return False




# Section B




#form a adjacency list for all legal states
def genGraph(S):
    setLegalStates = []
    graph = {}
    for n in range(len(S)):
        if isAStateLegal(S[n]) == True:     
            setLegalStates.append(S[n])               
    for n in range(len(setLegalStates)):
        setNextNodes = nextStates(setLegalStates[n],setLegalStates)
        graph.update({setLegalStates[n]:setNextNodes})
    return graph

#check whether two states have a link or not
def nextStates(aState,allStates):   
    neighborStates = []
    for m in allStates:
        if neighborNode(aState,m) == True:
            neighborStates.append(m)
    return neighborStates

#the condions if two states have link
def neighborNode(n1, n2):
    diff = 0
    man=0
    if n1[0] != n2[0]:
        for i in range(1,9):
            if n1[i] == n1[0]:
                if n1[i] != n2[i]:
                    diff = diff + 1
                    if i in [1,2,3,6]:
                        man+=1
            else:
                if n1[i] != n2[i]:
                    return False
    else:
        return False   
    if 0<diff<3 and man>0:               #1~2 person move with at least a man to drive the boat
        return True
    else:
        return False

#a recursive function to find a shortest path
def findShortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not (start in graph):
        return None
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
    return shortestPath

#a recursive function to find all paths
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not (start in graph):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths




# Section C




#print one of the solutions
def printShortestPath(shortest_path):
    namelist=['','Moses','Pharaoh','Ahab','Jezebel','servant of Ahab','Ananias','Sapphira','servant of Ananias']
    for i in range(len(shortest_path)-1):
        East=[]
        West=[]
        if shortest_path[i][0]=='E':
            src='east'
            des='west'
        else:
            src='west'
            des='east'
        move_person=''
        for j in range(1,len(shortest_path[i])):
            if shortest_path[i][j]!=shortest_path[i+1][j]:
                move_person+=str(j)
        for j in range(1,len(shortest_path[i])):
            if shortest_path[i][j]=='E':
                East.append(namelist[j])
            if shortest_path[i][j]=='W':
                West.append(namelist[j])
        print('East:',East)
        print('West:',West)
        print('('+str(i+1)+')',end=' ')
        if len(move_person)==1:
            print('%s goes from the %s to the %s'%(namelist[int(move_person)],src,des))
        else:
            print('%s and %s go from the %s to the %s'%(namelist[int(move_person[0])],namelist[int(move_person[1])],src,des))



#use matplotlib&&networkx to draw section B's graph
import networkx as nx
import matplotlib.pyplot as plt
def printGraph(legal_graph):
    G=legal_graph                # Generate a graph G from the set of states (nodes)
    graph=nx.Graph()
    for i in G:
        graph.add_node(i)
    for i in G:
        for j in G[i]:
            graph.add_edge(j,i)
    nx.draw_networkx(graph,pos=nx.shell_layout(graph),font_size=10)
    plt.show()  

main()
#reference: A7-3couple.py