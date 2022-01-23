import random

import nltk
import numpy as np
import pandas as pd
import torch
import torchvision
import wandb
from nltk.stem.porter import *
from torch.nn import *
from torch.optim import *
from torch.utils.data import DataLoader, Dataset
from tqdm import *

from Models.Summarize_V2.help_funcs import *
from Models.Summarize_V2.metrics import *
from Models.Summarize_V2.model import *

device = "cuda"
PROJECT_NAME = "Arxiv-Papers-Abstract-to-Title"
stemmer = PorterStemmer()
