


import matplotlib.pyplot as plt
import math
import random


def simulate():
    # Use a breakpoint in the code line below to debug your script.

    time, produce_rate, lag, consume_rate, servers = [], [], [], [], []
    time.append(0),
    produce_rate.append(0)
    lag.append(0)
    consume_rate.append(0)
    servers.append(3)

    number_of_servers = 4
    max_rate_of_server = 5000
    frecuency = 0.05
    time_period = 1000
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

        produce_one_timestep = offset + amplitude * math.cos(frecuency * t) + random_amplitude * (
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


def cos():
    time = []
    cos= []
    time_period = 1000
    frequency = 0.01

    amplitude = 5000

    for t in range(1, time_period):
         #m = amplitude * math.cos(frequency * t)
        m=  math.cos(frequency * t)
        time.append(t)
        cos.append(m)
    plt.plot(time, cos,
             label="time cosine")

    plt.xticks()
    plt.xlabel('time (min)')
    plt.ylabel('events lag')
    plt.title('A cosine workload ')
    # plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    #simulate()
    cos()

