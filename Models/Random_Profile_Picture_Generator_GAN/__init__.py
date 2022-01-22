import cv2
import os
import torch, torchvision
import torch.nn as nn
import numpy as np
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import torch.optim as optim
from torch.nn import *
from torch.utils.tensorboard import SummaryWriter
import matplotlib.pyplot as plt
import wandb
from ray import tune
import os

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["WANDB_SILENT"] = "false"
device = torch.device("cuda")
IMG_SIZE = 224
PROJECT_NAME = "Bob-Ross-Paintings"
transforms = torchvision.transforms.Compose(
    [torchvision.transforms.ToTensor(), torchvision.transforms.Normalize(0.9, 0.9)]
)

from Models.Random_Profile_Picture_Generator_GAN.models import *
from Models.Random_Profile_Picture_Generator_GAN.load_data import *
from Models.Random_Profile_Picture_Generator_GAN.metrics import *
from Models.Random_Profile_Picture_Generator_GAN.help_funcs import *
