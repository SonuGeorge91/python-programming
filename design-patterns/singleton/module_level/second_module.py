''' Module prints the value of shared variable.
    The purpose is to print the modified value from first_module.py and 
    ensure the value change is reflected'''
from . import module_level_singleton

def main():
    print(f'''From second module:: {
        module_level_singleton.shared_variable}''')

