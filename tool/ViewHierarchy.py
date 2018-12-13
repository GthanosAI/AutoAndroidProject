class ResultBean:
    def __init__(self, letter, content):
        self.startLetter = letter
        self.content = content
        self.childList = []

    def add(self, child):
        self.childList.append(child)

    def is_view(self):
        return len(self.childList) == 0

    def find(self):
        pass


class ContentViewHierarchy:

    def __init__(self, content):
        self.content = content

    def make(self):
        return self.__get_view_hierarchy(self.content)

    def get_result(self):
        pass

    def __get_view_hierarchy(self, content=""):
        self.__get_odd_right_bracket(content, 'l')

    def get_item(self, start, end, content, value):
        return {
            'start': start,
            'end': end,
            'content': content,
            'vale': value
        }

    def __get_odd_right_bracket(self, content, startLetter):
        self.content
        index = 0
        findIndex = -1
        start_index = 0
        ret = []
        flag = False
        nextFlag = True
        for a in content:
            findIndex = findIndex + 1
            if nextFlag and a == '[':
                nextFlag = True
                continue

            if nextFlag:
                startLetter = a
                start_index = findIndex
                index = 0
                nextFlag = False
                continue

            if flag and a == ',':
                flag = False
                nextFlag = True
                continue

            if a == '[':
                index = index + 1
            elif a == ']':
                index = index - 1
                if index < 0:
                    item = self.get_item(start_index,
                                         findIndex,
                                         content[start_index:findIndex],
                                         startLetter)
                    ret.append(item)
                    start_index = index
                    index = 0
                    flag = True
                    continue

        print(ret)


if __name__ == '__main__':
    result = ResultBean("l", "[c[i,i,r,i,i], i],c[i,i]")
    view = ContentViewHierarchy('[a[i,i,r,i,i],i],h[i,i],c[i,i]]')
    view.make()
