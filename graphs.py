verticles = []
con = []
edges = []
weights = []

myGraph = {'a': {'b': 4, 'c': 10}, 
     'b': {'c': 5, 'e': 12}, 
     'c': {'e': 6, 'd': 14}, 
     'd': {'e': 13}, 
     'e': {'f':3},
     'f': {'a': 2}
           }
for start,d in myGraph.items():
    for end, weight in d.items():
##        print ('{} -> {} {};\n'.format(start,end,weight))
        con.append(start+end+str(weight))
        weights.append(weight)
        edges.append(start+end)
    verticles.append(start)
print str(edges)


def MinimumSpanningTree(edges, verticles):
    MST=[]
    counter=0;
    for i in edges:
        for j in verticles:
            if i[0] in j:
                first=j
                break
            else:
                continue
        for j in verticles:
            if i[1] in j:
                second=j
                break
            else:
                continue
        if not first==second:
            MST.append((i[0],i[1]))
            new = first + second
            verticles.remove(first)
            verticles.remove(second)
            verticles.append(new)
            counter+=1
    print MST
##    
def sorting():
    vertexWeight = sorted(con, key=sortByLast)
    return vertexWeight
    
def sortByLast(s):
    return int(s[2:])
##def sortbyfirst(s):
##    return s[0:2]

def degree(verticles, edges):
    degree = 0
    for edge in edges:
        if verticles in edge:
            degree += 1
    print "The degree of node "+str(verticles)+" is: "+str(degree)


##print verticles
##
edges=[]
vertexWeight = sorting()
for a in vertexWeight:
    edge = a[0:2]
    edges.append(edge)
print edges
##print weights
##print vertexWeight

def totalWeight():
    totalWeight = 0
    for weight in weights:
        totalWeight +=  weight
    print "The total Weight of the graph is: "+str(totalWeight)


def main():
    inputs = ''
    while inputs != 'q':
        inputs =  raw_input("Enter command : 1 to find degree, 2 to find minimum spanning tree, 3 to find the total weight, q to quit: ")
        if inputs == '1':
            node=raw_input("Enter node: ")
            degree(node, edges)
            print ("\n")
        elif inputs == '2':
            MinimumSpanningTree(edges,verticles)
            print ("\n")
        elif inputs == '3':
            totalWeight()
            print ("\n")

main()
