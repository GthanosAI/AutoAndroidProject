import ConfigParser

CONFIG = 'config'
PGAE = 'page'


class Dict2Obj(object):
    """
    Turns a dictionary into a class
    """

    def reload(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def make_parser(self, parser, section):
        key_values = self.__dict__
        for key in key_values.keys():
            value = parser(section, key, key_values[key])
            key_values[key] = value

    def log(self):
        print(self.__dict__)


class AppBean(Dict2Obj):
    def __init__(self):
        self.package = ""
        self.project = ""
        self.projectDir = ""

    def make(self, parser):
        self.make_parser(parser, CONFIG)


class PageBean(Dict2Obj):
    def __init__(self):
        self.subPackage = ""
        self.type = ""
        self.view = ""
        self.modelPath = ""
        self.itemModel = ""
        self.itemView = ""
        self.pageNum = 0

    def make(self, parser, pageName):
        self.pageNum = pageName
        self.make_parser(parser, pageName)


class AppConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.__configParser = ConfigParser.ConfigParser()
        self.__configParser.read(config_file)

        self.appBean = None
        self.pages = []

    def get_value(self, section, key, default=""):
        if self.__configParser.has_option(section, key):
            return self.__configParser.get(section, key)
        else:
            return default

    def parser(self):
        pass

    def parse_config(self):
        self.appBean = AppBean()
        self.appBean.make(self.get_value)

        sections = self.__configParser.sections()
        for i in range(0, 100):
            name = PGAE + str(i)
            if name in sections:
                ret = PageBean()
                ret.make(self.get_value, name)
                self.pages.append(ret)

    def get_app_bean(self):
        return self.appBean

    def get_pages(self):
        return self.pages


if __name__ == '__main__':
    config = AppConfig("./app.config")
    config.parse_config()

    print(config.get_app_bean())
