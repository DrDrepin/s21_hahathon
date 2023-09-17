

class JSONData():
    def __init__(self):
        self.__data = [{}]

    def processAllData(self, f):
        for item in self.__data:
            f(item["path"], item["data"])


    def getElem(self, index) -> dict:
        return self.__data[index]
    
    def set_data(self, data):
        self.__data = data
