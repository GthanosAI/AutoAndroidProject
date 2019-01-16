# coding=utf-8
import ConfigParser
from tool.Constant import *

CONFIG = 'project'
BUILd = 'build'
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

    @staticmethod
    def get_path_param(full_path):
        paths = full_path.split('.')
        if len(paths) > 1:
            fileName = paths[-1]
            subPath = full_path.rstrip(fileName).rstrip('.')
        else:
            fileName = paths[-1]
            subPath = ''

        return fileName.replace("Fragment", ''), subPath

    def get_param(self):
        return None

    def log(self):
        print(self.__dict__)


class ProjectBean(Dict2Obj):
    """
    工程
    """

    def __init__(self):
        self.package = ""
        self.project = ""
        self.projectDir = ""

    def make(self, parser):
        self.make_parser(parser, CONFIG)

    def get_param(self):
        return {
            KEY_PACKAGE_NAME: self.package,
            KEY_PROJECT_NAME: self.project,
            KEY_PROJECT_DIR: self.projectDir
        }


class BuilderBean(Dict2Obj):
    """
    编译
    """

    def __init__(self):
        self.gradle = ""
        self.plugin = ""

    def make(self, parser):
        self.make_parser(parser, BUILd)

    def get_param(self):
        return {
            KEY_GRADLE: self.gradle,
            KEY_GRADLE_PLUGIN: self.plugin
        }


class PageBean(Dict2Obj):
    """
    页面
    """

    def __init__(self):
        self.pageNum = ''
        self.subPackage = ''
        self.type = ''
        self.viewParam = ''
        self.itemModel = ''
        self.itemView = ''
        self.adapterName = ''
        self.pageName = ''
        self.subPath = ''
        self.viewLayout = ""

        self.pageFragmentParam = {
            KEY_PACKAGE_NAME: "",
            KEY_PAGE_NAME: "",
            KEY_PAGE_SUB_PATH: "",
            KEY_PAGE_VIEW_NAME: ""
        }

        self.presenterParam = {
            KEY_PACKAGE_NAME: "",
            KEY_PAGE_NAME: "",
            KEY_PAGE_SUB_PATH: "",
        }

        self.viewParam = {
            KEY_PACKAGE_NAME: "",
            KEY_PAGE_NAME: "",
            KEY_PAGE_SUB_PATH: "",
        }

        self.viewLayoutParam = {
            KEY_VIEW_VALUE: "",
            KEY_VIEW_ROOT: '',
        }

    def is_adapter(self):
        return TYPE_A in self.types

    def is_mvp(self):
        return TYPE_MVP in self.types

    def __get_types(self):
        self.types = self.type.rstrip("|").lstrip("|").split("|")
        return self.types

    def make(self, parser, pageName):
        self.pageNum = pageName
        self.make_parser(parser, pageName)
        (self.pageName, self.subPath) = self.get_path_param(self.subPackage)
        # (modelName, modelPath) = self.get_path_param(self.itemModel)
        self.__make_fragment()
        self.__make_view()
        self.__make_presenter()
        self.__make_view_layout()

    def __make_fragment(self):
        self.pageFragmentParam[KEY_PAGE_NAME] = self.pageName
        self.pageFragmentParam[KEY_PAGE_VIEW_NAME] = "fragment_" + self.pageName.lower()
        self.pageFragmentParam[KEY_PAGE_SUB_PATH] = self.subPath

    def __make_view(self):
        self.viewParam[KEY_PAGE_NAME] = self.pageName
        self.viewParam[KEY_PAGE_SUB_PATH] = self.subPath

    def __make_view_layout(self):
        items = self.viewLayout.split('|')
        self.viewLayoutParam[KEY_VIEW_ROOT] = items[0]
        self.viewLayoutParam[KEY_VIEW_VALUE] = items[1]

    def __make_presenter(self):
        self.presenterParam[KEY_PAGE_NAME] = self.pageName
        self.presenterParam[KEY_PAGE_SUB_PATH] = self.subPath

    def get_param(self):
        return self.pageFragmentParam, self.viewParam, self.presenter


class AppParser:

    def __init__(self, config_file):
        self.config_file = config_file
        self.__configParser = ConfigParser.ConfigParser()
        self.__configParser.read(config_file)
        self.projectBean = ProjectBean()
        self.buildBean = BuilderBean()
        self.pages = []

    def __get_value(self, section, key, default=""):
        if self.__configParser.has_option(section, key):
            return self.__configParser.get(section, key)
        else:
            return default

    def parse_config(self):
        parser = self.__get_value
        # parse
        self.projectBean.make(parser)
        self.buildBean.make(parser)
        self.make_pages()

    def make_pages(self):
        sections = self.__configParser.sections()
        for i in range(0, 100):
            name = PGAE + str(i)
            if name in sections:
                ret = PageBean()
                ret.make(self.__get_value, name)
                self.pages.append(ret)

    def get_project_bean(self):
        return self.projectBean

    def get_build_bean(self):
        return self.buildBean

    def get_pages(self):
        return self.pages


if __name__ == '__main__':
    config = AppParser("./app.config")
    config.parse_config()
    print(config.get_pages()[0].log())

    # pageBean = PageBean()
