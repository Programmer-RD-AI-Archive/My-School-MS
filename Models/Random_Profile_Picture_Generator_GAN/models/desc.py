from Models.Random_Profile_Picture_Generator_GAN import *


class Desc(nn.Module):
    def __init__(self, activation=nn.LeakyReLU, starter=16):
        super().__init__()
        self.dis = nn.Sequential(
            nn.Conv2d(3, 4, 3),
            activation(),
            nn.Conv2d(4, 8, 3),
            activation(),
        )
        self.dis2 = nn.Sequential(
            nn.Linear(387200, starter),
            activation(),
            nn.Linear(starter, starter * 2),
            activation(),
            nn.Linear(starter * 2, starter),
            activation(),
            nn.Linear(starter, 1),
            nn.Sigmoid(),
        )

    def forward(self, x, shape=False):
        x = x.view(-1, 3, IMG_SIZE, IMG_SIZE)
        x = self.dis(x)
        if shape:
            print(x.shape)
        x = x.view(-1, 387200)
        x = self.dis2(x)
        return x
