import matplotlib.pyplot as plt
import numpy as np

twopi = 2*np.pi

def std_map_traj(itr, ic, K=0.5):
    '''Iterations, initial conditions and K'''
    state = np.empty(shape=(itr+1, 2), dtype=ic.dtype)
    state[0][0], state[0][1] = ic[0], ic[1] # Initial conditions of (p,x)
    for i in range(itr):
        p = state[i][0] + K * np.sin(state[i][1])
        x = state[i][1] + p
        # Only consider (p,x) in [0,twopi]*[0,twopi]
        state[i+1] = np.asarray([twopi*(p/twopi - np.floor(p/twopi)), twopi*(x/twopi - np.floor(x/twopi))])

    return state

ic = np.asarray([.5, .3])
traj = std_map_traj(2**10, ic, 0.7)

fig, ax = plt.subplots()
ax.scatter(traj[:, 1], traj[:, 0], marker='.', s=5, linestyle='None')
fig.savefig('std_map.png', format='png')

