from Models.Summarize_V2 import *


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
        self.linear1 = Linear(len(all_words_X), 1024)
        self.linear2 = Linear(1024, 1024)
        self.output = Linear(1024, len(all_words_y))

    def forward(self, X):
        preds = self.activation(self.linear1(X))
        for _ in range(self.iters):
            preds = self.activation(self.linear2(preds))
        preds = self.output(preds)
        return preds
