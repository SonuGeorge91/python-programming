# Singleton Pattern
from module_level import (
    first_module, second_module
)

def module_level_singleton():
    first_module.main()
    second_module.main()

if __name__ == '__main__':

    choice = int(input ("Enter 1 for Module-Level Singleton:"))
    if choice == 1:
        module_level_singleton()
    else:
        print("Wrong choice...")