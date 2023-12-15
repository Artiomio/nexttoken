class SparseMatrix:
    def __init__(self, shape):
        self.shape = shape
        self.matrix_dict = {}
    
    @staticmethod
    def get_index_key(indices):
        return  " ".join([str(x) for x in indices])

    def __getitem__(self, pos):
        #any_slices = any([isinstance(x, slice) for x in pos])
        

        
        #if not any_slices:
        return self.matrix_dict.get(SparseMatrix.get_index_key(pos), 0)


    def __setitem__(self, pos, value):
        self.matrix_dict[SparseMatrix.get_index_key(pos)] = value

