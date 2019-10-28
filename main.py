from trainer import Trainer

if __name__ == '__main__':
    trainer = Trainer("models/net_lyric.pth", "data/tokenized/lyric")
    trainer.train()
