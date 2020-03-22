class Matrix:

    def __init__(self, matrix_string):
        m = matrix_string.split('\n')
        mat = []
        for i in range(0, len(m)):
            mat.append([int(a) for a in (m[i].split())])
        self.mat = mat

    def row(self, index):
        return self.mat[index-1]

    def column(self, index):
        ret = []
        for i in range(0, len(self.mat)):
            ret.append(self.mat[i][index-1])
        return ret
