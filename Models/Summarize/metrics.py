from Models.Summarize import *


def get_accuracy(model, X, y):
    preds = model(X)
    correct = 0
    total = 0
    for pred, yb in zip(preds, y):
        for pred_in_pred, yb_in_yb in zip(pred, yb):
            pred_in_pred = int(torch.argmax(pred_in_pred))
            yb_in_yb = int(yb_in_yb)
            if pred_in_pred == yb_in_yb:
                correct += 1
            total += 1
    acc = round(correct / total, 3) * 100
    return acc


def get_loss(model, X, y, criterion):
    preds = model(X)
    loss = criterion(preds, y)
    return loss.item()
