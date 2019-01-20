#!/usr/bin/env python

import time
from letters import Letter
import unicornhat as unicorn

def main():
    try:
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(0)
        unicorn.brightness(0.3)
        width,height=unicorn.get_shape()
        letters = Letter.V + Letter.I + Letter.T

        yellow = [247, 178, 28]
        white = [255, 255, 255]
        colors = [yellow, yellow, yellow, white, yellow, yellow, yellow]

        for x in range(width):
            rgb = colors[x]
            for y in range(height):
                if len(letters) > y :
                    row = letters[y]
                    if len(row) > x :
                        if row[x] == 1 :
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
