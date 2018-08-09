import numpy as np
import cv2 as cv
import time
import queue as Q
# This reduces the need to verfiy corner pixels in the 8-connectivity algo
# The extra zeros can be discarded later on
def decompose(image):
    pad = 1;
    padded_image = np.pad(image, pad, 'constant');

    d = {}

    start_time = time.time()

    for x in range(pad, (padded_image.shape[0] - (pad))):
        for y in range(pad, (padded_image.shape[1] - (pad))):

            a = list();

            temp = np.array(padded_image[x - pad: x + pad + 1, y - pad:y + pad + 1]);

            temp [0,0] = 0
            temp [0,2] = 0
            temp [2,0] = 0
            temp [2,2] = 0

            for i in range(temp.shape[0]):
                for j in range(temp.shape[1]):
                    if not ((temp[i][j] == 0) or (temp[i][j] == padded_image[x][y])):
                        a.append(temp[i][j]);

            d[padded_image[x][y]] = a;

    final_time = time.time() - start_time;
    return d, final_time;

def A_Star(graph, straight_line_distance, start_node, goal_node, priority = 0, path = []):
    pq = Q.PriorityQueue()
    pq.put((priority, (start_node, 0)))
    while(not pq.empty()):
        current = pq.get()
        pq = Q.PriorityQueue()
        if current[1][0] == goal_node:
            path.append(current[1][0])
            return path
        else:
            for value in graph[current[1][0]]:
                if value not in path:
                    edge_cost = graph[current[1][0]][value]
                    pq.put(((current[1][1] + edge_cost + straight_line_distance[value]), (value, current[1][1] + edge_cost)))
            path.append(current[1][0])
    return path

graph_1 = {150:{{2:5,150,145},{80:74,150}},
           80:{{150:2,80},{145:2,80,45,102},{74:80,102}},
           74:{{80:74,150},{102:145,74,165}},
           2:{{150:2,80},{145:2,80,45,102},{5:2,45}},
           145:{{2:[5,150,145]},{80:[74,150]},{45:[5, 145, 165},
           102:{{145:[2,80,45,102]},{74:[80,102]},{165:[45,102]},
           5:{{2:5,150,145},{45:5, 145, 165}},
           45:{{5:2,45},{145:2,80,45,102},{165:[45,102}}}

path_1 = { 150:4,
           80:3,
           74:2,
           2:3,
           145:2,
           102:1,
           5:2,
           45:1 }


image = np.array([[150, 2, 5], [80, 145, 45], [74, 102, 165]])  # a 3X3 array of numbers
pad = 1;
padded_image = np.pad(image, pad, 'constant');  # Padding the image with zeros
graph, time = decompose(image);
path = A_Star(graph_1,path_1,150, 165);

print(path)
