from ProjectParser import PageBean, AppConfig
from tool.TemplateUtil import cp_file, template_file


class BaseGenerator:
    def __init__(self):
        pass

    def generate(self):
        pass


class PageGenerator(BaseGenerator):
    def __init__(self, pageBean, appBean):
        self.relative_path = "/res/mvp/"
        BaseGenerator.__init__(self)
        self.pageBean = pageBean
        self.appBean = appBean
        self.source_files = {
            'fragment': 'Fragment.java',
            'fragmentWithAdapter': 'FragmentWithAdapter.java',
            'view': "IView.java",
            'presenter': 'Presenter.java',
            'presenterWithAdapter': 'PresenterWithAdapter.java',
            'model': 'ModelBean.java'
        }

    def __get_path(self, path):
        return self.relative_path + path

    def make_param(self):
        pass

    def generate_fragment(self):
        if self.pageBean.is_adapter():
            sourceFile = self.source_files['fragmentWithAdapter']
        else:
            sourceFile = self.source_files['fragment']

        dstFileName = self.pageBean.get_fragment_name()
        dstDir = self.appBean.get_java_source_path()
        sourceFilePath = self.__get_path(sourceFile)
        dstFullFile = dstDir + dstFileName
        cp_file(sourceFilePath, dstFullFile)
        template_file(dstFullFile, {
            "page_name": '',
        })

    def generate_vp(self):
        pass

    def gnerate_view(self):
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

    tm1 = config.get_app_bean()
    tm2 = config.get_pages()

    tm1.log()
    for item in tm2:
        item.log()
