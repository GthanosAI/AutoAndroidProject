from tool.TemplateUtil import template_file, template_file_param, cp_dir, rename_dir, list_file
import os, shutil
from tool.Constant import *
from ProjectParser import AppParser
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='new.log',
                    filemode='a',
                    format=
                    '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


class Generator:
    def __init__(self, project_dir):
        self.project_dir = project_dir
        self.params = []

    def make(self):
        pass

    def get_single_param(self, file_path, key, param):
        return {
            KEY_PARAM_FILE: self.project_dir + file_path,
            KEY_PARAM_PARAM: {
                key: param[key]
            }
        }

    def get_abs_param(self, file, key, value):
        return {
            KEY_PARAM_FILE: file,
            KEY_PARAM_PARAM: {
                key: value
            }
        }

    def make(self):
        for param in self.params:
            template_file_param(param)


class GradleGenerator(Generator):
    def __init__(self, project_dir, config_bean):
        Generator.__init__(self, project_dir)

        param_plugin = self.get_single_param(
            GRADLE_PLUGIN_FILE,
            KEY_GRADLE_PLUGIN,
            config_bean
        )

        param_gradle = self.get_single_param(
            GRADLE_FILE,
            KEY_GRADLE,
            config_bean
        )

        self.params.append(param_gradle)
        self.params.append(param_plugin)


class ProjectGenerator(Generator):
    def __init__(self, project_dir, config_bean):
        Generator.__init__(self, project_dir)

        xml_package = self.get_single_param(
            XML_PACKAGE_FILE,
            KEY_PACKAGE_NAME,
            config_bean
        )

        build = self.get_single_param(
            APP_BUILD_FILE,
            KEY_PACKAGE_NAME,
            config_bean
        )

        self.params.append(xml_package)
        self.params.append(build)


class CodeConfig(Generator):
    def __init__(self, project_dir, package_name):
        Generator.__init__(self, project_dir)
        root_file = project_dir + JAVA_SRC_PATH + package_name.replace(".", "/")
        file_list = list_file(root_file, suffix='java')

        for file_item in file_list:
            item = self.get_abs_param(
                file_item,
                KEY_PACKAGE_NAME,
                package_name
            )
            self.params.append(item)


class AndroidProjectCreator:

    def __init__(self, parser):
        self.projectBean = parser.get_project_bean()
        self.buildBean = parser.get_build_bean()

        self.package_name = self.projectBean.package
        self.projectDir = self.projectBean.projectDir
        self.package_name_path = self.package_name.replace(".", "/")
        self.project_name = self.projectBean.project
        self.gradle = self.buildBean.gradle
        self.plugin = self.buildBean.plugin

        self.current_dir = AndroidProjectCreator.get_current_dir()
        self.source_dir = self.current_dir + RES_APP
        self.dst_dir = self.get_path(self.current_dir,
                                     self.projectDir,
                                     self.project_name)

        self.java_src_path = JAVA_SRC_PATH
        self.java_test_src_path = JAVA_TEST_SRC_PATH

    @staticmethod
    def get_current_dir():
        return os.path.dirname(os.path.realpath(__file__))

    @staticmethod
    def get_path(root, sub1="", sub2="", sub3=""):
        return os.path.join(root, sub1, sub2, sub3)

    def make(self):
        # 1 make output dir
        if os.path.exists(self.dst_dir):
            shutil.rmtree(self.dst_dir)

        cp_dir(self.source_dir, self.dst_dir)

        # 2.1
        self.add_base()

        # 2. rename source file name
        # 1) rename source file
        src_dir = self.get_path(self.dst_dir, SRC_PATH)
        new_src_dir = self.get_path(self.dst_dir, self.java_src_path, self.package_name_path)
        rename_dir(src_dir, new_src_dir)

        # 2) rename test file
        test_src_dir = self.get_path(self.dst_dir, TEST_SRC_PATH)
        new_test_src_dir = self.get_path(self.dst_dir, self.java_test_src_path, self.package_name_path)
        rename_dir(test_src_dir, new_test_src_dir)

        logging.debug("create project path success")

        # 3. config app and config gradle config
        app_config = ProjectGenerator(self.dst_dir, self.projectBean.get_param())
        gradle_config = GradleGenerator(self.dst_dir, self.buildBean.get_param())
        code_config = CodeConfig(self.dst_dir, self.package_name)

        app_config.make()
        gradle_config.make()
        code_config.make()

    def add_base(self):
        pass


if __name__ == '__main__':
    logging.debug("begin to parser")
    appParser = AppParser('./app.config')
    appParser.parse_config()
    logging.debug("parser finish")
    creator = AndroidProjectCreator(appParser)
    creator.make()
    logging.debug("create project success")
