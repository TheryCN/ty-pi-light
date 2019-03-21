#!/usr/bin/env python

import time
import websocket
import json
import unicornhat as unicorn

def on_message(ws, message):
    try:
        print(message)
        data = json.loads(message)
        colors = data["colors"]
        width,height=unicorn.get_shape()

        for x in range(width):
            if len(colors) > x:
                for y in range(height):
                    if len(colors[x]) > y and len(colors[x][y])==3 :
                        rgb = colors[x][y]
                        unicorn.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
                    unicorn.show()
                    time.sleep(0.05)
    except:
        print('traceback.format_exc():\n%s',traceback.format_exc())

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")
    time.sleep(15)
    print("### trying to reconnect ###")
    connect()

def on_open(ws):
    ws.send("Hello i'm your client")

def connect():
    ws = websocket.WebSocket()
    ws = websocket.WebSocketApp("ws://localhost:4000",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == '__main__':
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(0.3)
    connect()
