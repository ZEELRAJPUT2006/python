class demo:
    def __init__(self,item):
        self.item = item

    def __setitem_(self,index,value):
        self.item[index] = value

    def _getitem_(self,index):
        return self.item[index]
    
d = demo([10,20,30,40])
d[2] = 100
print(d[1])