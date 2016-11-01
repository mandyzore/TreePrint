# TreePrint
如何优雅的打印tree结构

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
