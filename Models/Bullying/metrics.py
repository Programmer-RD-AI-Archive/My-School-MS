from Models.Bullying import *


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
    preds = model(X)
    correct = 0
    total = 0
    for pred, y_batch in zip(preds, y):
        pred = int(torch.argmax(pred))
        y_batch = int(torch.argmax(y_batch))
        if pred == y_batch:
            correct += 1
        total += 1
    acc = round(correct / total, 3) * 100
    return acc
