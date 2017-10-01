import sys
import hashlib
import random
from PIL import Image


RESOLUTION = 128, 128
V_RESOLUTION = 16, 16
MODE = "RGB"


# entrance function, takes args from console
def main():
    name = sys.argv[1]
    generate(name)


# generate image based on string
def generate(string):
    hash_string = generate_hash(string)
    print(hash_string)

    color = random_color()
    print(color)

    image = Image.new(MODE, RESOLUTION, color)
    image.show()


# hash a string using hashlib MD5 algorithm
def generate_hash(string):
    try:
        hash_object = hashlib.md5(str.encode(string))
        print(hash_object.hexdigest())

        return hash_object.hexdigest()

    except IndexError:
        print("Error: Please enter a string as an argument.")


# create a random foreground color
def random_color():
    color = (random.randint(50, 255), random.randint(50, 255),
             random.randint(50, 255), 255)

    return color


if __name__ == '__main__':
    main()
