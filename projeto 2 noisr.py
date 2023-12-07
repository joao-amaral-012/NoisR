import random
import matplotlib.pyplot as plt


def random_walk(num_steps, prob_right, num_particles):

    particle_paths = [[0] for i in range(num_particles)] #particle paths tem o path de todas as partículas, estando cada step de cada partícula numa lista ordenada
    for step in range(1, num_steps):                     #por exemplo: se fossem três partículas, seria particle_paths = [[0][0][0]]
        for particula in range(num_particles):

            x = random.uniform(0,1)

            if x <= prob_right:
                particle_paths[particula].append(particle_paths[particula][-1]+1)
            else:
                particle_paths[particula].append(particle_paths[particula][-1]-1)

    create_plot(num_steps, particle_paths)

    return particle_paths


def create_plot (num_steps, particle_paths):
    time = [x for x in range (len(particle_paths [0]))]

    for particle_path in particle_paths:
        plt.plot(particle_path, time)

    plt.title ('Random Walk - N particles')
    plt.xlabel ('Position')
    plt.ylabel ('Time')
    plt.show ()


num_steps = 100
prob_right = 0.5
num_particles = 100

random_walk(num_steps, prob_right, num_particles)