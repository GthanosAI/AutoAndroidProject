import logging
from tool.Logger import loggingConfig
from CreateProject import AppParser
from CreateProject import AndroidProjectCreator
from BussGenerator import PageGenerator

if __name__ == '__main__':
    loggingConfig()
    logging.debug("begin to parser")
    appParser = AppParser('./app.config')
    appParser.parse_config()
    logging.debug("parser finish")
    creator = AndroidProjectCreator(appParser)
    creator.make()
    logging.debug("create project success")

    logging.debug("begin to generate pages ")
    projectBean = appParser.get_project_bean()
    pages = appParser.get_pages()

    coder = PageGenerator(pages, projectBean)
    coder.generate()
    logging.debug("generate pages success")
