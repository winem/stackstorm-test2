from st2actions.runners.pythonrunner import Action

__all__ = [
    'PrintVersionAction'
]


class PrintVersionAction(Action):
    def run(self):
        version = 'v0.25.0'
        print(version)
        return version
