import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Universes
dirt = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'dirt')
load = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'load')
wash_time = ctrl.Consequent(np.arange(0, 60.1, 0.1), 'wash_time')

# Membership functions (trapezoid/triangle)
dirt['low']    = fuzz.trapmf(dirt.universe, [0, 0, 2, 4])
dirt['medium'] = fuzz.trimf(dirt.universe, [3, 5, 7])
dirt['high']   = fuzz.trapmf(dirt.universe, [6, 8, 10, 10])

load['small']  = fuzz.trapmf(load.universe, [0, 0, 2, 4])
load['medium'] = fuzz.trimf(load.universe, [3, 5, 7])
load['large']  = fuzz.trapmf(load.universe, [6, 8, 10, 10])

wash_time['short']  = fuzz.trapmf(wash_time.universe, [0, 0, 10, 20])
wash_time['normal'] = fuzz.trimf(wash_time.universe, [15, 30, 45])
wash_time['long']   = fuzz.trapmf(wash_time.universe, [40, 50, 60, 60])

# Rules
r1 = ctrl.Rule(dirt['low']    & load['small'],  wash_time['short'])
r2 = ctrl.Rule(dirt['medium'] | load['medium'], wash_time['normal'])
r3 = ctrl.Rule(dirt['high']   | load['large'],  wash_time['long'])
r4 = ctrl.Rule(dirt['high']   & load['large'],  wash_time['long'])

# Control system
wm_ctrl = ctrl.ControlSystem([r1, r2, r3, r4])
wm = ctrl.ControlSystemSimulation(wm_ctrl)

# Example input
wm.input['dirt'] = 7.5    # fairly dirty
wm.input['load'] = 6.0    # medium-large load

wm.compute()
print("Recommended wash time (min):", round(wm.output['wash_time'], 1))

# Visualize (optional)
# dirt.view(); load.view(); wash_time.view(sim=wm)

# Output surface (optional)
D = np.linspace(0, 10, 26)
L = np.linspace(0, 10, 26)
DD, LL = np.meshgrid(D, L)
WT = np.zeros_like(DD)
for i in range(DD.shape[0]):
    for j in range(DD.shape[1]):
        sim = ctrl.ControlSystemSimulation(wm_ctrl, flush_after_run=1)
        sim.input['dirt'] = DD[i, j]
        sim.input['load'] = LL[i, j]
        sim.compute()
        WT[i, j] = sim.output['wash_time']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(DD, LL, WT, alpha=0.85, rstride=1, cstride=1)
ax.set_xlabel('Dirt'); ax.set_ylabel('Load'); ax.set_zlabel('Wash Time (min)')
ax.set_title('Washing Machine Fuzzy Controller Output Surface')
plt.show()
