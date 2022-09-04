class IterateDataFrame:

    """Iterator that returns a new register every iteration"""

    def __init__(self,  dataFrame):
        self.num = 0
        self.dataFrame = dataFrame

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1

        return self.dataFrame.loc[num]
