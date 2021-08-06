import argparse
import os

class ArgumentParser:
    
    def __init__(self):
        self.ap = argparse.ArgumentParser()

    def add_argument(self, short_name, long_name):
        self.ap.add_argument(f"-{short_name}", f"-{long_name}", required=True)

    def get_values(self):
        return vars(self.ap.parse_args())


class VideoArgument:
    
    def __init__(self):
        self.ap = ArgumentParser()
        self.ap.add_argument("p", "path_video")
        self.args = self.ap.get_values()
    
    def get_data(self, name):
        return self.args[name]