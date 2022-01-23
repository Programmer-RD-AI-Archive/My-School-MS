from Models.Rock_Paper_Scissors import *


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
        self.max_pool2d = MaxPool2d((2, 2), (2, 2))
        self.activation = ReLU()
        self.conv1 = Conv2d(3, 6, (5, 5))
        self.conv1batchnorm = BatchNorm2d(6)
        self.conv2 = Conv2d(6, 9, (5, 5))
        self.conv2batchnorm = BatchNorm2d(9)
        self.conv3 = Conv2d(9, 12, (5, 5))
        self.conv3batchnorm = BatchNorm2d(12)
        self.conv4 = Conv2d(12, 15, (5, 5))
        self.conv4batchnorm = BatchNorm2d(15)
        self.linear1 = Linear(15 * 3 * 3, 512)
        self.linear1batchnorm = BatchNorm1d(512)
        self.linear2 = Linear(512, 1024)
        self.linear2batchnorm = BatchNorm1d(1024)
        self.linear3 = Linear(1024, 2048)
        self.linear3batchnorm = BatchNorm1d(2048)
        self.linear4 = Linear(2048, 1024)
        self.linear4batchnorm = BatchNorm1d(1024)
        self.output = Linear(1024, 3)

    def forward(self, X):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        preds = self.max_pool2d(
            self.activation(self.conv1batchnorm(self.conv1(X))))
        preds = self.max_pool2d(
            self.activation(self.conv2batchnorm(self.conv2(preds))))
        preds = self.max_pool2d(
            self.activation(self.conv3batchnorm(self.conv3(preds))))
        preds = self.max_pool2d(
            self.activation(self.conv4batchnorm(self.conv4(preds))))
        #         print(preds.shape)
        preds = preds.view(-1, 15 * 3 * 3)
        preds = self.activation(self.linear1batchnorm(self.linear1(preds)))
        preds = self.activation(self.linear2batchnorm(self.linear2(preds)))
        preds = self.activation(self.linear3batchnorm(self.linear3(preds)))
        preds = self.activation(self.linear4batchnorm(self.linear4(preds)))
        preds = self.output(preds)
        return preds
