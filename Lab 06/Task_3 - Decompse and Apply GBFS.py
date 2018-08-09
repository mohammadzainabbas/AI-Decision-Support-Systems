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

def GBFS(graph, start_node, goal_node, priority = 0, path = []):
    pq = Q.PriorityQueue()
    pq.put((priority, start_node))

    while(not pq.empty()):
        u = pq.get()
        pq = Q.PriorityQueue()
        if u[1] == goal_node:
            path.append(u[1])
            return path
        else:
            for values in graph[u[1]]:
                for key in values.keys():
                    if key not in path:
                        pq.put((values[key], key))
            path.append(u[1])
    return path

graph_1 = {150:[{2:[5,150,145]},{80:[74,150]}],
           80:[{150:[2,80]},{145:[2,80,45,102]},{74:[80,102]}],
           74:[{80:[74,150]},{102:[145,74,165]}],
           2:[{150:[2,80]},{145:[2,80,45,102]},{5:[2,45]}],
           145:[{2:[5,150,145]},{80:[74,150]},{45:[5, 145, 165]}],
           102:[{145:[2,80,45,102]},{74:[80,102]},{165:[45,102]}],
           5:[{2:[5,150,145]},{45:[5, 145, 165]}],
           45:[{5:[2,45]},{145:[2,80,45,102]},{165:[45,102]}]}

image = np.array([[150, 2, 5], [80, 145, 45], [74, 102, 165]])  # a 3X3 array of numbers
pad = 1;
padded_image = np.pad(image, pad, 'constant');  # Padding the image with zeros

graph, time = decompose(image);
path = GBFS(graph_1,150, 165);

print(path)