import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision
import wandb
from sklearn.model_selection import train_test_split
from torch.nn import *
from torch.optim import *
from tqdm import tqdm

from Models.Rock_Paper_Scissors.help_funcs import *
from Models.Rock_Paper_Scissors.metrics import *
from Models.Rock_Paper_Scissors.models.cnn import *

device = "cuda"
PROJECT_NAME = "Rock-Paper-Scissors-Clf"
