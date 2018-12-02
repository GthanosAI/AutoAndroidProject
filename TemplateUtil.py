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


def template_text(content, param):
    ret = Template(content)
    return ret.safe_substitute(param)


def rename_dir(source, dst):
    cp_dir(source, dst)

    shutil.rmtree(source)


def cp_dir(source, dst):
    shutil.copytree(src=source, dst=dst)


def cp_file(source, dest):
    shutil.copy(src=source, dst=dest)
