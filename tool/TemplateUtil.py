from string import Template
import shutil, os, stat
import io
from Constant import *


def template_file(source, param):
    with io.open(source, 'r', encoding='utf-8') as tf:
        content = tf.read()
    content = content.encode('utf-8')
    new_content = template_text(content, param)
    with open(source, 'w') as fp:
        fp.write(new_content)
    return source


def template_file_param(param):
    template_file(param[KEY_PARAM_FILE], param[KEY_PARAM_PARAM])


def list_file(root, suffix=None):
    files = []
    for main_dir, sub_dir, file_name_list in os.walk(root):
        for file_name in file_name_list:
            full_file = os.path.join(main_dir, file_name)
            if suffix is not None:
                if file_name.split('.')[-1] == suffix:
                    files.append(full_file)
            else:
                files.append(file_name)
    return files


def template_text(content, param):
    ret = Template(content)
    return ret.safe_substitute(param)


def rename_dir(source="", dst=""):
    # cp_dir(source, dst)
    # shutil.rmtree(source)
    shutil.move(source, dst)


def cp_dir(source, dst):
    shutil.copytree(src=source, dst=dst)


def cp_file(source, dst):
    shutil.copy(src=source, dst=dst)


def create_path(path):
    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    cp_file("./a", "./b.txt")
    # ret = list_file("/Users/jacky/PycharmProjects/AutoAndroidProject/res/app/app/src/main/java", suffix='java')
    # print(ret)
