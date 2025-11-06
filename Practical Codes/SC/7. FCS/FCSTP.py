import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Fuzzy variables
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip     = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Membership functions (auto for inputs, simple triangles for output)
quality.automf(3)          # poor / average / good
service.automf(3)
tip['low']    = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high']   = fuzz.trimf(tip.universe, [13, 25, 25])

# Rules
rules = [
    ctrl.Rule(quality['poor']  | service['poor'],  tip['low']),
    ctrl.Rule(service['average'],                  tip['medium']),
    ctrl.Rule(service['good']  | quality['good'],  tip['high'])
]

# Build once
system = ctrl.ControlSystem(rules)

def recommend_tip(q, s):
    sim = ctrl.ControlSystemSimulation(system)
    sim.input['quality'] = q
    sim.input['service'] = s
    sim.compute()
    return sim.output['tip']

# Example
print("Tip for quality=6.5, service=9.8 ->", round(recommend_tip(6.5, 9.8), 2), "%")
