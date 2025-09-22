import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Universes
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Auto-membership (triangular sets for 3 qualities: poor/average/good)
quality.automf(3)   # poor, average, good
service.automf(3)   # poor, average, good

# Custom output MFs
tip['low']    = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high']   = fuzz.trimf(tip.universe, [13, 25, 25])

# Rules
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'],                tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Example input
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Compute
tipping.compute()

print("Recommended tip (%):", round(tipping.output['tip'], 2))

q = np.linspace(0, 10, 21)
s = np.linspace(0, 10, 21)
Q, S = np.meshgrid(q, s)
Z = np.zeros_like(Q)
for i in range(Q.shape[0]):
    for j in range(Q.shape[1]):
        sim = ctrl.ControlSystemSimulation(tipping_ctrl, flush_after_run=1)
        sim.input['quality'] = Q[i, j]
        sim.input['service'] = S[i, j]
        sim.compute()
        Z[i, j] = sim.output['tip']

# Plot surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Q, S, Z, alpha=0.8, rstride=1, cstride=1)
ax.set_xlabel('Quality'); ax.set_ylabel('Service'); ax.set_zlabel('Tip (%)')
ax.set_title('Fuzzy Tipping Controller Output Surface')
plt.show()
