import configparser

config=configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def getUserEmail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getUserPassword():
        password=config.get('common info','password')
        return password