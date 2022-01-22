import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import wandb
from ray import tune
from torch.nn import *
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from Models.Random_Profile_Picture_Generator_GAN.help_funcs import *
from Models.Random_Profile_Picture_Generator_GAN.load_data import *
from Models.Random_Profile_Picture_Generator_GAN.metrics import *
from Models.Random_Profile_Picture_Generator_GAN.models import *

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["WANDB_SILENT"] = "false"
device = torch.device("cuda")
IMG_SIZE = 224
PROJECT_NAME = "Bob-Ross-Paintings"
transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(0.9, 0.9)
])
