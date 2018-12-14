# -*- encoding:utf-8 -*-

import os
import utils
import config
import argparse

def parse_args():
	parser = argparse.ArgumentParser(description = 'manager the libs')

	#parser.add_argument('op', type = str, choices = ['install', 'list'])
	parser.add_argument('libs', type = str, nargs = '*')

	return parser.parse_args()

class lib_mgr(object):
	def __init__(self, name):
		self.name = name

		self.project_path = config.get_path('build', 'libs', self.name)
	
	def gen_project(self):
		source = config.get_path('libs_src', self.name)
		project = self.project_path
		install = config.get_path('libs')

		options = utils.cmake_options(
			CMAKE_INSTALL_PREFIX = install,
			CMAKE_EXPORT_NO_PACKAGE_REGISTRY = 'ON'
		)

		# cmake source target
		command = 'cmake %s -B %s %s'%(options, project, source)
		self.system(command)
	
	def system(self, command):
		print('[command]', command)
		os.system(command)
	
	def install(self):
		target = 'INSTALL'
		config_type = config.package_install_type

		command = 'cmake --build %s --target %s --config %s'%(self.project_path, target, config_type)
		self.system(command)
	
class exporter(object):
	def __init__(self, args):
		self.args = args

	def gen_export_libs(self):
		# get depends
		return self.args.libs
	
	def export(self):
		libs = self.gen_export_libs()

		for lib in libs:
			self.do_export(lib)
	
	def do_export(self, lib):
		mgr = lib_mgr(lib)

		mgr.gen_project()
		mgr.install()

if __name__ == '__main__':
	args = parse_args()

	export = exporter(args)

	export.export()