
import_file = "../input/log.csv"


def file_reader(import_file):
    with open(import_file, 'r') as f:
        yield f.readline()


if __name__ == '__main__':
    for line in file_reader(import_file):
        print(line)
