import json
import requests

from dataset import get_all_data
from models import Monster


if __name__ == "__main__":
    data = get_all_data()

    monsters = data['monsters']
    m1 = Monster(**monsters[0])

raw_input("Are you done here?\n> ")
