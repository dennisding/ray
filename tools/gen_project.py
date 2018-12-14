# -*- encoding:utf-8 -*-

import os
import utils
import config
import argparse

def parse_args():
	# python3 gen_project.py
	parser = argparse.ArgumentParser(description = 'gen_projects')

	#parser.add_argument('op', type = str, choices = ['install', 'list'])
	parser.add_argument('projects', type = str, nargs = '*')

	return parser.parse_args()

class generator(object):
	def __init__(self, args):
		self.args = args
	
	def generate(self):
		print('genreate', self.args)
	
		source = config.get_path('src')
		target = config.get_path('build', 'projects')
		module_path = config.get_path('libs')

		options = utils.cmake_options(
			CMAKE_PREFIX_PATH = module_path,
#			CMAKE_INCLUDE_CURRENT_DIR = 'ON'
		)

		command = 'cmake %s -B %s %s'%(options, target, source)

		self.system(command)
	
	def system(self, command):
		print('[command]', command)
		os.system(command)

if __name__ == '__main__':
	args = parse_args()

	gen = generator(args)

	gen.generate()