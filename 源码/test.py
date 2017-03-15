import pprint
import sys

def test(num):
    if num == 1:
        print("Hello!")
        print(sys.argv[0])

    else :
        sys.exit()


if __name__=='__main__':
    test(int(sys.argv[1]))
