# 服务端进程，用于分配任务给另一进程去（可以是本地或分布）
import random, time, queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
back_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue

def return_back_queue():
    global back_queue
    return back_queue

def test():
    # 将两个队列注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_back_queue', callable=return_back_queue)
    # 绑定端口5000， 设置验证码‘Miss’
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'Miss')
    # 启动Queue
    manager.start()
    
    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    back = manager.get_back_queue()

    # 尝试放几个任务进去
    for i in range(10):
        num = random.randint(0, 10000)
        print('server put task %d...' % num)
        task.put(num)

    # 从back队列中读取结果
    print('...try get back_queue...')
    for i in range(10):
        result = back.get(timeout=10)
        print('result: %s' % result)
    # 关闭
    manager.shutdown()
    print('master exit()')

if __name__ == '__main__':
    freeze_support()
    test()