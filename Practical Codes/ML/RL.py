# ==== Reinforcement Learning (Q-Learning) ====
# Formula:
# Q(s, a) ← Q(s, a) + α [r + γ * max(Q(s', a')) - Q(s, a)]
# where:
# s  = current state
# a  = action taken
# r  = reward received
# s' = next state
# α  = learning rate
# γ  = discount factor

import numpy as np

# ---- Simple Environment (4 states, 2 actions) ----
n_states = 4
n_actions = 2
Q = np.zeros((n_states, n_actions))

# Hyperparameters
alpha = 0.1   # Learning rate
gamma = 0.9   # Discount factor
episodes = 1000

# Rewards: simple grid where goal is state 3
rewards = [0, 0, 0, 1]

for episode in range(episodes):
    state = np.random.randint(0, n_states - 1)  # start randomly
    done = False
    while not done:
        action = np.random.choice(n_actions)
        next_state = (state + 1) % n_states
        reward = rewards[next_state]

        # Q-learning update
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])

        if next_state == 3:  # goal reached
            done = True
        state = next_state

# ---- Evaluate Success ----
successes = sum(np.argmax(Q, axis=1) == np.argmax(rewards))
accuracy = successes / n_states

print("Q-Table:\n", np.round(Q, 3))
print(f"Success Rate (Accuracy Equivalent): {accuracy:.2f}")
