from Utils import Utils

class InvalidOperationException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        