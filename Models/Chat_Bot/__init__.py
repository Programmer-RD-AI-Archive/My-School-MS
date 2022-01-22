import numpy as np
import nltk

nltk.download("punkt")
from nltk.stem.porter import PorterStemmer

import torch
import torch.nn as nn
import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
from Models.Chat_Bot.help_funcs import *
from Models.Chat_Bot.model import *
