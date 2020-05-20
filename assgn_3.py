import os

class ConfigDict(dict):
    def __init__(self, text_file):
        self._text_file = text_file
        if os.path.isfile(self._text_file):
            with open(self._text_file) as file:
                for line in file:
                    line = line.rstrip()
                    key, val = line.split('=', 1)
                    dict.__setitem__(self, key, val)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._text_file, 'w') as file:
            for k, v in self.items():
                file.write('{0}={1}\n'.format(k,v))


