
from websocket import create_connection
ws = create_connection("wss://localhost/", timeout=5)
if ws.connected:
      ws.send('8')
      print(ws.recv())
      # ws.close()