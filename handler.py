# write your code here

import argparse
import os


class FileHandler:
    def __init__(self):
        self.file_list = []
        self.size_dict = {}

    @staticmethod
    def size_sort_valid(size):
        while size not in [1, 2]:
            print('Wrong option')
            size = input()
        print()

        return size

    def file_list_append(self, file_format, name):
        for root, dirs, files in os.walk(name):
            if file_format == '':
                self.file_list.extend(
                    [
                        (os.path.join(root, v), os.path.getsize(os.path.join(root, v)))
                        for v in files
                    ]
                )
            else:
                self.file_list.extend(
                    [
                        (os.path.join(root, v), os.path.getsize(os.path.join(root, v)))
                        for v in files
                        if v.endswith(f'.{file_format}')
                    ]
                )

    def size_dict_add(self):
        for a, b in self.file_list:
            self.size_dict.setdefault(b, []).append(a)

    def find_root_chdir(self, name):
        if name != 'Directory is not specified':

            print('Enter file format:')
            file_format = input()

            print('Size sorting options:')
            print('1. Descending')
            print('2. Ascending')

            print('Enter a sorting option:')
            size_sort = int(input())
            size_sort_result = self.size_sort_valid(size_sort)

            self.file_list_append(file_format, name)
            self.size_dict_add()

            if size_sort_result == 1:
                size_keys = sorted(self.size_dict, reverse=True)
            else:
                size_keys = sorted(self.size_dict)

            for s in size_keys:
                print(f'{s} bytes')
                for v in self.size_dict[s]:
                    print(v)
                print()
        else:
            print(name)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('root_folder', nargs='?', default='Directory is not specified')
    args_name = parse.parse_args()

    file_handler = FileHandler()
    file_handler.find_root_chdir(args_name.root_folder)


if __name__ == '__main__':
    main()
