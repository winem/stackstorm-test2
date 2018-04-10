import sys

from st2actions.runners.pythonrunner import Action

__all__ = [
    'PrintPythonVersionAction'
]


class PrintPythonVersionAction(Action):
    def run(self):
        print('%s on %s' % (sys.version, sys.platform))
