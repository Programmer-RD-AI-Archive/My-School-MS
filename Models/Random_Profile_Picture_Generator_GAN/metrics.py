from Models.Random_Profile_Picture_Generator_GAN import *


def accuracy_fake(desc_fake):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    correct = 0
    total = 0
    preds = np.round(np.array(desc_fake.cpu().detach().numpy()))
    for pred in preds:
        if pred == 0:
            correct += 1
        total += 1
    return round(correct / total, 3)


def accuracy_real(desc_real):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    correct = 0
    total = 0
    preds = np.round(np.array(desc_real.cpu().detach().numpy()))
    for pred in preds:
        if pred == 1:
            correct += 1
        total += 1
    return round(correct / total, 3)
