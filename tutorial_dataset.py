import json
import cv2
import numpy as np

from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self):
        self.data = []
        with open('training/Entreprenerdz/prompt.json', 'rt') as f:
            for line in f:
                print(line)
                self.data.append(json.loads(line))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        source_filename = item['source']
        target_filename = item['target']
        prompt = item['prompt']

        print('training/Entreprenerdz/' + source_filename)
        source = cv2.imread('training/Entreprenerdz/' + source_filename)
        target = cv2.imread('training/Entreprenerdz/' + target_filename)

        # Do not forget that OpenCV read images in BGR order.
        print(source.shape)
        source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

        # Normalize source images to [0, 1].
        source = source.astype(np.float32) / 255.0

        # Normalize target images to [-1, 1].
        target = (target.astype(np.float32) / 127.5) - 1.0

        return dict(jpg=target, txt=prompt, hint=source)

