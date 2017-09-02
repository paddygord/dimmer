import asyncio
import websockets
import parse

import struct
import mmap
f = open('ui_file', 'a+b')
m = mmap.mmap(f.fileno(), 0)

async def consumer_handler(websocket, path):
    while True:
        message = await websocket.recv()
        u = parse.parse("{:g} {:g} {:g} {:g}", message)
        if u is not None:
            b0, b1, x, y = u
            print(b0, b1, x, y)
            m.seek(0)
            m.write(bytes(struct.pack('ffff', b0, b1, x, y)))

start_server = websockets.serve(consumer_handler, 'raspberrypi.local', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
