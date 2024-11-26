import json
import sys

if __name__ == '__main__':
    x = sys.argv
    print(x)

    # python3 main.py create --input '{ "name": " chinaskill001", " imagename": "imageid"}'
    if x[1] == 'create':
        if x[2] == '--input' or x[2] == '-i':
            # print(f"Json: {x[3]}")
            j = json.loads(x[3])
            print(j['name'])

    if x[1] == 'get':
        pass

    if x[1] == 'apply':
        if x[2] == '--input' or x[2] == '-i':
            pass