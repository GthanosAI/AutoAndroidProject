from string import Template
import os
if __name__ == '__main__':
    s1 = Template('${test} helloworld')
    print(s1.safe_substitute({'test1': "hewei"}))

    print(os.path.dirname(os.path.realpath(__file__)))

    print("com.test.demo".replace('.', '/'))
