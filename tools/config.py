# -*- encoding:utf-8 -*-

import os
import os.path

package_install_type = 'Release'

root = '..'

def get_path(*names):
	g = globals()

	path = os.path.join(g.get('root', ''), *names)
	return os.path.abspath(path)