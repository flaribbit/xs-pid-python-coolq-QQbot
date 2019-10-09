import requests
URL_API="http://xs-pid.com/Activate.php?action=cmdActivateOnline&action2=online"
res=requests.post(URL_API,data={
    "ActivateOnlineServer": 1,
    "txtImage": 1,
    "inpImage": "",
    "ActivateIID": "5454900-9543025-1937290-2769366-0500436-8887324-5772570-5357156-9708721"
})
print(res.text)