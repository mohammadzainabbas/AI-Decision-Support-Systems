#Testing

graph = {7:[11,8],2:[],3:[8,10],11:[2,9,10],5:[11],9:[],8:[9]}

for i in graph:
    print(i, str(len(graph[i])))
##    In = 0;
##    for j in graph_3:
##        if (i in graph_3[j]):
##            In = In + 1
##    print(i,' has out-degree ',str(len(graph_3[i])),' and in-degree ',str(In))
