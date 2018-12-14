# -*- encodding:utf-8 -*-

import config
import os.path

def cmake_options(name = 'common', **kwds):
	option_map = get_option_map(name, **kwds)

	options = []
	for key, value in option_map.items():
		option = '-D %s=%s'%(key, value)
		options.append(option)
	
	return ' '.join(options)

def get_option_map(name = 'common', **kwds):
	names = name,
	if name != 'common':
		names = 'common', name
	
	options = {}
	for file_name in names:
		file_options = get_file_option_map(file_name)
		options.update(file_options)
	
	options.update(kwds)

	return options

def get_file_option_map(name):
	path = config.get_path('etc', 'cmake', '%s.txt'%(name))

	options = {}
	if not os.path.isfile(path):
		return options

	for line in open(path):
		line = line.strip()
		if not line:
			continue
		
		tokens = line.split('=')
		options[tokens[0].strip()] = tokens[1].strip()
	
	return options
