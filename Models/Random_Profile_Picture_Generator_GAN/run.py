from Models.Random_Profile_Picture_Generator_GAN import *

IMG_SIZE = 56
X = load_data(directory="./data/")
np.save("./data.npy", np.array(X))
X = np.load("./data.npy")

z_dim = 64
gen = Gen(z_dim).to(device)
desc = Desc().to(device)
lr = 3e-4
batch_size = 32
epochs = 250
criterion = nn.BCELoss()
optimizer_gen = torch.optim.Adam(gen.parameters(), lr=lr)
optimizer_desc = torch.optim.Adam(desc.parameters(), lr=lr)
fixed_noise = torch.randn((batch_size, z_dim)).to(device)
