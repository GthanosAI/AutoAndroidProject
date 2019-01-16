from CreateProject import AndroidProjectCreator
from ProjectParser import PageBean, AppParser
from tool.TemplateUtil import cp_file, template_file, template_text, create_path
from tool.Constant import *
from tool.ViewHierarchy import make as viewmaker
import os


class BaseGenerator:
    def __init__(self):
        pass

    def generate(self):
        pass


class PageGenerator(BaseGenerator):
    @staticmethod
    def get_path(root, sub1="", sub2="", sub3=""):
        ret = os.path.join(root, sub1.lstrip('/'), sub2.lstrip('/'), sub3.lstrip('/'))
        return ret.rstrip('/')

    def __init__(self, pageBeans, projectBean):
        BaseGenerator.__init__(self)

        self.project_name = projectBean.project
        self.package_name = projectBean.package
        self.projectDir = projectBean.projectDir
        self.package_name_path = self.package_name.replace(".", "/")
        self.current_dir = AndroidProjectCreator.get_current_dir()
        self.source_dir = self.get_path(self.current_dir, RES_MVP)
        self.dst_dir = self.get_path(self.current_dir, self.projectDir, self.project_name)
        self.pages = pageBeans

        # page path
        self.src_root_path = self.get_path(self.dst_dir, JAVA_SRC_PATH, self.package_name_path)
        self.res_layout_path = self.get_path(self.dst_dir, APP_RES_LAYOUT)

    @staticmethod
    def get_abs_param(file_path, value):
        return {
            KEY_PARAM_FILE: file_path,
            KEY_PARAM_PARAM: value
        }

    def generate_fragment(self, pageBean):
        subPath = pageBean.subPath
        src_file = self.get_path(self.source_dir, FRAGMENT)
        page_fragment_param = pageBean.pageFragmentParam

        dst_file_name = template_text(TEMPLATE_FRAGMENT, page_fragment_param)
        dst_file = self.get_path(self.src_root_path, subPath, dst_file_name)

        create_path(dst_file)

        cp_file(src_file, dst_file)
        page_fragment_param[KEY_PACKAGE_NAME] = self.package_name
        template_file(dst_file, page_fragment_param)

    def generate_vp(self, pageBean):
        # view
        subPath = pageBean.subPath
        viewParam = pageBean.viewParam
        src_file = self.get_path(self.source_dir, IVIEW)
        dst_file_name = template_text(TEMPLATE_VIEW, viewParam)
        dst_file = self.get_path(self.src_root_path, subPath, dst_file_name)
        cp_file(src_file, dst_file)
        viewParam[KEY_PACKAGE_NAME] = self.package_name

        template_file(dst_file, viewParam)

        # presenter
        presenterParam = pageBean.presenterParam
        src_file = self.get_path(self.source_dir, PRESENTER)
        dst_file_name = template_text(TEMPLATE_PRESENTER, presenterParam)
        dst_file = self.get_path(self.src_root_path, subPath, dst_file_name)
        cp_file(src_file, dst_file)
        presenterParam[KEY_PACKAGE_NAME] = self.package_name
        template_file(dst_file, presenterParam)

    def generate_view_layout(self, pageBean):
        viewLayout = pageBean.viewLayoutParam
        viewLayoutFileName = template_text(TEMPLATE_VIEW_LAYOUT,
                                           {KEY_PAGE_NAME_LOWCASE: pageBean.pageName.lower()})
        dst_file = self.get_path(self.res_layout_path, viewLayoutFileName)
        viewmaker(viewLayout[KEY_VIEW_ROOT], viewLayout[KEY_VIEW_VALUE], dst_file)

    def generate(self):
        for pageBean in self.pages:
            self.generate_fragment(pageBean)
            self.generate_vp(pageBean)
            self.generate_view_layout(pageBean)


if __name__ == '__main__':
    config = AppParser("./app.config")
    config.parse_config()

    projectBean = config.get_project_bean()
    pages = config.get_pages()

    coder = PageGenerator(pages, projectBean)
    coder.generate()
