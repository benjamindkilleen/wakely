import numpy as np
import matplotlib.pyplot as plt

# mission day, lat, long, alt (km), (pressure?), horizon alt, azimuth
sun_data = np.load("sun_data.npy")
days = np.zeros(len(sun_data))
alts = np.zeros(len(sun_data))
azims = np.zeros(len(sun_data))

for i in range(len(sun_data)):
    days[i] = sun_data[i,0]
    alts[i] = sun_data[i,5]
    azims[i] = sun_data[i,6]

fig = plt.figure(dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(days, alts, 'r,')
ax.set_xlabel("Projected Mission Day")
ax.set_ylabel("Altitude from Horizon (deg)")
ax.set_title("Altitude of the Sun from Horizon over Projected Flight Path")
plt.savefig("plots/sun_alts.png")
plt.close()

fig = plt.figure(dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(days, azims, 'r,')
ax.set_xlabel("Projected Mission Day")
ax.set_ylabel("Azimuth (deg)")
ax.set_title("Sun Azimuth over Projected Flight Path")
plt.savefig("plots/sun_azims.png")
plt.close()

fig = plt.figure(dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(azims, alts, 'r,')
ax.set_xlabel("Azimuth (deg)")
ax.set_ylabel("Altitude from Horizon (deg)")
ax.set_title("Time Independent Path of Sun over Projected Flight Data")
plt.savefig("plots/sun_azims_vs_alts.png")
plt.close()
