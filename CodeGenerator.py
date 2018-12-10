from ConfigParser import PageBean, AppConfig


class BaseGenerator:
    def __init__(self):
        pass

    def generate(self):
        pass


class PageGenerator(BaseGenerator):
    def __init__(self, pageBean):
        BaseGenerator.__init__(self)
        self.pageBean = pageBean

    def generate(self):
        pass





if __name__ == '__main__':
    config = AppConfig("./app.config")
    config.parse_config()

    print(config.get_app_bean())
    print(config.get_pages())
