import threadpool
from main import *

print("多线程开始执行......")
pool = threadpool.ThreadPool(15)
args_list = list(range(1000))
req = threadpool.makeRequests(subThread, args_list)
[pool.putRequest(temp) for temp in req]
pool.wait()

args_list = getParamList()
while len(args_list) != 0:
    print("还需要对此数组请求一遍...args_list --> ", args_list)
    req = threadpool.makeRequests(subThread, args_list)
    [pool.putRequest(temp) for temp in req]
    pool.wait()
    args_list = getParamList()

print("多线程执行结束......")
