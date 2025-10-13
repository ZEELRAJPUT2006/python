class demo:
    def __init__(self,item):
        self.item = item

    def __setattr__(self, index, value):
        self.item[index] = value

    def _getitem_(self,index):
        return self.item[index]
    
