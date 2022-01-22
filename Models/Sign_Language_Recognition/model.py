from Models.Sign_Language_Recognition import *


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.pool = nn.MaxPool2d((2, 2))
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.conv3 = nn.Conv2d(32, 64, 5)
        self.conv2 = nn.Conv2d(64, 128, 5)
        self.fc1 = nn.Linear(128 * 10 * 10, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc4 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 36)
        self.activation = nn.SELU()

    def forward(self, x, shape=False):
        x = self.pool(self.activation(self.conv1(x)))
        x = self.pool(self.activation(self.conv3(x)))
        x = self.pool(self.activation(self.conv2(x)))
        x = x.view(-1, 128 * 10 * 10)
        x = self.activation(self.fc1(x))
        x = self.activation(self.fc2(x))
        x = self.activation(self.fc4(x))
        x = self.fc3(x)
        return x
