from Models.Summarize import *


class Model(Module):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().__init__()
        self.activation = ReLU()
        self.iters = 10
        self.linear1 = Linear(len(X_words), 256)
        self.linear2 = Linear(256, 256)
        self.linear2bn = BatchNorm1d(256)
        self.output = Linear(256, len(y_words))

    def forward(self, X):
        preds = self.linear1(X)
        for _ in range(self.iters):
            preds = self.activation(self.linear2bn(self.linear2(preds)))
        preds = self.output(preds)
        return preds
