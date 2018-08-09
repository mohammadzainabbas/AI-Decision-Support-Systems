#Task No. 02
print('3rd graph')
graph_3 = {7:[11,8],2:[],3:[8,10],11:[2,9,10],5:[11],9:[],8:[9]}
keys_3 = list(graph_3.keys())
##
##for i in range(len(keys_3)):
##    temp = graph_3.get(keys_3[i])
##    print(str(keys_3[i]) + ' is connected with ' + str(temp) + ' and has degree of ' + str(len(temp)))

for i in graph_3:
    In = 0;
    for j in graph_3:
        if (i in graph_3[j]):
            In = In + 1
    print(i, ' is connected with ', str(graph_3[i]),' and has out-degree ',str(len(graph_3[i])),' and in-degree ',str(In))

graph_4 = {'A':['B'],'B':['C','D','E'],'C':['E'],'D':['E'],'E':['F'],'F':[],'G':['D']}
keys_4 = list(graph_4.keys())

##for i in range(len(keys_4)):
##    temp = graph_4.get(keys_4[i])
##    print(str(keys_4[i]) + ' is connected with ' + str(temp) + ' and has degree of ' + str(len(temp)))
print('4th graph')
for i in graph_4:
    In = 0;
    for j in graph_4:
        if (i in graph_4[j]):
            In = In + 1
    print(i, ' is connected with ', str(graph_4[i]),' and has out-degree ',str(len(graph_4[i])),' and in-degree ',str(In))
