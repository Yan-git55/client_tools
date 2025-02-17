import requests
import json
import client_tools
import os

class chatgml():
    """
    本demo为chatgml6b的client
    github 地址为：
    https://github.com/THUDM/ChatGLM-6B

    """
    url = 'http://127.0.0.1:8000'
    headers = {"Content-Type": "application/json"}

    def __init__(self):
        self.history = []
        self.load_chatgml6b_url()

        pass

    def load_chatgml6b_url(self):

        if os.name =="posix":
            ls = str(client_tools.__file__).split("/")
            path = "/" + ls[1]
            for i in ls[2:-1]:
                path = path + "/" + i
            path = path + "/" + "config.json"

        elif os.name == "nt":
            ls = str(client_tools.__file__).split("\\")
            path = ls[0]
            for i in ls[1:-1]:
                path = path + "\\" + i
            path = path + "\\" + "config.json"


        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            chatgml.url = config["chat"]['chatgml6b']
    def make_send_json(self,ques):
        """
        return : 默认支持长对话
        """
        return {"prompt":ques,"history":self.history}
    def get_assitant(self,data):
        if data["status"] !=200:
            return "状态码不对"

        self.history = data["history"]
        return str(data["response"])

    def post(self,user_ed):
        json_payload = json.dumps(user_ed)
        response = requests.post(chatgml.url,data=json_payload,headers=chatgml.headers)
        return self.get_assitant(response.json())


if __name__ == '__main__':
    ai = chatgml()
    while 1:
        ques = input("请输入你的问题:\t")

        user_ed = ai.make_send_json(ques)

        assitant = ai.post(user_ed)
        print(assitant)