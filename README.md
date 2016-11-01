# TreePrint
论如何优雅的在python中打印tree结构

---------------------------

记：最近做了一些纯文本的文章结构抽取的工作，抽取器debug过程中需要不断地加入‘监督’（真人工·智能），以下是即该过程中的降低认知难度的一些零碎东西。(Oct 30, Beijing)

---------------------------


节点类的格式化输出函数：
```
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
```

输出样例：

```

====================================
  一、父节点
   # 我是父节点，我是父节点，我是父节点，我是父节点
    1. 孩子节点1
     # 我是孩子1
    2. 孩子节点2
     # 我是孩子2

```
