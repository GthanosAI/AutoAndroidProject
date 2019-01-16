from ViewConstant import get_map

viewCount = 0


class ResultBean:
    def __init__(self, letter, content='', name=""):
        self.startLetter = letter
        self.content = content.replace(' ', '')
        self.length = len(content)
        self.childList = []
        self.name = name
        self.view_content = None

    def add(self, child):
        self.childList.append(child)

    def is_view(self):
        return len(self.childList) == 0

    def find(self):
        pass

    def make(self):
        input_content = self.content[1:self.length - 1]
        tool = ContentViewHierarchy(input_content)
        make_result = tool.make()
        for item in make_result:
            self.add(item)
            if item.is_view():
                item.make()

    def make_view(self):
        viewFunc = get_map(self.startLetter)
        if self.is_view():
            ret_content = viewFunc(self.name)

        else:
            viewGroup = viewFunc
            items = []
            for item in self.childList:
                item_view = item.make_view()
                items.append(item_view)
            ret_content = viewGroup(self.name, items)
        self.view_content = ret_content
        return ret_content

    def log(self):
        print(self.startLetter, self.view_content, len(self.childList))
        for item in self.childList:
            item.log()


class ContentViewHierarchy:

    def __init__(self, content):
        self.content = content

    def make(self):
        return self.__get_view_hierarchy(self.content)

    def get_result(self):
        pass

    def __get_view_hierarchy(self, content=""):
        return self.__get_odd_right_bracket(content)

    def get_item(self, start, end, content, value):
        global viewCount
        viewCount = viewCount + 1
        name = 'v' + value + str(viewCount)
        return ResultBean(value, content, name)

    def __get_odd_right_bracket(self, content):
        index = 0
        findIndex = -1
        start_index = 0
        ret = []
        flag = False
        splitFlag = False
        mayBeNext = False
        startLetter = None
        contentLength = len(content)

        if contentLength == 0:
            return []

        if contentLength == 1:
            item = self.get_item(0, 1, content, content)
            ret.append(item)
            return ret

        if contentLength > 1:
            startLetter = content[0]

        for a in content:
            findIndex = findIndex + 1
            if findIndex == 0 and contentLength > 1 and content[1] == ',':
                mayBeNext = True
                start_index = findIndex
                startLetter = a
                continue

            if mayBeNext and ((a == ',')
                    #
                    # or (contentLength == findIndex)
            ):
                mayBeNext = False
                item = self.get_item(start_index,
                                     findIndex,
                                     content[start_index:findIndex],
                                     startLetter)
                ret.append(item)
                flag = False
                splitFlag = True
                continue

            if mayBeNext:
                mayBeNext = False

            if splitFlag:
                splitFlag = False
                startLetter = a
                start_index = findIndex
                # next is
                mayBeNext = True
                continue

            if flag and a == ',':
                flag = False
                splitFlag = True
                continue

            if a == '[':
                mayBeNext = False
                index = index + 1
            elif a == ']':
                mayBeNext = False
                index = index - 1
                if index == 0:
                    item = self.get_item(start_index,
                                         findIndex,
                                         content[start_index + 1:findIndex + 1],
                                         startLetter)

                    ret.append(item)
                    start_index = index
                    index = 0
                    startLetter = None
                    flag = True

        if startLetter and mayBeNext:
            item = self.get_item(contentLength - 1,
                                 contentLength,
                                 startLetter,
                                 startLetter)
            ret.append(item)

        return ret


def make(root='', content="", xml_name=""):
    result_bean = ResultBean(root, content, 'vl0')
    result_bean.make()
    result_content = result_bean.make_view()
    with open(xml_name, 'w') as tf:
        tf.write(result_content)


if __name__ == '__main__':
    # a = 'i'
    # c = ContentViewHierarchy(a)
    # c.make()

    make('L', '[c[c[i,i,r[i],i,i],i],c[i,i]]', 'fragment_layout.xml')
