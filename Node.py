#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Node:

    """
        节点类
    """

    def __init__(self, title):
        self.title = title
        self.content = ""
        self.children = []
        self.parent = None
        self.level = None
        self.out = ""

    def getTitle(self):
        return self.title

    def getChildren(self):
        return self.children

    def getContent(self):
        return self.content

    def getParent(self):
        return self.parent

    def getLevel(self):
        return self.level

    def setTitle(self,title):

        self.title = title

    def setContent(self,content):
        self.content = content

    def setParent(self,parent):
        self.parent = parent

    def setLevel(self,level):
        self.level = level

    def addChild(self,child):
        self.children.append(child)

    def format_print(self, prefix):
        '''
            格式化输出
        '''

        if prefix=="":
            self.out = '\n====================================\n'
        else:
            self.out = ""

        prefix+='  ' # 父子层之间的缩进
        self.out+='{}{}\n'.format(prefix, self.getTitle()) # 标题
        self.out+=' {}# {}\n'.format(prefix, self.getContent().replace('\n', '')) # 内容
        
        for child in self.getChildren():
            child.format_print(prefix)
            self.out+=child.out
        
        return self.out


if __name__ == '__main__':

    root = Node("一、父节点")
    root.setContent("我是父节点，我是父节点，我是父节点，我是父节点")

    child1 = Node("1. 孩子节点1")
    child1.setContent("我是孩子1")
    child2 = Node("2. 孩子节点2")
    child2.setContent("我是孩子2")
    
    root.addChild(child1)
    root.addChild(child2)

    print(root.format_print(""))



