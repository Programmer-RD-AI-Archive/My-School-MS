from Models.Bullying import *


class Model(Module):
    def __init__(self):
        super().__init__()
        self.iters = 10
        self.activation = ReLU()
        self.linear1 = Linear(len(words), 512).to(device)
        self.linear2 = Linear(512, 512).to(device)
        self.output = Linear(512, len(labels)).to(device)

    def forward(self, X):
        preds = self.linear1(X)
        for _ in range(self.iters):
            preds = self.activation(self.linear2(preds))
        preds = self.output(preds)
        return preds
