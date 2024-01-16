import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):
    loaded_json = json.loads(string)
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path):
    with open(path, 'r') as _f:
        string = _f.read()
    print(formatter(string))

if __name__ == '__main__':
    # This gives us info from a help menu
    parser = argparse.ArgumentParser(description='A tool to format JSON files.')

    # This will let us use a flag to sort the keys as an optional argument
    parser.add_argument('-s', '--sort', action='store_true', help='Sort keys')

    args = parser.parse_args()

    # This will let us run the script from the command line
    main(sys.argv[-1]) # passing the last argument in the command line



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


    # we can also use:
    # python3 jformat.py --help
    