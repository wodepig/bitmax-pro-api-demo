import os
import click
import requests
from pprint import pprint

# Local imports 
from util import *



@click.command()
@click.option("--symbol", type=str, default="BTMX/USDT")
@click.option("--n", type=int, default=10, help="number of records to request")
@click.option("--config", type=str, default=None)
def run(symbol, n, config):
    if config is None:
        config = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config.json")
        print(f"Config file is not specified, use {config}")
    btmx_cfg = load_config(config)['bitmax']

    host = btmx_cfg['https']

    url = f"{host}/api/pro/trades"
    params = dict(symbol=symbol, n=n)

    res = requests.get(url, params=params)
    pprint(parse_response(res))


if __name__ == "__main__":
    run()