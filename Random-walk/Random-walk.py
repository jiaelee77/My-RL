'''
I refer to the site, "https://frhyme.github.io/python/randomwalk/". 
'''

import numpy as np 
import matplotlib.pyplot as plt

## random walk in 1dim 
move_set = [-1, 1]
plt.figure(figsize=(15, 4))
for i in range(0, 5):
    xs = np.array([np.random.choice(move_set) for i in range(0, 100)])
    cum_xs = np.cumsum(xs)
    plt.plot(np.arange(0, len(xs)), cum_xs, linestyle='--', label='random_walk_{}'.format(i))
plt.legend()
plt.savefig('random-walk-1d.png')
plt.show()

## random walk in 2dim
move_set = [[-1, 0], [1, 0], [0, -1], [0, 1]]
plt.figure(figsize=(10, 10))
for i in range(0, 5):
    moves = [[0, 0]]+[move_set[np.random.randint(0, len(move_set))] for i in range(0, 300)]
    moves = np.array([np.array(m) for m in moves])
    cum_moves = np.cumsum(moves, axis=0)
    plt.plot(cum_moves[:, 0], cum_moves[:, 1], marker='o', alpha=0.5)
plt.savefig('random-walk_2d.png')
plt.show()

## random walk in 3dim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111, projection='3d')
## random walk in 2dim
move_set = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [0, -1, 0]]

for i in range(0, 5):
    moves = [[0, 0, 0]]+[move_set[np.random.randint(0, len(move_set))] for i in range(0, 500)]
    moves = np.array([np.array(m) for m in moves])
    cum_moves = np.cumsum(moves, axis=0)
    ax.plot(cum_moves[:, 0], cum_moves[:, 1], cum_moves[:, 2], 
            marker='o', markersize=3, linestyle='-', linewidth=2)
plt.savefig('random-walk_3d.png')
plt.show()
