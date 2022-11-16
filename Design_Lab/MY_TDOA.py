from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d

def tdoa(micro =[], velocity =340.0, source =[]):
    distances = []
    for mic in micro:
        x_diff = np.abs(mic[0]-source[0][0])
        y_diff = np.abs(mic[1]-source[0][1])
        z_diff = np.abs(mic[2]-source[0][2])
        xy_diff = np.sqrt(np.power(x_diff,2)+np.power(y_diff,2))

        distances.append(np.sqrt(np.power(xy_diff,2)+np.power(z_diff,2)))

    times = [distance/velocity for distance in distances]
    all_differences = np.zeros((len(times),len(times)))
    time_differences = []

    #MY TIME DIFFERENCES
    my_time_diffs = []
    mic_num = 0
    for time in times:
        dict = {"Mic " + str(mic_num) : time - min(times)}
        my_time_diffs.append(dict)
        mic_num += 1


    for i in range(len(times)):
        for j in range(len(times)):
            all_differences[i,j] = times[i] - times[j]

    for i in range(len(times)):
        for j in range(len(times)):
            try:
                if i != 0:
                    time_differences.append({"TDoA_"+str(i+1)+"_"+str(j+i+2) : all_differences[i,j+i+1]})
                else:
                    time_differences.append({"TDoA_"+str(i+1)+"_"+str(j+i+1) : all_differences[i,j+i]})
            except:
                continue

    return distances, times, time_differences, all_differences, my_time_diffs


def time_differences_between_every_mic(micro =[], velocity =343.0, source =[]):
    distances = []
    for mic1 in micro:
        for mic2 in micro:
            x_diff = np.abs(mic1[0]-mic2[0])
            y_diff = np.abs(mic1[1]-mic2[1])
            z_diff = np.abs(mic1[2]-mic2[2])
            xy_diff = np.sqrt(np.power(x_diff,2)+np.power(y_diff,2))

            distances.append(np.sqrt(np.power(xy_diff,2)+np.power(z_diff,2)))
    times = [distance/velocity for distance in distances]

    return times


# sources = np.zeros((7,2))
# for ele in sources:
#     ele[0] = random.randint(0,1000)
#     ele[1] = random.randint(0,1000)
microphones = np.array([[ 500.,  550., 0.],
                    [ 500.,  450., 0.],
                    [ 550.,  525., 0.],
                    [ 550.,  475., 0.],
                    [ 450.,  525., 0.],
                    [ 450.,  475., 0.]])


source = np.array([[random.randint(0,1000), random.randint(0,1000), random.randint(0,1000)]])
# source = np.array([[100., 100., 100.]])
velocity = 343.0  # m

# Count ranges
distances, times, time_differences, all_diffs, my_time_diffs = tdoa(microphones, velocity, source)
# print(distances)
# print(times)
# print(my_time_diffs)
#
# print()
# print(time_differences)
#
# print()
# print(all_diffs)

# # MOZE TEZ O COS TAKIEGO CHODZIĆ
# diffs = time_differences_between_every_mic(microphones, velocity, source)
# print(diffs)

# plot
fig = plt.figure(figsize=(7,7))
ax = plt.axes(projection='3d')
ax.scatter(microphones[:,0],microphones[:,1],microphones[:,2], label="Microphones")

ax.scatter(source[0,0], source[0,1], source[0,2], marker="^", s=50, label="Source")

# plot source coordinates so it is visible
ax.scatter(source[0,0], 0, 0,c='r',marker="x", label="Source")
ax.scatter(0, source[0,1], 0,c='r',marker="$y$", label="Source")
ax.scatter(0, 0, source[0,2],c='r',marker="$z$", label="Source")

print(source)
plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.show()

