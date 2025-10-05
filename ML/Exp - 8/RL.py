# rl_qlearning_gridworld.py
# Minimal, from-scratch Q-Learning on a 2D GridWorld (no gym required)

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# -----------------------------
# 1) Simple GridWorld environment
# -----------------------------
class GridWorld:
    """
    0 1 2 3
    1 . . G
    2 . # .
    3 S . X

    S: start, G: goal(+1), X: pit(-1), #: wall (blocked)
    Reward: -0.01 per step, +1 on goal, -1 in pit. Episode ends at G or X.
    """
    def __init__(self, h=4, w=4):
        self.h, self.w = h, w
        self.start = (3, 0)
        self.goal  = (1, 3)
        self.pit   = (3, 2)
        self.wall  = (2, 1)
        self.state = self.start
        self.action_space = 4  # 0:UP, 1:RIGHT, 2:DOWN, 3:LEFT

    def reset(self):
        self.state = self.start
        return self._s2i(self.state)

    def step(self, a):
        r, c = self.state
        if a == 0: nr, nc = r - 1, c
        elif a == 1: nr, nc = r, c + 1
        elif a == 2: nr, nc = r + 1, c
        else: nr, nc = r, c - 1

        # stay inside grid
        nr = np.clip(nr, 0, self.h - 1)
        nc = np.clip(nc, 0, self.w - 1)

        # block the wall cell
        if (nr, nc) == self.wall:
            nr, nc = r, c

        self.state = (nr, nc)

        # rewards and termination
        reward = -0.01
        done = False
        if self.state == self.goal:
            reward, done = 1.0, True
        elif self.state == self.pit:
            reward, done = -1.0, True

        return self._s2i(self.state), reward, done

    def _s2i(self, s):  # (r,c) -> integer index
        return s[0] * self.w + s[1]

    def _i2s(self, i):  # index -> (r,c)
        return (i // self.w, i % self.w)

    def render_policy(self, Q):
        arrows = {0: "↑", 1: "→", 2: "↓", 3: "←"}
        grid = np.full((self.h, self.w), "·", dtype=object)
        grid[self.start] = "S"
        grid[self.goal]  = "G"
        grid[self.pit]   = "X"
        grid[self.wall]  = "#"
        for s in range(self.h * self.w):
            rc = self._i2s(s)
            if rc in [self.start, self.goal, self.pit, self.wall]:
                continue
            a = np.argmax(Q[s])
            grid[rc] = arrows[a]
        print("\nGreedy Policy (arrows):")
        for r in range(self.h):
            print(" ".join(grid[r]))


# -----------------------------
# 2) Q-Learning
# -----------------------------
env = GridWorld()
n_states = env.h * env.w
n_actions = env.action_space

Q = np.zeros((n_states, n_actions))

alpha = 0.1        # learning rate
gamma = 0.99       # discount
epsilon = 1.0      # exploration rate (ε-greedy)
eps_min = 0.05
eps_decay = 0.995

episodes = 2000
rewards_history = []

rng = np.random.default_rng(0)

for ep in range(episodes):
    s = env.reset()
    done = False
    ep_reward = 0.0

    while not done:
        # ε-greedy action selection
        if rng.random() < epsilon:
            a = rng.integers(n_actions)
        else:
            a = np.argmax(Q[s])

        s_next, r, done = env.step(a)
        ep_reward += r

        # TD target and update
        td_target = r + gamma * (0 if done else np.max(Q[s_next]))
        Q[s, a] += alpha * (td_target - Q[s, a])

        s = s_next

    rewards_history.append(ep_reward)
    epsilon = max(eps_min, epsilon * eps_decay)

print(f"Training finished. Final ε = {epsilon:.3f}")

# -----------------------------
# 3) Inspect learned policy and value
# -----------------------------
env.render_policy(Q)

V = Q.max(axis=1).reshape(env.h, env.w)
print("\nState-value (max Q) grid:\n", np.round(V, 2))

# -----------------------------
# 4) Plot learning curve
# -----------------------------
window = 50
running_avg = np.convolve(rewards_history, np.ones(window)/window, mode="valid")

plt.figure(figsize=(8,4))
plt.plot(rewards_history, alpha=0.4, label="Episode return")
plt.plot(range(window-1, episodes), running_avg, lw=2, label=f"{window}-ep moving avg")
plt.axhline(0.0, color="k", ls="--", lw=1)
plt.xlabel("Episode")
plt.ylabel("Return")
plt.title("Q-Learning on GridWorld")
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------
# 5) Demo a greedy episode
# -----------------------------
s = env.reset()
done = False
path = [env._i2s(s)]
while not done and len(path) < 50:
    a = np.argmax(Q[s])
    s, r, done = env.step(a)
    path.append(env._i2s(s))

print("\nGreedy path from S:", path)
