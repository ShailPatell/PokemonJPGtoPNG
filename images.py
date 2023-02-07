import sys
import os
from PIL import Image, ImageFilter

img = Image.open('PokemonJPGtoPNG\Pokedex\squirtle.jpg')
img.thumbnail((400,400))
img.save('thumbnail.jpg')

