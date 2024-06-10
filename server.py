import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

players = {}

@sio.event
async def connect(sid, environ):
    print('Client connected:', sid)
    players[sid] = {'x': 200, 'y': 200, 'health': 100, 'character': None}

@sio.event
async def disconnect(sid):
    print('Client disconnected:', sid)
    if sid in players:
        del players[sid]
        await sio.emit('player_disconnected', sid)

@sio.event
async def select_character(sid, data):
    if sid in players:
        players[sid]['character'] = data['character']
        await sio.emit('character_selected', {'sid': sid, 'character': data['character']})

@sio.event
async def update_position(sid, data):
    if sid in players:
        players[sid]['x'] = data['x']
        players[sid]['y'] = data['y']
        await sio.emit('position_update', {'sid': sid, 'x': data['x'], 'y': data['y']})

@sio.event
async def attack(sid, data):
    if sid in players:
        await sio.emit('attack', {'sid': sid, 'x': data['x'], 'y': data['y'], 'character': data['character']})

if __name__ == '__main__':
    web.run_app(app, port=5001)  
