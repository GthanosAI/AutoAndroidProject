from TemplateUtil import template_file, cp_dir, rename_dir
import os, shutil


class GradleConfig:
    def __init__(self, project_dir):
        self.config = {
            "plugin_file": project_dir + "/gradle/wrapper/gradle-wrapper.properties",
            "build_file": project_dir + "/build.gradle"
        }

    def set_param(self, plugin_version="", build_version=""):
        self.params = [
            {'file_name': self.config['plugin_file'],
             'param': {'gradle_plugins': plugin_version}
             },
            {'file_name': self.config['build_file'],
             'param': {'gradle_build_version': build_version}
             }
        ]

    def make(self):
        for param in self.params:
            template_file(param['file_name'], param['param'])


class AppConfig:
    def __init__(self, project_dir):
        self.config = {
            "xml_package_file": project_dir + "/app/src/main/AndroidManifest.xml",
            'settings_project_file': project_dir + '/settings.gradle'
        }

    def set_param(self, package_name, project_name):
        self.params = [
            {
                "file_name": self.config['xml_package_file'],
                'param': {'package_name': package_name}
            },

            {
                "file_name": self.config['settings_project_file'],
                'param': {'project_name': project_name}
            }
        ]

    def make(self):
        for param in self.params:
            template_file(param['file_name'], param['param'])


class AndroidProjectCreator:

    def __init__(self, package_name, project_name):
        self.project_param = {
            'package_name': package_name,
            'project_name': project_name,
            'plugin_version': 'gradle-4.6-all',
            'build_version': 'com.android.tools.build:gradle:3.1.0-alpha08',
        }

    def make(self):
        # 1 make output dir
        current_dir = os.path.dirname(os.path.realpath(__file__))
        source_dir = current_dir + '/res/app'
        dst_dir = current_dir + '/output/' + self.project_param['project_name']

        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)

        cp_dir(source_dir, dst_dir)

        # 2. rename source file name
        src_dir = dst_dir + '/app/src/main/java/com/ifog/myapplication'
        new_src_dir = dst_dir + '/app/src/main/java/' + self.project_param['package_name'].replace(".", '/')

        rename_dir(src_dir, new_src_dir)

        # 3. config app and config gradle config
        app_config = AppConfig(dst_dir)
        gradle_config = GradleConfig(dst_dir)

        app_config.set_param(self.project_param['package_name'], self.project_param['project_name'])
        gradle_config.set_param(self.project_param['plugin_version'], self.project_param['build_version'])

        app_config.make()
        gradle_config.make()


if __name__ == '__main__':
    creator = AndroidProjectCreator('com.demo.helloworld', "Helloworld")
    creator.make()