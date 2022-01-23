from Models.Sign_Language_Recognition import *


def test(net, X, y):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    device = "cpu"
    net.to(device)
    correct = 0
    total = 0
    net.eval()
    with torch.no_grad():
        for i in range(len(X)):
            real_class = torch.argmax(y[i]).to(device)
            net_out = net(X[i].view(-1, 1, 112, 112).to(device).float())
            net_out = net_out[0]
            predictied_class = torch.argmax(net_out)
            if predictied_class == real_class:
                correct += 1
            total += 1
    net.train()
    net.to("cuda")
    return round(correct / total, 3)


def get_loss(criterion, y, model, X):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    model.to("cpu")
    preds = model(X.view(-1, 1, 112, 112).to("cpu").float())
    preds.to("cpu")
    loss = criterion(preds, torch.tensor(y, dtype=torch.long).to("cpu"))
    loss.backward()
    return loss.item()
