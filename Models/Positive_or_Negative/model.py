from Models.Positive_or_Negative import *


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
        self.linear1 = Linear(len(words), 512)
        self.linear2 = Linear(512, 512)
        self.linear2bn = BatchNorm1d(512)
        self.output = Linear(512, len(labels))

    def forward(self, X):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        preds = self.linear1(X)
        for _ in range(self.iters):
            preds = self.activation(self.linear2bn(self.linear2(preds)))
        preds = self.output(preds)
        return preds
