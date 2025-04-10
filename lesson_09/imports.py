# from importlib.machinery import SourceFileLoader
#
# module_name = 'math'
# math_module = SourceFileLoader(module_name, '/folder/math.py').load_module()
#
# result = math_module.add(2, 3)
# from idlelib.colorizer import prog_group_name_to_tag

# --------------------
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

import esng

print(string_one)