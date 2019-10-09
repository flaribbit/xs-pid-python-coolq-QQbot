from websocket_server import WebsocketServer
import json as JSON
import requests
import re

URL_API="http://xs-pid.com/Activate.php?action=cmdActivateOnline&action2=online"

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

# 这个函数用来把数字用横线隔开
def buildID(id,m,n):
    s=""
    for i in range(n):
        if i>0:
            s+="-"
        s+=id[m*i:m*(i+1)]
    return s

# 这个函数用来从网页获取ActivateCID
def getRetActivateCID(installID):
    html=requests.post(URL_API,data={
        "ActivateOnlineServer": 1,
        "txtImage": 1,
        "inpImage": "",
        "ActivateIID": buildID(installID,7,9)
    }).text
    return re.search('x.value="(\\d*)"',html)[1]

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
        if re.match("\\d{63}", data["message"]):
            sendPrivateMessage(server, client, data["sender"]["user_id"], "正在获取...请等待大约10秒钟...")
            msg="获取成功\n"+buildID(getRetActivateCID(data["message"]),7,7)
            sendPrivateMessage(server, client, data["sender"]["user_id"], msg)
        elif data["message"]=="get":
            # sendPrivateMessage(server, client, data["sender"]["user_id"], 要发送的内容)
            sendPrivateMessage(server, client, data["sender"]["user_id"], "meow~")

server = WebsocketServer(1149, host='127.0.0.1')
# server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
