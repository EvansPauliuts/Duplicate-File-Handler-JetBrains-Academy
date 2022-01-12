# write your code here

import argparse
import os


class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def find_root_chdir(name):
        if name != 'Directory is not specified':
            os.chdir(name)

            for root, dirs, files in os.walk('.', topdown=True):
                for name in files:
                    print(os.path.join(root, name))
        else:
            print(name)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('root_folder', nargs='?', default='Directory is not specified')
    args_name = parse.parse_args()

    FileHandler.find_root_chdir(args_name.root_folder)


if __name__ == '__main__':
    main()
