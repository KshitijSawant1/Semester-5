### **Experiment 9 – Automobile Speed Control using ANFIS Hybrid System**

---

### **1. Theory**

* **ANFIS (Adaptive Neuro-Fuzzy Inference System)** merges fuzzy logic and neural networks.
* Fuzzy rules express human-like reasoning (“If slope ↑ and speed ↓ → increase throttle”).
* Neural learning adjusts membership functions and rule weights automatically.
* The system learns input–output relations from data to maintain vehicle speed under varying road slopes and loads.
* Uses a **Sugeno-type FIS** trained by a **hybrid algorithm** (least-squares + back-propagation).

---

### **2. Working (Detailed)**

1. **Inputs (Slope Angle, Throttle %)**

   * Represent external driving conditions and driver’s torque demand.
   * Provide real-time data that influence vehicle acceleration and control response.

2. **Error (e) and Change in Error (de)**

   * Error = (Desired Speed – Actual Speed); Change in Error shows how fast the error is varying.
   * These values form the control feedback that guides throttle adjustments.

3. **Scaling with Gains (Ke, Kde, Ku)**

   * Ke and Kde normalize the input signals to fit within fuzzy inference limits.
   * Ku scales the final output signal to suitable actuator range for throttle/brake control.
  
| Symbol  | Full Form       | Acts On                 | Role                            | Formula                  |
| ------- | --------------- | ----------------------- | ------------------------------- | ------------------------ |
| **Ke**  | Error Gain      | Error (e)               | Normalizes speed difference     | e(scaled) = Ke X e       |
| **Kde** | Derivative Gain | Change of error (de/dt) | Normalizes rate of error change | de(scaled) = Kde X de/dt |
| **Ku**  | Output Gain     | Control signal (u)      | Denormalizes fuzzy output       | u(final) = Ku X u(fuzzy) |


4. **ANFIS Controller Core (Fuzzy + Neural Integration)**

   * Fuzzy logic layer interprets linguistic rules such as “If error is small and decreasing → reduce throttle.”
   * Neural learning layer continuously tunes membership functions and rule weights for optimal behavior.

5. **ACO Optimization Loop (Metaheuristic Layer)**

   * Ant Colony Optimization fine-tunes Ke, Kde, Ku, λ, μ to minimize control error metrics (IAE, ISE, RMSE).
   * Ants explore multiple parameter paths and reinforce best-performing combinations through pheromone updating.

6. **Vehicle Dynamics Block (Plant Model)**

   * Receives control signal *u(t)* and converts it into vehicle speed response based on inertia and load.
   * Provides nonlinear simulation of real-world conditions like slope variation and friction.

7. **Feedback and Convergence**

   * The actual speed is continuously fed back to recalculate the new error.
   * Once minimal error and steady-state stability are achieved, final optimal parameters are fixed for the ANFIS controller.

---

### **3. Block Diagram (with Explanation)**

```
   Desired Speed ─┐
                  │
                  ▼
          [ Error (e) & ΔError (de) ]
                  │
         (Scaled by Ke, Kde, Ku)
                  │
     ┌────────────────────────────┐
     │       ANFIS Controller     │
     │  - Fuzzy Logic + NN Layer  │
     │  - ACO Optimization Loop   │
     └────────────────────────────┘
                  │
         Engine Control Signal (u)
                  ▼
        [ Vehicle Dynamics Model ]
      - Simulates speed response
      - Feeds back actual speed
                  │
                  ▼
         [ Feedback & Update ]
      - Error recalculated
      - Parameters adjusted
```

---


### **4. Advantages**

* Automatically adapts to nonlinear and varying road conditions.
* Requires little manual tuning once trained.
* Provides smooth and stable speed response.
* Combines interpretability of fuzzy logic with learning power of neural nets.

---

### **5. Disadvantages**

* High computational cost during training.
* Performance depends on quality of training data.
* Choosing initial membership functions is critical.
* Real-time hardware implementation may be resource-intensive.

---
