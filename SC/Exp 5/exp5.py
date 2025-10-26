import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),torchvision.transforms.Normalize((0.5,),(0.5,))])

train_set = torchvision.datasets.MNIST(root='./data',train=True,download=True,transform=transform)
test_set = torchvision.datasets.MNIST(root='./data',train=False,download=True,transform=transform)

train_loader = torch.utils.data.DataLoader(train_set,batch_size=32,shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set,batch_size=32,shuffle=False)

print()
print(f'Number of images in the training dataset: {len(train_set)}')
print()
print(f'Number of images in the testing dataset: {len(test_set)}')
print()
print(f"Shape of the images in the training dataset: {test_loader.dataset[0][0].shape}")
plt.show()


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork,self).__init__()
        self.input = nn.Linear(28*28,128)           # 28 * 28 = 728 input values and outputs 128 values
        self.hidden = nn.Linear(128,64)             # First Hidden Layer has 128 input neurons and 64 Activation Values 
        self.output = nn.Linear(64,10)              # Output Layer Takes 64 Activations and Turns them in 10 each for one digit 
        
    def forward(self,x):                            # input x is a 2D Array of Size 28 * 28
        x = x.view(-1,28*28)                        # Falten this 2D Array of length vector of 724 
        x = F.relu(self.input(x))
        x = F.relu(self.hidden(x))
        x = F.log_softmax(self.output(x),dim=1)     # the 10 Activations are feed to softmax function to turn thme into probability 
        return x
    
model = NeuralNetwork()


# here Backpropagation is used it check a input and 
# if correct then goes ahead otherwise 
# tweaks the neuron in the netwokr it does it until it gets the correct answers 
# then  we are checking the log of the probablity that gives a higher values on lower probability after that negate the log 

loss_function = nn.NLLLoss()                        # optimizer for working with log probability
optimizer = optim.Adam(model.parameters(),lr=0.001) # Adam is one of the implementation of backpropagation

print()
epochs = 5

for epoch in range(epochs):
    for images , labels in train_loader:
        optimizer.zero_grad()
        
        output = model(images)
        loss = loss_function(output,labels)
        
        loss.backward()
        optimizer.step()
        
    print(f'Epoch [{epoch+1}{epochs}],Loss: {loss.item():4f}')
    
print()

def view_classify(image, probabilities):
    probabilities = probabilities.data.numpy().squeeze()

    fig, (ax1, ax2) = plt.subplots(figsize=(6, 9), ncols=2)
    ax1.imshow(image.numpy().squeeze(), cmap='gray')
    ax1.axis('off')

    ax2.barh(np.arange(10), probabilities)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    ax2.set_yticklabels(np.arange(10))
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)

    plt.tight_layout()
    plt.show()

images, _ = next(iter(test_loader))
image = images[0]

with torch.no_grad():
    log_probabilities = model(image)

probabilities = torch.exp(log_probabilities)
view_classify(image, probabilities)


correct = 0 
total = 0 
with torch.no_grad():
    for images, labels in test_loader:
        output = model (images)
        _,predicted = torch.max(output,1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
print()
print(f'Accuracy of the neural network on the {total} test images : {100* correct /total}%')

def show_predictions_for_all_digits_grid(model, test_loader):
    model.eval()
    shown_digits = set()
    digit_images = [None] * 10
    digit_probs = [None] * 10

    with torch.no_grad():
        for images, labels in test_loader:
            for i in range(images.size(0)):
                label = labels[i].item()
                if label not in shown_digits:
                    image = images[i]
                    log_prob = model(image.unsqueeze(0))
                    prob = torch.exp(log_prob)

                    digit_images[label] = image
                    digit_probs[label] = prob.squeeze()
                    shown_digits.add(label)

                    if len(shown_digits) == 10:
                        break
            if len(shown_digits) == 10:
                break

    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(5, 4, width_ratios=[1, 2, 1, 2], hspace=0.6, wspace=0.5)

    for idx in range(10):
        row = idx // 2
        col_base = (idx % 2) * 2  # 0 or 2 for first or second digit in the row

        image = digit_images[idx]
        probs = digit_probs[idx].numpy()

        # Image subplot
        ax_img = plt.subplot(gs[row, col_base])
        ax_img.imshow(image.squeeze().numpy(), cmap='gray')
        ax_img.axis('off')
        ax_img.set_title(f"Digit: {idx}", fontsize=12)

        # Probability bar chart subplot
        ax_bar = plt.subplot(gs[row, col_base + 1])
        ax_bar.barh(np.arange(10), probs, color='steelblue')
        ax_bar.set_yticks([0, 5, 9])
        ax_bar.set_yticklabels([0, 5, 9])
        ax_bar.set_xlim(0, 1.1)
        ax_bar.set_title("Probabilities", fontsize=10)
        ax_bar.invert_yaxis()
        ax_bar.tick_params(labelsize=8)

    plt.tight_layout()
    plt.show()

show_predictions_for_all_digits_grid(model, test_loader)
