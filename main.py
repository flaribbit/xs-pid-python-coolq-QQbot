from websocket_server import WebsocketServer
import json as JSON
import requests

# def new_client(client, server):
# 	server.send_message_to_all("Hey all, a new client has joined us")

# 发送私聊消息
def sendPrivateMessage(server, client, user_id, message):
    msg=JSON.dumps({
        "action": "send_private_msg",
        "params": {
            "user_id": user_id,
            "message": message
        }
    })
    server.send_message(client, msg)

# 发送群消息
def sendGroupMessage(server, client, user_id, message):
    msg=JSON.dumps({
        "action": "send_group_msg",
        "params": {
            "user_id": user_id,
            "message": message
        }
    })
    server.send_message(client, msg)

# 收到消息的回调函数
def message_received(client, server, message):
    # 解析消息的内容
    data=JSON.loads(message)
    # 忽略发送反馈
    if "retcode" in data:
        print("消息发送成功")
        return
    # 如果收到了私聊消息
    if data["message_type"]=="private":
        # 根据消息的内容自动回复
        if data["message"]=="get":
            # 回复消息的写法：
            # sendPrivateMessage(server, client, data["sender"]["user_id"], 要发送的内容)
            sendPrivateMessage(server, client, data["sender"]["user_id"], "正在获取")
            # 获取网页信息
            msg=requests.get("http://xs-pid.com/mskey.php?action=online").text
            sendPrivateMessage(server, client, data["sender"]["user_id"], msg)

server = WebsocketServer(1149, host='127.0.0.1')
# server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
