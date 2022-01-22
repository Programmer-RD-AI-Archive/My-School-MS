import random

import nltk
import numpy as np
import pandas as pd
import torch
import torchvision
import wandb
from nltk.stem.porter import *
from sklearn.model_selection import *
from torch.nn import *
from torch.optim import *
from torch.utils.data import DataLoader, Dataset
from tqdm import *

from Models.Will_Answer_Solve_Issue.help_funcs import *
from Models.Will_Answer_Solve_Issue.load_data import *
from Models.Will_Answer_Solve_Issue.metrics import *
from Models.Will_Answer_Solve_Issue.model import *

stemmer = PorterStemmer()
PROJECT_NAME = "kickstarter-NLP-V7"
device = "cuda"
