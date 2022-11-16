from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

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

    for i in range(len(times)):
        for j in range(len(times)):
            all_differences[i,j] = times[i] - times[j]

    for i in range(len(times)):
        for j in range(len(times)):
            try:
                if i != 0:
                    time_differences.append({"TDoA_"+str(i)+"_"+str(j+i+1) : all_differences[i,j+i+1]})
                else:
                    time_differences.append({"TDoA_"+str(i)+"_"+str(j+i) : all_differences[i,j+i]})
            except:
                continue

    return distances, times, time_differences, all_differences


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
distances, times, time_differences, all_diffs = tdoa(microphones, velocity, source)
print(distances)
print(times)

print()
print(time_differences)

print()
print(all_diffs)


# plot
plt.figure(figsize=(7,7))
plt.axis(projections='3d')
# plt.scatter(stations[:,0], stations[:,1], marker="^", s=80, label="Receivers")
# plt.scatter(x_true[0], x_true[1], s=40, label="True source position")
# plt.legend(loc=2)
plt.scatter(microphones[:,0],microphones[:,1])
plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.scatter(source[:,0], source[:,1])
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()

