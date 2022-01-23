from Models.Random_Profile_Picture_Generator_GAN import *


def train(
    gen,
    desc,
    X,
    z_dim,
    device,
    criterion,
    optimizer_gen,
    optimizer_desc,
    epochs,
    batch_size,
    IMG_SIZE,
):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    wandb.init(project=PROJECT_NAME, name="baseline-with-backward-pass-gen")
    for epoch in tqdm(epochs):
        for idx in range(0, len(X), batch_size):
            X_batch = (torch.tensor(np.array(X[idx:idx + batch_size])).view(
                -1, IMG_SIZE * IMG_SIZE * 3).to(device))
            batch_size = X_batch.shape[0]
            noise = torch.randn(batch_size, z_dim).to(device)
            fake = gen(noise)
            desc_real = desc(X_batch).view(-1)
            lossD_real = criterion(desc_real, torch.ones_like(desc_real))
            desc_fake = desc(fake).view(-1)
            lossD_fake = criterion(desc_fake, torch.zeros_like(desc_fake))
            lossD = (lossD_real + lossD_fake) / 2
            desc.zero_grad()
            lossD.backward(retain_graph=True)
            wandb.log({"lossD": lossD.item()})
            optimizer_desc.step()
            output = desc(fake).view(-1)
            lossG = criterion(output, torch.ones_like(output))
            gen.zero_grad()
            wandb.log({"lossG": lossG.item()})
            lossG.backward()
            wandb.log({"lossG": lossG.item()})
            optimizer_gen.step()
    with torch.no_grad():
        fake = gen(noise).view(-1, 3, IMG_SIZE, IMG_SIZE)
        img_grid_fake = torchvision.utils.make_grid(fake, normalize=True)
        wandb.log({"img": wandb.Image(img_grid_fake)})
    return None
