#this is a class that sets the foudation

class matrix():
    def __init__(self,m):         
        self.m=list()
        self.line=len(m)

        if type(m[0]) == list:
            self.row=len(m[0])
            for line in range(0,self.line):
                self.m.append([])
                for row in range(0,self.row):
                    
                    self.m[line].append(m[line][row])
        elif type(m[0]) != list:
            self.row=1
            for line in range(0,self.line):
                self.m.append([m[line]])

       #在构造函数中，分两种情况：1.MXN的矩阵 2.1XN矩阵。两种情况分别考虑通过 matrix.m的属性来访问矩阵

    def get_line(self):         
        return self.line
    def get_row(self):
        return self.row

    def __add__(self,other):  #矩阵相加
        c=matrix(self.m)
        if self.line==other.line and self.row==other.row:
            for i in range(0,self.line):
                for j in range(0,self.row):
                    c.m[i][j]=self.m[i][j]+other.m[i][j]
        return c

    def __sub__(self,other):  #矩阵减法
        c=matrix(self.m)
        if self.line==other.line and self.row==other.row:
            for i in range(0,self.line):
                for j in range(0,self.row):
                    c.m[i][j]=self.m[i][j]-other.m[i][j]
        return c

    def __mul__(self,other):  #矩阵之间相乘
        c=list()
        for i in range(0,self.line):
            c.append([])
            for j in range(0,other.row):
                result=0
                for r in range(0,self.row):
                    result=result+ self.m[i][r]*other.m[r][j]
                c[i].append(result)
        new=matrix(c)

        return new

    def mul(self,a):             #矩阵数乘
        for i in range(0,self.line):
            for j in range(0,self.row):
                self.m[i][j]=a*self.m[i][j]



def zeros(line,row):
    zero=[]
    for i in range(0,line):
        zero.append([])
        for j in range(0,row):
            zero[i].append(0)

    zero=matrix(zero)
    return zero

def subarray(mat,i,j):         #计算矩阵的ij 主子阵
    sub=zeros(mat.line-1,mat.row-1)
    line_holder = [x for x in range(0,mat.line)]
    row_holder=[y for y in range(0,mat.row)]
    del line_holder[i]
    del row_holder[j]
    counter1=-1
    
    for a in line_holder:
        counter1=counter1+1
        counter2=-1
        for b in row_holder:
            
            counter2=counter2+1
            sub.m[counter1][counter2]=mat.m[a][b]
    return sub

def determinant(mat):      #计算方阵的行列式
    if mat.line==2 and mat.row==2:
        return mat.m[0][0]*mat.m[1][1]-mat.m[0][1]*mat.m[1][0]
    else:
        ans=0
        for row in range(0,mat.row):
            ans=ans+(-1)**(row)*(determinant(subarray(mat,0,row)))
    return ans

def inverse_matrix(mat):   #矩阵求逆
    if mat.line==mat.row and determinant(mat)!=0:
        inverse=zeros(mat.line,mat.row)
        for i in range(0,mat.line):
            for j in range(0,mat.row):
                inverse.m[i][j]=((-1)**(i+j)*determinant(subarray(mat,i,j)))
        det_mat=determinant(mat)
        for i in range(0,mat.line):
            for j in range(0,mat.row):
                inverse.m[i][j]=inverse.m[i][j]*(1/det_mat)
        return inverse
    else:
        print('error')
    
    

def trans(mat):                 #矩阵转置
    c=[]
    for i in range(0,mat.row):
        c.append([])
        for j in range(0,mat.line):
            c[i].append(0)

    new_c=matrix(c)
    for i in range(0,new_c.line):
        for j in range(0,new_c.row):
                new_c.m[i][j]=mat.m[j][i]
    return new_c



def slices(mat,start_line,end_line,start_row,end_row):
    sliced_matrix=zeros(end_line-start_line,end_row-start_row)
    for i in range(0,sliced_matrix.line):
        for j in range(0,sliced_matrix.row):
            sliced_matrix.m[i][j]=mat.m[start_line+i][start_row+j]

    return sliced_matrix

#slices（）获取矩阵的子阵
#其中五个参数分别为原矩阵，开始行a,结束行b,开始列c与结束列d
#slices()获取a to b-1 行， c to d-1 列的矩阵
    

   
    



def array(m):
    mat=matrix(m)

    return mat
#设置新矩阵的方法
#代码示例： c=array([[][]]) 与numpy 大同小异




        
