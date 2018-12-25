from string import Template
import shutil, os, stat
import io


def template_file(source, param):
    with io.open(source, 'r', encoding='utf-8') as tf:
        content = tf.read()

    new_content = template_text(content, param)
    with open(source, 'w') as fp:
        fp.write(new_content)
    return source


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


def cp_file(source, dest):
    shutil.copy(src=source, dst=dest)


if __name__ == '__main__':
    ret = list_file("/Users/jacky/PycharmProjects/AutoAndroidProject/res/app/app/src/main/java", suffix='java')
    print(ret)