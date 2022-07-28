import requests,uuid,random,string

# src without colorama, so you can try it on the phone without any problem <3

print("[ > ]" " Instagram Password Reset\n[ < ] Instagram : @rv.y\n[ > ] Follow Me <3 ")

print("\n[ < ] Enter Your Target : ", end="")
target = input()
if target[0] == "@":
    print("[ > ] Without ( @ ) Please .. ", end="")
    input()
    exit()

usr = "username"

url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"            
data = {
    "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
    usr: target,
    "guid": uuid.uuid4(),
    "device_id": uuid.uuid4()
    }
headers = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}

req = requests.post(url,headers=headers,data=data)
        
if "obfuscated_email" in req.text:
    print(f"[ > ] {req.text} ",end="")
    input()
    exit()
elif req.status_code == 404:
    print("[ > ] No Users Found .. ",end="")
    input()
    exit()
else:
    print(f"[ > ] {req.text} ",end="")
    input()
    exit()
