import math
import random
from sympy import primerange, sqrt, log, Rational
import matplotlib.pyplot as plt

#  对一个字典按照键大小升序排序，需要返回
def sort_dict_key(my_dict):
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[0], reverse=False)
    my_dict = dict(sorted_dict)
    return my_dict

#  对一个字典按照值大小降序排序，需要返回
def sort_dict_value(my_dict):
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=False)
    my_dict = dict(sorted_dict)
    return my_dict

#  打印一个置乱
def print_permutated_table(permutated_table):
    for i in list(permutated_table.keys()):
        print("{:<4}".format(i), end='')
    print()
    for i in list(permutated_table.values()):
        print("{:<4}".format(i), end='')

#  得到一个随机的N个数的置乱
def get_permutated_table(N):
    y = [i for i in range(1, N+1)]

    random.seed()
    random.shuffle(y)
    permutated_table = {i+1:y[i] for i in range(N)}
    
    return permutated_table




#  求一个置乱的分解
def get_decomposition_of_permutated_table(ori_permutated_table):
    permutated_table = ori_permutated_table.copy()
    counter = 0

    if not permutated_table:
        return []
    
    #  随机弹出一个键值对
    start, iterator = permutated_table.popitem()
    counter += 1

    while(True):
        if start == iterator:
            break

        iterator = permutated_table.pop(iterator)
        counter += 1
    
    part_decomposition_list = get_decomposition_of_permutated_table(permutated_table)
    part_decomposition_list.append(counter)
    return part_decomposition_list

#  求一个置乱的阶
def get_order_of_permutated_table(decomposition_list):
    if len(decomposition_list) == 0:
        return None
    elif len(decomposition_list) == 1:
        return decomposition_list[0]
    

    lcm = decomposition_list[0] * decomposition_list[1] // math.gcd(decomposition_list[0], decomposition_list[1])
    for i in range(2, len(decomposition_list)):
        lcm = (lcm * decomposition_list[i]) // math.gcd(lcm, decomposition_list[i])
    
    return lcm




#  求N的最大阶
def get_greatestorder_of_N(N): # compute terms a(0)..a(N)
    V = [1 for j in range(N+1)]
    if N < 4:
        C = 2
    else:
        C = Rational(166, 125)
    for i in primerange(C*sqrt(N*log(N))):
        for j in range(N, i-1, -1):
            hi = V[j]
            pp = i
            while pp <= j:
                hi = max(V[j-pp]*pp, hi)
                pp *= i
            V[j] = hi
    return V




#  求给定N时，它的所有分解
def decompose(num):
    result = []
    decompose_helper(num, [], result)
    return result

def decompose_helper(num, current, result):
    if num == 0:
        result.append(current)
        return
    for i in range(1, num+1):
        if not current or i >= current[-1]:
            decompose_helper(num-i, current+[i], result)



#  给定N时，求pK_tabel
def get_pk_table(N):
    res = decompose(N)

    pk_table = {}

    for i in res:
        order = get_order_of_permutated_table(i)
        if order in pk_table:
            pk_table[order] += 1
        elif order not in pk_table:
            pk_table[order] = 1

    pk_table = sort_dict_key(pk_table)


    sum = 0

    for i in pk_table.values():
        sum +=i
    

    F = 0
    for i in pk_table:
        F +=pk_table[i]
        pk_table[i] = F / sum
        

    return pk_table

#  画图
def draw_pk(pk_table, N):
    
    x = list(pk_table.keys())
    y = list(pk_table.values())

    plt.plot(x, y)
    plt.title('pk(N={0})'.format(N))
    plt.xlabel('K')
    plt.ylabel('pk')

    plt.show()





#  生成混沌表
def get_Logistic_table(N, mu, x0):
    if x0 < 0 or x0 > 1:
        raise Exception('x0的值应该在0与1之间')
    Logistic_table = {}
    Logistic_table[1] = mu * x0 * (1 - x0)
    for i in range(2, N+1):
        Logistic_table[i] = mu * Logistic_table[i-1] * (1 - Logistic_table[i-1])

    Logistic_table = sort_dict_value(Logistic_table)

    k = 1
    for i in Logistic_table:
        Logistic_table[i] = k
        k += 1

    return Logistic_table

#  画出混沌置乱散点图
def draw_Logistic(N, mu):
    x0 = []
    order = []
    for i in range(N**2):
        x0.append(random.random())
        Logistic_table = get_Logistic_table(N, mu, x0[i])
        # print_permutated_table(Logistic_table)
        list = get_decomposition_of_permutated_table(Logistic_table)
        order.append(get_order_of_permutated_table(list))


    plt.scatter(x0, order, s=5)
    plt.title('Logistic assessment(N={0})'.format(N))
    plt.xlabel('x0')
    plt.ylabel('order')

    plt.show()



#  已知pk_table，画出pk曲线
if __name__ == '__main__':
    N = 10
    # print('{0}个数的置乱最大阶为'.format(N), get_greatestorder_of_N(N)[-1])
    
    # permutated_table = get_permutated_table(N)
    # print('随机得到的一个{0}个数的置乱为'.format(N))
    # print_permutated_table(permutated_table)
    # print('\n\n')

    # decomposition_list = get_decomposition_of_permutated_table(permutated_table)
    # print('这个置乱的分解为', decomposition_list)

    # order = get_order_of_permutated_table(decomposition_list)
    # print('这个置乱的阶', order)

    pk_table = get_pk_table(N)
    draw_pk(pk_table, N)