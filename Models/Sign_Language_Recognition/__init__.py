import os
import random

import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import wandb
from tqdm import tqdm

from Models.Sign_Language_Recognition.help_funcs import *
from Models.Sign_Language_Recognition.metrics import *
from Models.Sign_Language_Recognition.model import *

PROJECT_NAME = "Sign-Language-Recognition"

NAME = "change the conv2d"
BATCH_SIZE = 32
device = torch.device("cuda")
