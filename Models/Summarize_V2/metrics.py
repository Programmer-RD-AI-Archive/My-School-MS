from Models.Summarize_V2 import *


def accuracy(model, X, y):
    correct = 0
    total = 0
    preds = model(X)
    for pred, y_batch in zip(preds, y):
        if pred == y_batch:
            correct += 1
        total += 1
    acc = round(correct / total, 3) * 100
    return acc
