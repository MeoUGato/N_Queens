class square:
    def __init__(self,row,col,queen=None):
        self.row = row
        self.col = col
        self.queen = queen
    def has_queen(self):
        return self.queen != None
    