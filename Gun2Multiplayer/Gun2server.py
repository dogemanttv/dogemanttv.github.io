import asyncio
import websockets

async def message(websocket, path):
    user_id = None
    if len(CLIENTS) < 2:
        CLIENTS.add(websocket)
        user_id = len(CLIENTS)
        CONNECTIONS[user_id] = websocket
        await websocket.send(f"You are player {user_id}")
        print(f"{websocket.remote_address[0]} joined.")
        print(f"{len(CLIENTS)} connected players.")
    else:
        print(f"{websocket.remote_address[0]} tried to join but server is full.")
        await websocket.send("Server is full!")
        await websocket.close()

    while True:
        if user_id == 1:
            other_user_id = 2
        else:
            other_user_id = 1
        try:
            message = await CONNECTIONS[user_id].recv()
        except websockets.ConnectionClosed:
            print(f"Connection closed for player {user_id}")
            CLIENTS.remove(user_id)
            break

        if message == "Respawn":
            await CONNECTIONS[other_user_id].send("Respawn")
            print(f"Player {user_id} respawned.")
        elif message == "Shoot":
            await CONNECTIONS[other_user_id].send("Shoot")
            print(f"Player {user_id} shot.")
        elif message == "Up":
            await CONNECTIONS[other_user_id].send("Up")
            print(f"Player {user_id} moved up.")
        elif message == "Left":
            await CONNECTIONS[other_user_id].send("Left")
            print(f"Player {user_id} moved left.")
        elif message == "Down":
            await CONNECTIONS[other_user_id].send("Down")
            print(f"Player {user_id} moved down.")
        elif message == "Right":
            await CONNECTIONS[other_user_id].send("Right")
            print(f"Player {user_id} moved right.")
        else:
            print(f"Unknown message received from player {user_id}: {message}")

async def main():
    async with websockets.serve(message, "0.0.0.0", port):
        await asyncio.Future()  # run forever

CLIENTS = set()
CONNECTIONS = {}
port = 8080
print(f"Gun2 Server Started @ {port}")
asyncio.run(main())
