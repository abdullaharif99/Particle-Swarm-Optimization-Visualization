from particle import Swarm
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def costFunc(x):
    return 10*2 + (x[0] ** 2 - 10*math.cos(2*math.pi*x[0])) + (x[1] ** 2 - 10*math.cos(2*math.pi*x[1]))


def animate(iters, n_particles, pos_list):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()
    plt.ion()
    plt.show()
    for m in range(0, iters):
        xs = []
        ys = []
        for j in range(0, n_particles):
            x, y = pos_list[m][j]
            xs.append(x)
            ys.append(y)
        ax.scatter(xs, ys, c='b', marker="o", s=2)
        ax.set_title("Iteration " + str(m))
        plt.pause(0.25)


pos_list = []
weight_bounds = [0.4, 0.9]
c1 = 0.8
c2 = 0.9
n_particles = int(input("Number of particles: "))
n_iter = int(input("Number of itrations: "))
target_err = float(input("Target Error: "))

bounds = [(-5.12, 5.12), (-5.12, 5.12)]
init_vel = [0.0, 0.0]
swarm =Swarm(bounds, n_particles, 2, c1, c2, init_vel)


weight = weight_bounds[1]

for i in range(0, n_iter):
    w_change = (weight_bounds[1] - weight_bounds[0])/n_iter
    swarm.evaluate_particles(costFunc)
    swarm.calc_gbest()
    swarm.move_particles(weight)
    weight = weight = w_change
    pos_list.append(swarm.get_current_pos())
    iters = i + 1
    if swarm.g_best_err < target_err:
        break

print("Iterations performed: ", iters)
print("Best Error: ", swarm.g_best_err)
print("Solution: ", swarm.g_best)

animate(iters, n_particles, pos_list)