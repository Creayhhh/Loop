import requests
from utils import sha256_encryption

url = "http://127.0.0.1:5000"


def register(user_data):
    post_data = user_data
    post_data["password"] = sha256_encryption(post_data["password"])
    try:
        res = requests.post(url=url + '/registration', json=post_data)
        if res.status_code == 200:
            res = res.json()
            if res["state"] == 1:
                return True, "注册成功"
            elif res["state"] == 0:
                return False, "用户已存在"
            else:
                return False, res["message"]
        else:
            return False, "内部错误"

    except:
        return False, "无法连接服务器"


def login(username, password):
    post_data = {
        "username": username,
        "password": sha256_encryption(password)
    }
    try:
        res = requests.post(url=url + '/login', json=post_data).json()
        if res["state"] == 1:
            return True, res["token"]
        elif res["state"] == 0:
            return False, "用户不存在"
        elif res["state"] == -2:
            return False, "密码错误"
        else:
            return False, res["message"]
    except:
        return False, "无法连接服务器"


def get_userinfo(token):
    headers = {"Authorization": "Bearer " + token["access_token"]}
    try:
        res = requests.post(url=url + '/query/userinfo', headers=headers)
        if res.status_code == 200:
            return res.json()["user_info"]
        else:
            return None
    except:
        return None


def submit_sport_record(token, data):
    headers = {"Authorization": "Bearer " + token["access_token"]}
    try:
        res = requests.post(url=url + '/submit/record', json=data, headers=headers)
        if res.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def query_sport_history(token, data):
    headers = {"Authorization": "Bearer " + token["access_token"]}
    try:
        res = requests.post(url=url + '/query/history', json=data, headers=headers)
        if res.status_code == 200:
            if "sport_history" in res.json():
                return True, res.json()["sport_history"]
            else:
                return True, []
        else:
            return False, None
    except Exception as e:
        return False, None


def refresh_token(token):
    headers = {"Authorization": "Bearer " + token["refresh_token"]}
    try:
        res = requests.post(url=url + '/token/refresh', headers=headers)
        if res.status_code == 200:
            return res.json()["access_token"]
        else:
            return None
    except:
        return None
