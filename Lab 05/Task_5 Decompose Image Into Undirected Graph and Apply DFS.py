import numpy as np
import cv2 as cv
import time

image = np.array([[150, 2, 5], [80, 145, 45], [74, 102, 165]])  # a 3X3 array of numbers
pad = 1;
padded_image = np.pad(image, pad, 'constant');  # Padding the image with zeros


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



def DFS(graph1, start):
    path = [];

    q = [];
    q.append(start);

    while (len(q)!=0):

        node = q.pop();

        if node not in path:

            path.append(node)
            neighbours = graph1[node];

            for neighbour in neighbours:
                q.append(neighbour);

    return path;


graph, time = decompose(image);
path = DFS(graph,150);

print(graph)
print(path)
print('time taken----->');
print(time)