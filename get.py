import requests
import os
import argparse

parser = argparse.ArgumentParser(
	prog = 'GET Files',
	description = 'Downloads Files'
	)

parser.add_argument('-l', '--link', help = 'Link to be Downloads.')
parser.add_argument('-d', '--download', help = 'Location where the file is downloaded.', default = os.path.join(os.environ["USERPROFILE"],'Downloads'))
parser.add_argument('-f', '--filename', help = 'Name of the file.')

args = parser.parse_args()

print(':: Download Started ::')

if args.filename == None:
	args.filename = args.link.split('/')[-1]

with open(os.path.join(args.download,args.filename),'wb') as f:
	f.write(requests.get(args.link).content)

print(':: Download Complete ::')