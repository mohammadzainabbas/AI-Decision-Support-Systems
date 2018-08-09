#Task No. 01

graph_1 = {1:[2,5],2:[1,3,5],3:[2,4],4:[3,5,6],5:[1,2,4],6:[4]}
keys_1 = list(graph_1.keys())

for i in range(len(keys_1)):
    temp = graph_1.get(keys_1[i])
    print(str(keys_1[i]) + ' is connected with ' + str(temp) + ' and has degree of ' + str(len(temp)))

graph_2 = {'A':['B','D','E'],'B':['D','E','A'],'C':['D'],'D':['A','B','C'],'E':['A','B']}
keys_2 = list(graph_2.keys())

for i in range(len(keys_2)):
    temp = graph_2.get(keys_2[i])
    print(str(keys_2[i]) + ' is connected with ' + str(temp) + ' and has degree of ' + str(len(temp)))
