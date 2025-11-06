## **Theory**

A **Fuzzy Logic Controller (FLC)** is a rule-based system that mimics human reasoning for decision making under uncertainty.
Instead of using precise numerical inputs, it uses **linguistic variables** (e.g., _poor_, _average_, _good_) and applies **fuzzy rules** to produce smooth, human-like control actions.

---

### **1. Objective**

To design a **Fuzzy Tipping Controller** that determines the **tip percentage** based on two inputs:

- **Service Quality** (0–10)
- **Food Quality** (0–10)

and outputs:

- **Tip (%)** (0–25)

---

### **2. Fuzzy Variables and Membership Functions**

| Variable | Type   | Linguistic Terms    | Range |
| -------- | ------ | ------------------- | ----- |
| Service  | Input  | Poor, Average, Good | 0–10  |
| Quality  | Input  | Poor, Average, Good | 0–10  |
| Tip      | Output | Low, Medium, High   | 0–25  |

Membership functions are **triangular**, representing gradual transitions between terms.

---

### **3. Rule Base (Mamdani Type)**

1. IF _Service_ is **Poor** OR _Quality_ is **Poor**, THEN _Tip_ is **Low**
2. IF _Service_ is **Average**, THEN _Tip_ is **Medium**
3. IF _Service_ is **Good** OR _Quality_ is **Good**, THEN _Tip_ is **High**

These rules form a **Mamdani inference system**, where both antecedent and consequent are fuzzy sets.

---

### **4. Working Principle**

1. **Fuzzification:**
   Converts crisp inputs (quality, service) into fuzzy degrees using membership functions.

2. **Rule Evaluation:**
   Applies the defined IF–THEN rules using fuzzy logic operations (AND, OR, MIN, MAX).

3. **Aggregation:**
   Combines outputs from all rules into a single fuzzy set for the “tip.”

4. **Defuzzification:**
   Converts the fuzzy result back into a crisp numeric tip value (using the **centroid** method).

---

### **5. Output Behavior**

- When both _service_ and _quality_ are poor → **Low Tip** (~0–5%)
- When both are average → **Medium Tip** (~10–15%)
- When both are good → **High Tip** (~20–25%)

The controller smoothly transitions between these levels based on fuzzy reasoning.

---

### **6. Advantages**

- Handles vague or imprecise input data.
- Simple, rule-based design—no mathematical model needed.
- Produces smooth, human-like control decisions.

### **7. Disadvantages**

- Rule base must be carefully defined.
- Performance depends on shape and number of membership functions.
- Not ideal for high-dimensional or rapidly changing systems.

---

### **Conclusion**

The **Fuzzy Tipping Controller** demonstrates how **Mamdani Fuzzy Inference** can model real-life decision making.
By combining linguistic rules and fuzzy logic, it provides a logical yet flexible way to compute tips based on subjective inputs like service and food quality.
