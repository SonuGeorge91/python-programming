''' The module access the shared variable and modify it'''

from . import module_level_singleton

def main():
    print(f'''From first module:: {
        module_level_singleton.shared_variable}''')

    # modify the shared variable
    module_level_singleton.shared_variable += "(modified by first_module)"

