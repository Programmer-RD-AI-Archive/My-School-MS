import os
import cv2
import torch
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm
import wandb
import random

PROJECT_NAME = "Sign-Language-Recognition"

NAME = "change the conv2d"
BATCH_SIZE = 32
device = torch.device("cuda")

from Models.Sign_Language_Recognition.help_funcs import *
from Models.Sign_Language_Recognition.metrics import *
from Models.Sign_Language_Recognition.model import *
