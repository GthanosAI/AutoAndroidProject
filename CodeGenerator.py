from ProjectParser import PageBean, AppConfig


class BaseGenerator:
    def __init__(self):
        pass

    def generate(self):
        pass


class PageGenerator(BaseGenerator):
    def __init__(self, pageBean, appBean):
        BaseGenerator.__init__(self)
        self.pageBean = pageBean
        self.appBean = appBean

    def make_param(self):
        pass

    def generate(self):
        """"
        FragmentWithAdapter:
                        page_name["xxx"],
                        sub_path,
                        layout_prama[""],
                        layout_type[Grid, Linear] ,
                        adapter_name,
                        model_name,
                        page_name_lowcase

        Adapter: package_name
                 sub_path
                 adapter_name
                 model_path
                 model_name
                 page_name
                 adapter_name_lowcase
        return:
        """
        pass


if __name__ == '__main__':
    config = AppConfig("./app.config")
    config.parse_config()

    print(config.get_app_bean())
    print(config.get_pages())
