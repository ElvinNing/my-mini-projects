import matplotlib.pyplot as plt
import numpy as np

twopi = 2*np.pi

def std_map_multi(itr, ic, K=0.5):
    state = np.empty(
            shape=tuple([itr+1]+list(ic.shape)),
            # Question 1 list tuple???
            dtype = ic.dtype)
    state[0, :] = ic
    for i in range(itr):
        state[i+1, 1] = np.mod(state[i, 1] + K*np.sin(state[i, 0]), twopi)
        state[i+1, 0] = np.mod(state[i, 0] + state[i+1, 1], twopi)
    return state

ic = 2*np.pi*np.random.random((2,32))
states = std_map_multi(200, ic, K=0.7)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(states[:, 0], states[:, 1], marker = '.', linestyle='None')
fig.savefig('std_map_multi.png', format = 'png')