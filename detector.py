from trainer import Trainer
from nets import GPT2
import torch
import random


class Detector:
    def __init__(self, net_path, dictionary_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.dictionary_path = dictionary_path
        self.net = GPT2().to(self.device)
        self.vocab = torch.tensor([[random.randint(0, 2123)]]).to(self.device)
        self.position = torch.tensor([[random.randint(0, 200)]]).to(self.device)
        self.net.load_state_dict(torch.load(net_path))
        self.net.eval()

    def detect(self):
        for i in range(200):
            output = self.net(self.vocab, self.position)
            output = output[:, -1:]
            # 得到8个最大的值跟索引
            value, index = torch.topk(output, 8, dim=-1)
            # torch.multinomial()只能用于1维或2维的tensor
            value, index = value[0], index[0]
            value_index = torch.multinomial(torch.softmax(value, dim=-1), 1)
            output = index[0][value_index]
            # 效果与上一行代码相同
            # output = torch.gather(index, -1, v_index)
            self.vocab = torch.cat([self.vocab, output], dim=-1).to(self.device)
            self.position = torch.tensor([range(i + 2)]).to(self.device)
        with open(self.dictionary_path, "r+", encoding="utf-8") as dictionary:
            strs = dictionary.read().split()
            for index in self.vocab[0]:
                if strs[index] == "[SEQ]":
                    print()
                elif strs[index] == "[PAD]":
                    print(" ", end="")
                elif strs[index] == "[START]":
                    print()
                elif strs[index] == "[END]":
                    print("end...")
                    break
                else:
                    print(strs[index], end="")


if __name__ == '__main__':
    detector = Detector("models/net_lyric.pth", "data/dictionary/dictionary.txt")
    detector.detect()
