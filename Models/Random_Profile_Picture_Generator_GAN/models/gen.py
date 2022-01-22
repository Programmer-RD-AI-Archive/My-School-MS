class Gen(nn.Module):
    def __init__(self, z_dim, activation=nn.LeakyReLU, starter=256):
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
        return self.gen(x)
