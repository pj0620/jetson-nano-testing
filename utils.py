import itertools
import json
from typing import Any

FACES = ["front", "back"]
SIDES = ["left", "right"]

FORWARD = "forward"
BACK = "back"


def get_pinout():
  with open('gpio.json', 'r') as file:
    data = json.load(file)
  return data


def get_forward_pins() -> list[int]:
  pins = get_pinout()
  return [
    pins[face][side][FORWARD]
    for face, side in itertools.product(FACES, SIDES)
  ]


def get_back_pins() -> list[int]:
  pins = get_pinout()
  return [
    pins[face][side][BACK]
    for face, side in itertools.product(FACES, SIDES)
  ]
