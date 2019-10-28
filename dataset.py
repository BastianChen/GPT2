import os
from torch.utils.data import Dataset
import config as cfg
import torch


class Dataset(Dataset):
    def __init__(self, path):
        self.dataset = []
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), "r+") as file:
                words = [int(word) for word in file.read().split()]
                words_length = len(words)
                start = 0
                while words_length - start > cfg.pos_num + 1:
                    self.dataset.append(words[start:start + cfg.pos_num + 1])
                    start += cfg.stride
                else:
                    if words_length > cfg.pos_num + 1:
                        self.dataset.append(words[words_length - cfg.pos_num - 1:])

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, item):
        data = torch.tensor(self.dataset[item])
        return data[0:-1], data[1:]


if __name__ == '__main__':
    myDataset = Dataset("data/tokenized/lyric")
    print(len(myDataset))
    # print(myDataset[1][0])
    # print(myDataset[1][0].shape)