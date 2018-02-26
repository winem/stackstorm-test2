from st2actions.runners.pythonrunner import Action

import local_module
from local_module import CONSTANT_FOO

__all__ = [
    'PrintVersionAction'
]


class PrintVersionAction(Action):
    def run(self):
        version = 'v0.22.0'
        print(local_module)
        print(CONSTANT_FOO)
        print(version)
        return version
