import random
import numpy as np


class Particle:
    def __init__(self, x, c1, c2, init_vel):
        self.c1 = c1 #cognitive constant
        self.c2 = c2 #social constant
        self.position = x
        self.p_best = self.position
        self.best_err = float('inf')
        self.velocity = init_vel
        self.err = 0.0

    def evaluate(self, costfunc):
        self.err = costfunc(self.position)
        if self.err < self.best_err:
            self.p_best = self.position
            self.best_err = self.err

    def move(self, weight, g_best):
        cognitive = (self.c1*random.uniform(-1, 1))* (np.array(self.p_best) - np.array(self.position))
        social = (self.c2*random.uniform(-1, 1)) * (np.array(g_best) - np.array(self.position))
        self.velocity = weight*np.array(self.velocity) + cognitive + social
        self.position = self.position + self.velocity


class Swarm:
    def __init__(self, bounds, n_particles, n_dim, c1, c2, init_vel):
        self.particles = []
        self.g_best = []
        self.g_best_err = float('inf')
        self.bounds = bounds
        self.n_particles = n_particles

        for i in range(0, n_particles):
            x = []
            for n in range(0, n_dim):
                x.append(random.uniform(bounds[n][0], bounds[n][1]))

            self.particles.append(Particle(x, c1, c2, init_vel))

    def calc_gbest(self):
        for i in range(0, self.n_particles):
            if self.particles[i].best_err < self.g_best_err:
                self.g_best = self.particles[i].p_best
                self.g_best_err = self.particles[i].best_err

    def evaluate_particles(self, costFunc):
        for i in range(0, self.n_particles):
            self.particles[i].evaluate(costFunc)

    def move_particles(self, weight):
        for i in range(0, self.n_particles):
            self.particles[i].move(weight, self.g_best)

    def get_current_pos(self):
        l = []
        for i in range(0, self.n_particles):
            l.append(self.particles[i].position)
        return l
