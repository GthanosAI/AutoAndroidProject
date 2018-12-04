from string import Template
import os
from CreateProject import AndroidProjectCreator

if __name__ == '__main__':
    creator = AndroidProjectCreator('com.demo.helloworld', "Helloworld")
    creator.make()

