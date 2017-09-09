import asyncio
import websockets
import parse

import struct
import mmap
f = open('ui_file', 'a+b')
m = mmap.mmap(f.fileno(), 20)

async def consumer_handler(websocket, path):
    while True:
        message = await websocket.recv()
        m.seek(0)
        m.write(message)

start_server = websockets.serve(consumer_handler, 'raspberrypi.local', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
