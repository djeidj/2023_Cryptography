import permutation as pe
import time

if __name__ == '__main__':
    # N = 80
    # start = time.time()
    # pk_table = pe.get_pk_table(N)
    # pe.draw_pk(pk_table, N)
    # end = time.time()
    # print('N={0}时,绘制pk曲线所用时间为'.format(N), end - start)
    # print('{0}个数的置乱最大阶为'.format(N), pe.get_greatestorder_of_N(N)[-1])

    # N = int(input('请输入你想要测评Logistic时N的大小'))
    # mu = float(input('请输入mu的大小(3.57<mu<4)'))

    N = 30
    mu = 3.85
    pe.draw_Logistic(N, mu)