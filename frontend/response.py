import requests

class TalkerWithServer:
    def __init__(self):
        self.__auth_token = None
        self.__IP = "http://localhost:9999"

        print(f"{self.__IP}/token")

    def authorization(self, login: str, password: str) -> bool:
        Data = {"login": login, "password": password}
        respons = requests.post(f"{self.__IP}/token", headers=None, json=Data)
        

        if respons.status_code == 200:
            self.__auth_token = respons.json()["access_token"]

            return True
        
        return False

    def register(self, login: str, password: str) -> bool:
        Data = {"login": login, "password": password}
        respons = requests.post(f"{self.__IP}/create_user", headers=None, json=Data)


        if respons.status_code == 200:
            self.__auth_token = respons.json()["access_token"]

            return True
        
        return False
    
    def getPage(self, path: str, limit: int, offset: int):
        Data = {"path": path, "limit": limit, "offset": offset}
        Head = {"Authorization": "Bearer " + self.__auth_token}
        respons = requests.post(f"{self.__IP}/read_path", headers=Head, json=Data)

        print(respons.status_code)
        print(respons.text)
        if respons.status_code == 200:
            return respons.json()["data"]
        else:
            return None
    

    def sendFile(self, path: str, data: bytes):
        Params = {"path": path}
        Data = {"data": data}
        Head = {"Authorization": "Bearer " + self.__auth_token}
        respons = requests.post(f"{self.__IP}/upload_file", headers=Head, json=Data, params=Params)

        return respons.status_code == 200


    def getFile(self, path: str):
        Params = {"path": path}
        Head = {"Authorization": "Bearer " + self.__auth_token}
        respons = requests.get(f"{self.__IP}/upload_file", headers=Head, params=Params)

        if respons.status_code == 200:
            return respons.json()["data"]
        else:
            return None




# test = TalkerWithServer()

# test.authorization("usr", "123")
# test.register("usr", "123")

# print(test.getPage("/foto", 2, 1))