import torch, torchvision
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
import matplotlib.pyplot as plt

# ---- Data ----
tfm = transforms.Compose([transforms.ToTensor(),
                          transforms.Normalize((0.5,), (0.5,))])

train_set = torchvision.datasets.MNIST(root="./data", train=True,  download=True, transform=tfm)
test_set  = torchvision.datasets.MNIST(root="./data", train=False, download=True, transform=tfm)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)
test_loader  = torch.utils.data.DataLoader(test_set,  batch_size=256, shuffle=False)

# ---- Model (784 -> 128 -> 64 -> 10) ----
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28, 128), nn.ReLU(),
    nn.Linear(128, 64),    nn.ReLU(),
    nn.Linear(64, 10)      # logits
)

# ---- Loss/Opt ----
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# ---- Train ----
EPOCHS = 3
for epoch in range(1, EPOCHS+1):
    model.train()
    running = 0.0
    for x, y in train_loader:
        optimizer.zero_grad()
        out = model(x)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        running += loss.item()
    print(f"Epoch {epoch}/{EPOCHS} - Loss: {running/len(train_loader):.4f}")

# ---- Test Acc ----
model.eval()
correct, total = 0, 0
with torch.no_grad():
    for x, y in test_loader:
        pred = model(x).argmax(1)
        total += y.size(0)
        correct += (pred == y).sum().item()
print(f"Test Accuracy: {100*correct/total:.2f}%")

# ---- Show one prediction ----
x, y = next(iter(test_loader))
with torch.no_grad():
    probs = model(x[:1]).softmax(1).squeeze()
pred_cls = probs.argmax().item()

plt.imshow(x[0].squeeze(), cmap="gray")
plt.title(f"Pred: {pred_cls}  (conf: {probs[pred_cls]:.2f})")
plt.axis("off")
plt.show()
