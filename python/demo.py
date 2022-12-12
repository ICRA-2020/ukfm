import ukfm
import numpy as np
import matplotlib
ukfm.utils.set_matplotlib_config()

MODEL = ukfm.LOCALIZATION

# sequence time (s)
T = 40
# odometry frequency (Hz)
odo_freq = 100
#  create the model
model = MODEL(T, odo_freq)
# odometry noise standard deviation
odo_std = np.array([0.01,          # longitudinal speed (v/m)
                    0.01,          # transverse shift speed (v/m)
                    1/180*np.pi])  # differential odometry (rad/s)
# radius of the circle trajectory (m)
radius = 5
# simulate trajectory
states, omegas = model.simu_f(odo_std, radius)

# GPS frequency (Hz)
gps_freq = 1
# GPS noise standard deviation (m)
gps_std = 1
# simulate measurements
ys, one_hot_ys = model.simu_h(states, gps_freq, gps_std)

model.plot_traj(states, ys)

matplotlib.pyplot.show()

