import os
import argparse
import numpy as np

from PIL import Image
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--original', type=str, default='../data/original')
parser.add_argument('--final', type=str, default='../data/final')
args = parser.parse_args()


if not os.path.exists(args.final):
	os.makedirs(args.final)

for root, dirs, files in os.walk(args.original, topdown=False):
	for name in tqdm(files):
		try:
			both = Image.new('RGB', (512, 256))
			img1 = Image.open(os.path.join(args.original, name))
			img2 = img1.convert('L')
   
			both.paste(img2)
			both.paste(img1, (256, 0))
			both.save(os.path.join(args.final, name))
		except Exception as e:
			print('Error: {}'.format(e))
