import torch
from torch.utils.data import Dataset
from torchvision import transforms

class DatasetFromSubset(Dataset):
    def __init__(self, subset, transform=None):
        self.subset = subset
        self.transform = transform
    
    def __getitem__(self, index):
        x, y = self.subset[index]

        if self.transform:
            x = self.transform(x)
        return x, y
    
    def __len__(self):
        return len(self.subset)

def accuracy(labels, targets, label=False):
    if label:
        print("inputs are labels")
    else:
        print("inputs are weights")