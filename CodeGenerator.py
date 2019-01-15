from CreateProject import AndroidProjectCreator
from ProjectParser import PageBean, AppParser
from tool.TemplateUtil import cp_file, template_file
from tool.Constant import *
import os


class BaseGenerator:
    def __init__(self):
        pass

    def generate(self):
        pass


class PageGenerator(BaseGenerator):

    @staticmethod
    def get_path(root, sub1="", sub2="", sub3=""):
        return os.path.join(root, sub1, sub2, sub3)

    def __init__(self, pageBeans, projectBean):
        BaseGenerator.__init__(self)

        self.project_name = projectBean.project
        self.package_name = projectBean.package
        self.projectDir = projectBean.projectDir
        self.package_name_path = self.package_name.replace(".", "/")
        self.current_dir = AndroidProjectCreator.get_current_dir()
        self.source_dir = self.get_path(self.current_dir, RES_MVP)
        self.dst_dir = self.get_path(self.current_dir, self.projectDir)

        self.pages = pageBeans
        # page path
        self.src_root_path = self.get_path(self.dst_dir, JAVA_SRC_PATH, self.package_name_path)

    def make_param(self):
        pass

    def __make_file(self):
        pass

    def generate_fragment(self, pageBean):
        pageSubPath = pageBean.subPackage

        src_file = self.get_path(self.source_dir, FRAGMENT)
        dst_file = self.get_path(self.src_root_path)
        


        cp_file(sourceFilePath, dstFullFile)

        template_file(dstFullFile, {
            "page_name": '',
        })

    def generate_vp(self):
        pass

    def gnerate_view(self):
        pass

    def generate(self):
        pass


if __name__ == '__main__':
    config = AppParser("./app.config")
    config.parse_config()

    projectBean = config.get_project_bean()
    pages = config.get_pages()

    coder = PageGenerator(pages, projectBean)
    coder.generate()
