import os
import sys
import json

def formatter(string, sort_keys=True, indent=4):
    loaded_json = json.loads(string)
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path):
    with open(path, 'r') as _f:
        string = _f.read()
    print(formatter(string))

if __name__ == '__main__':
    main(sys.argv[1])
    # run from terminal: 
    # python3 jformat.py <path_to_json_file>

    # e.g.
    # python3 jformat.py examples/example.json

    # output:
    #    {
    #        "arg": 1,
    #        "boto": true,
    #        "zeta": 7
    #    }