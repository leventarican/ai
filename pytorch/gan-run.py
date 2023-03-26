import torch
import torch.nn as nn

from torchvision.utils import save_image
from torchvision import transforms

# Define the generator network
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 784),
            nn.Tanh()
        )

    def forward(self, x):
        out = self.model(x)
        out = out.view(out.size(0), 1, 28, 28)
        return out

# Load the saved generator model
generator = Generator()
generator.load_state_dict(torch.load('generator.pth'))

# Generate new fake images
num_images = 3
noise = torch.randn(num_images, 100)
fake_images = generator(noise)

# Save the generated images to a file
for i in range(num_images):
    save_image(fake_images[i], f'fake_image_{i}.png')
