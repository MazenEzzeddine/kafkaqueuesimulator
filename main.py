


import matplotlib.pyplot as plt
import math
import random


import numpy as np

from scipy.stats import pareto


def simulate():
    # Use a breakpoint in the code line below to debug your script.

    time, produce_rate, lag, consume_rate, servers = [], [], [], [], []
    time.append(0),
    produce_rate.append(0)
    lag.append(0)
    consume_rate.append(0)
    servers.append(3)

    number_of_servers = 3
    max_rate_of_server = 5000
    frequency = 0.05
    time_period = 100
    offset = 10000
    amplitude = 5000
    rescale_time = 5
    pause = 0
    rescale_threshold = 10000
    rescale_cooldown = 30
    random_amplitude = 10000

    cooldown = 0

    lag_one_timestep = 0

    for t in range(1, time_period):
        time.append(t)
        if cooldown > 0:
            cooldown -= 1

        produce_one_timestep = offset + amplitude * math.cos(frequency * t) + random_amplitude * (
            random.uniform(-0.5, 0.5))
        if pause == 0:
            consume_one_timestep = min(produce_one_timestep + lag[-1], (number_of_servers * max_rate_of_server))
            lag_one_timestep = lag[-1] - consume_one_timestep + produce_one_timestep

            if lag_one_timestep > rescale_threshold and cooldown == 0:
                number_of_servers += 1
                pause = rescale_time
                cooldown = rescale_cooldown
            elif lag_one_timestep <= rescale_threshold and cooldown == 0 and (
                    (max_rate_of_server * number_of_servers) - produce_one_timestep > max_rate_of_server):
                number_of_servers -= 1
                pause = rescale_time
                cooldown = rescale_cooldown
        else:
            pause -= 1
            consume_one_timestep = 0
            lag_one_timestep = lag[-1] + produce_one_timestep

        produce_rate.append(produce_one_timestep)
        consume_rate.append(consume_one_timestep)
        lag.append(lag_one_timestep)
        servers.append(number_of_servers)

    fig, axs = plt.subplots(3)

    axs[0].plot(time, produce_rate, label='Produce rate')
    axs[0].plot(time, consume_rate, label='Consume rate')
    axs[1].plot(time, lag)
    axs[2].plot(time, servers)

    axs[2].set_xlabel("Time Units")

    axs[0].title.set_text('Events produced and consumed per second')
    axs[1].title.set_text('Consumer lag')
    axs[2].title.set_text('Number of consumers')

    axs[0].grid()
    axs[1].grid()
    axs[2].grid()

    axs[0].legend()

    fig.tight_layout()

    plt.show()# Press Ctrl+F8 to toggle the breakpoint.


def workload():
    time = []
    cos= []
    time_period = 600
    #frequency = 2*np.pi/(time_period)
    #frequency = 2*np.pi/(time_period/10)
    frequency = 2*np.pi/(time_period/10)
    amplitude = 50

    for t in range(1, time_period):
       # m = amplitude * math.sin(frequency * t)
       #  m = 200 + amplitude * math.sin(frequency * t) + 150 * (
       #      random.uniform(0.2, 1))
       #  m = 150 +  amplitude * math.sin(frequency * t) + 75 * (
       #  random.uniform(0.3, 0.8))
        m = 150 +  amplitude * math.sin(frequency * t) + 50 * (
        random.uniform(0.3, 0.9))
        time.append(t)
        cos.append(m)
        print(t, m)
    plt.plot(time, cos,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()
    work = open("work2.csv", "w")

    for i in range(len(time)):
        work.write(str(time[i]) + "," + str(cos[i]) + "\n")


    work.close()



def workload2():
    time = []
    cos= []
    time_period = 600
    #frequency = 2*np.pi/(time_period)
    #frequency = 2*np.pi/(time_period/10)
    frequency = 2*np.pi/(time_period/4)
    frequency2 = 2*np.pi/(time_period/2)
    amplitude = 50
    for t in range(1, time_period):
       # m = amplitude * math.sin(frequency * t)
       #  m = 200 + amplitude * math.sin(frequency * t) + 150 * (
       #      random.uniform(0.2, 1))
       #  m = 150 +  amplitude * math.sin(frequency * t) + 75 * (
       #  random.uniform(0.3, 0.8))
        m1 = 150 +  amplitude * math.sin(frequency * t)
        m2 = 50 + amplitude * math.sin(frequency2 * t)
        time.append(t)
        #cos.append((m2+m1))

        #m= m1+m2

       # m = (m2 + m1) * random.uniform(0.6, 0.9)
        m= (m2 + m1)  + 50 * random.uniform(0.1, 0.9)
        cos.append( m )
        print(t,m)
#print(t, m)
    plt.plot(time, cos,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()
    work = open("worktwosine.csv", "w")

    for i in range(len(time)):
        work.write(str(time[i]) + "," + str(cos[i]) + "\n")


def work2():
    import os
    import time
    import math

    # use threads in java?

    start = 30
    period = 2 * math.pi / 90
    amplitude = 200000
    vertical_shift = 200000
    limit = 100000
    for i in range(1, 91):
        start_time = time.time()
        # print(start_time)

        counter = 0

        finish_time = time.time()

        difference = finish_time - start_time
        # print(difference)
        # if difference <= 1:
        #     time.sleep(1 - difference)
        limit = vertical_shift + amplitude * math.cos(period * start)
        while (counter < limit):
            counter += 1
        start += 1

        print(i, counter)


def workload3():
    time = []
    cos= []
    time_period = 600
    #frequency = 2*np.pi/(time_period)
    #frequency = 2*np.pi/(time_period/10)
    frequency = 2*np.pi/(time_period/4)
    frequency2 = 2*np.pi/(time_period/2)
    amplitude = 50
    for t in range(1, time_period):
       # m = amplitude * math.sin(frequency * t)
       #  m = 200 + amplitude * math.sin(frequency * t) + 150 * (
       #      random.uniform(0.2, 1))
       #  m = 150 +  amplitude * math.sin(frequency * t) + 75 * (
       #  random.uniform(0.3, 0.8))
        m1 = 150 +  amplitude * math.sin(frequency * t)
        m2 = 50 + amplitude * math.sin(frequency2 * t)
        time.append(t)
        #cos.append((m2+m1))

        #m= m1+m2

        #m = (m2 + m1) * random.uniform(0.6, 0.9)
        #m= (m2 + m1)  +   20*pareto.rvs(2.75,1,3) #  3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        #m = (m2 + m1) +  pareto.rvs(10, 1, 50)  # 3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        m = (m2 + m1) + pareto.rvs(5, 1, 50)

        cos.append( m )
        print(t,m)
#print(t, m)
    plt.plot(time, cos,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()
    work = open("workparetoo.csv", "w")

    for i in range(len(time)):
        work.write(str(time[i]) + "," + str(cos[i]) + "\n")


def pplot():
    time = []
    val=[]

    work = open("workparetosingle2.csv", "r")
    for line in work:
        t, m = line.split(',')
        print(t,m)
        time.append(int(t))
        val.append(float(m))
    plt.plot(time, val,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()


def workload4():
    time = []
    cos= []
    time_period = 600
    #frequency = 2*np.pi/(time_period)
    #frequency = 2*np.pi/(time_period/10)
    frequency = 2*np.pi/(time_period/4)
    frequency2 = 2*np.pi/(time_period/2)
    amplitude = 50
    for t in range(1, time_period):
       # m = amplitude * math.sin(frequency * t)
       #  m = 200 + amplitude * math.sin(frequency * t) + 150 * (
       #      random.uniform(0.2, 1))
       #  m = 150 +  amplitude * math.sin(frequency * t) + 75 * (
       #  random.uniform(0.3, 0.8))
        m1 = 150 +  amplitude * math.sin(frequency * t)
        m2 = 50 + amplitude * math.sin(frequency2 * t)
        time.append(t)
        #cos.append((m2+m1))

        #m= m1+m2

        #m = (m2 + m1) * random.uniform(0.6, 0.9)
        #m= (m2 + m1)  +   20*pareto.rvs(2.75,1,3) #  3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        #m = (m2 + m1) +  pareto.rvs(10, 1, 50)  # 3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        #m = (m2 + m1) + pareto.rvs(5, 1, 50)

        #m = (m2 + m1) + pareto.rvs(5, 1, 50)
        m = m2 + pareto.rvs(5, 1, 50)

        cos.append( m )
        print(t,m)
#print(t, m)
    plt.plot(time, cos,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()
    work = open("workparetosingle.csv", "w")

    for i in range(len(time)):
        work.write(str(time[i]) + "," + str(cos[i]) + "\n")


def workload5():
    time = []
    cos= []
    time_period = 600
    #frequency = 2*np.pi/(time_period)
    #frequency = 2*np.pi/(time_period/10)
    frequency = 2*np.pi/(time_period/4)
    frequency2 = 2*np.pi/(time_period/5)
    amplitude = 50
    for t in range(1, time_period):
       # m = amplitude * math.sin(frequency * t)
       #  m = 200 + amplitude * math.sin(frequency * t) + 150 * (
       #      random.uniform(0.2, 1))
       #  m = 150 +  amplitude * math.sin(frequency * t) + 75 * (
       #  random.uniform(0.3, 0.8))
        m1 = 150 +  amplitude * math.sin(frequency * t)
        m2 = 50 + amplitude * math.sin(frequency2 * t)
        time.append(t)
        #cos.append((m2+m1))

        #m= m1+m2

        #m = (m2 + m1) * random.uniform(0.6, 0.9)
        #m= (m2 + m1)  +   20*pareto.rvs(2.75,1,3) #  3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        #m = (m2 + m1) +  pareto.rvs(10, 1, 50)  # 3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        #m = (m2 + m1) + pareto.rvs(5, 1, 50)

        #m = (m2 + m1) + pareto.rvs(5, 1, 50)
        #m = m2 + 50* random.uniform(1, 4)
       # m= m2 + random.gauss(100,10)
        m = m2 + pareto.rvs(4, 1, 50)

        cos.append( m )
        print(t,m)
#print(t, m)
    plt.plot(time, cos,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()
    work = open("workparetosingle.csv", "w")

    for i in range(len(time)):
        work.write(str(time[i]) + "," + str(cos[i]) + "\n")

def workload6():
    time = []
    cos= []
    time_period = 600
    #frequency = 2*np.pi/(time_period)
    #frequency = 2*np.pi/(time_period/10)
    frequency = 2*np.pi/(time_period/4)
    frequency2 = 2*np.pi/(time_period/2)
    amplitude = 50
    for t in range(1, time_period):
       # m = amplitude * math.sin(frequency * t)
       #  m = 200 + amplitude * math.sin(frequency * t) + 150 * (
       #      random.uniform(0.2, 1))
       #  m = 150 +  amplitude * math.sin(frequency * t) + 75 * (
       #  random.uniform(0.3, 0.8))
        m1 = 150 +  amplitude * math.sin(frequency * t)
        m2 = 150 + amplitude * math.sin(frequency2 * t)
        time.append(t)
        #cos.append((m2+m1))

        #m= m1+m2

        #m = (m2 + m1) * random.uniform(0.6, 0.9)
        #m= (m2 + m1)  +   20*pareto.rvs(2.75,1,3) #  3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        #m = (m2 + m1) +  pareto.rvs(10, 1, 50)  # 3 * (np.random.pareto((2.75, 1) + 1 ))  # * random.uniform(0.1, 0.9)

        m = (m2) + 100 * ( random.uniform(0.1, 0.9))#+ pareto.rvs(5, 1, 50)

        cos.append( m )
        print(t,m)
#print(t, m)
    plt.plot(time, cos,
             label="workload")
    plt.xticks()
    plt.xlabel('time (sec)')
    plt.ylabel('events/s')
    plt.title('A sine  workload ')
    # plt.grid()
    plt.legend()
    plt.show()
    work = open("uniform.csv", "w")

    for i in range(len(time)):
        work.write(str(time[i]) + "," + str(cos[i]) + "\n")


if __name__ == '__main__':
    #simulate()
    #workload()
    #workload3()
    #workload4()
    #workload5()



    #work2()
    #workload2()
    workload6()

    #pplot()







