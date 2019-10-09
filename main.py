import logging
from websocket_server import WebsocketServer

# def new_client(client, server):
# 	server.send_message_to_all("Hey all, a new client has joined us")

def message_received(client, server, message):
    server.send_message(client, "Recieved: "+message)

server = WebsocketServer(1234, host='127.0.0.1')
# server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
