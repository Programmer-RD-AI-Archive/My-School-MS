import json
import random

import nltk
import numpy as np
import torch
import torch.nn as nn
from nltk.stem.porter import PorterStemmer
from torch.utils.data import DataLoader, Dataset

from Models.Chat_Bot.help_funcs import *
from Models.Chat_Bot.model import *

nltk.download("punkt")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
