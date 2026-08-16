class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        for i in range(len(mat)):
            for j in range(i, len(mat[0])):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(len(mat)):
            mat[i].reverse()
            
