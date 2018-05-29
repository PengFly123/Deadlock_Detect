# 死锁避免和死锁检测
from numpy import *
def found(needs, avail, rest):
    for i in range(needs.shape[0]):
        flag = 1
        if rest[i]==-1:
            continue
        for j in range(needs.shape[1]):
            if needs[i][j]>avail[j]:
                flag = 0
                break
        if flag==1 and i<needs.shape[0]:
            return i
    return -1
def detect(t):
    run = []
    rest = [1, 1, 1, 1]
    allocation, needs, avail = read_matrix(t)
    while len(run) < needs.shape[0]:
        process = found(needs, avail, rest)
        if process == -1:
            for i in range(len(run)):
                print(run[i], end=' ')
            print('此时发生死锁')
            input()
            break
        else:
            avail += allocation[process]
            allocation[process] -= allocation[process]
            run.append(process + 1)  # 运行队列的顺序
            rest[process] = -1  # 标记此进程已经运行完毕
            process += 1
            print('进程 %d 正在运行：' % process)
            print('Allocation Matrix:')
            print(allocation)
            input()
            print('Needs Matrix:')
            print(needs)
            input()
            print('Available Matrix:')
            print(avail)
            input()
    if len(run) == allocation.shape[0]:
        print("进程按照次顺序执行也避免死锁：",end=' ')
        for i in range(len(run)):
            print(run[i], end=' ')
        print('\n')

def read_matrix(t):
    contents = [['Claim1.txt', 'Allocation1.txt', 'Resource1.txt'],
                ['Claim3.txt', 'Allocation3.txt', 'Resource3.txt'],
                ['Claim2.txt', 'Allocation2.txt', 'Resource2.txt']]
    claim = []
    with open(contents[t][0]) as f:
        lines = f.readlines()
        for line in lines:
            claim.append([int(x) for x in line.split()])         # 将文件里面的数据读出来后放到列表;
    claim = array(claim)            # 转换成数组
    print("第%d组测试样例：\nClaim Matrix:" % (t+1))
    print(claim)
    input()

    allocation = []
    with open(contents[t][1]) as f:
        lines = f.readlines()
        for line in lines:
            allocation.append([int(x) for x in line.split()])         # 将文件里面的数据读出来后放到列表;
    allocation = array(allocation)          # 转换成数组
    print("\nAllocation Matrix:")
    print(allocation)
    input()
    needs = claim-allocation        # 各进程还需资源数
    print("\nNeeds Matrix:")
    print(needs)
    input()
    # 读取Resource矩阵
    with open(contents[t][2]) as f:                 # 读取总资源数
        line = f.readline()
        resource = [int(x) for x in line.split()]
    resource = array(resource)              # 转换成数组
    print("\nResource Matrix:")
    print(resource)
    input()
    avail = []
    for i in range(allocation.shape[1]):
        total = 0
        for j in range(allocation.shape[0]):
            total += allocation[j][i]
        avail.append(resource[i]-total)
    print("\nAvailable Matrix:")
    print(avail)
    input()
    return allocation, needs, avail
if __name__ == '__main__':
    t=0
    print("共有三组检测样例,请根据开始提醒检测:\n")
    while t<3:
        key = input("y:开始检测第%d组样例\ns:退出检测\n请选择：" % (1+t))
        if key == 'y':
            detect(t)
            t += 1
        elif key == 's':
            again = input('您还有未检查的样本，确认退出吗？\ny:确认\nn:继续检查\n')
            if again == 'y':
                break
            else:
                continue
        else:
            print("您的输入有误，请重新输入")
    if t==3:
        print('所有样例均已检查完毕')