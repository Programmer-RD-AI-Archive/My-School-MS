from Models.Rock_Paper_Scissors import *


def get_loss(model, X, y, criterion):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    preds = model(X)
    loss = criterion(preds, y)
    return loss.item()


def get_accuracy(model, X, y):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    correct = 0
    total = 0
    preds = model(X)
    for pred, y_batch in zip(preds, y):
        pred = int(torch.argmax(pred))
        if pred == y_batch:
            correct += 1
        total += 1
    acc = round(correct / total, 3) * 100
    return acc


def get_pred(model):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    model.eval()
    for file in os.listdir("./test_data/"):
        img = cv2.imread(f"./test_data/{file}")
        img = cv2.resize(img, (112, 112))
        img = (torch.from_numpy(np.array(img / 255.0)).to(device).view(
            -1, 3, 112, 112).float())
        pred = model(img)
        pred = torch.argmax(pred)
        plt.figure(figsize=(12, 6))
        plt.imshow(img.view(112, 112, 3).cpu().detach().numpy())
        plt.title(f"{labels[int(pred)]}")
        plt.savefig(f"./preds/{file}")
        plt.close()
    model.train()
