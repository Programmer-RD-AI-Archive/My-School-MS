from Models.Random_Profile_Picture_Generator_GAN import *


class Gen(nn.Module):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self, z_dim, activation=nn.LeakyReLU, starter=256):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().__init__()
        self.gen = nn.Sequential(
            nn.Linear(z_dim, starter),
            activation(),
            nn.Linear(starter, starter * 2),
            activation(),
            nn.Linear(starter * 2, starter * 4),
            activation(),
            nn.Linear(starter * 4, starter * 2),
            activation(),
            nn.Linear(starter * 2, IMG_SIZE * IMG_SIZE * 3),
            nn.Tanh(),
        )

    def forward(self, x):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.gen(x)
