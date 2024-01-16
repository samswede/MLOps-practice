
# this is how we use the "click" module to do the same thing.
# It will be easier to use, more readable, and more robust.

import json
import click

def formatter(string, sort_keys=True, indent=4):
    loaded_json = json.loads(string)
    return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

@click.command()
@click.option('--sort', '-s', is_flag=True, help='Sort keys')
@click.argument('path', type=click.Path(exists=True))
def main(path, sort):
    with open(path, 'r') as _f:
        string = _f.read()
    print(formatter(string, sort_keys=sort))

if __name__ == '__main__':
    main()

    # run from terminal: 
    # python3 jformat.py <path_to_json_file> --<options>

    # e.g.
    '''
    (venv) bash-3.2$ python3 jformat_click.py examples/example.json
    {
        "arg": 1,
        "zeta": 7,
        "boto": true
    }
    (venv) bash-3.2$ python3 jformat_click.py examples/example.json --sort
    {
        "arg": 1,
        "boto": true,
        "zeta": 7
    }
    (venv) bash-3.2$ 
    
    '''