#!/usr/bin/env python

import math
import time
from color import UIColor
import unicornhat as unicorn

def main():
    try:
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(0)
        unicorn.brightness(0.3)
        width,height=unicorn.get_shape()

        predictions = [UIColor.convert(0), UIColor.convert(3), UIColor.convert(4), UIColor.convert(2),
        UIColor.convert(2), UIColor.convert(5), UIColor.convert(8), UIColor.convert(12)]

        for x in range(width):
            rgb = predictions[x]
            for y in range(height):
                unicorn.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
                unicorn.show()
                time.sleep(0.05)

    except:
        print('traceback.format_exc():\n%s',traceback.format_exc())
        exit()

if __name__ == '__main__':
    while True:
        main()
        time.sleep(60*10)
