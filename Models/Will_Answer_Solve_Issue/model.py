from Models.Will_Answer_Solve_Issue import *


class Model(Module):
    def __init__(self):
        super().__init__()
        self.hidden = 8
        self.activation = ReLU()
        self.bn = BatchNorm1d(self.hidden)
        self.linear1 = Linear(len(words), self.hidden)
        self.linear2 = Linear(self.hidden, self.hidden)
        self.linear3 = Linear(self.hidden, len(labels))

    def forward(self, X):
        preds = self.linear1(X)
        preds = self.activation(self.bn(self.linear2(preds)))
        preds = self.linear3(preds)
        return preds
