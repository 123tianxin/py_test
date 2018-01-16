import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager：
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字：
QueueManager.register('get_task_queue')
QueueManager.register('get_back_queue')

print('Connect to server %s...' % '127.0.0.1')
# 端口和验证码保持一致
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'Miss')
# 从网络连接
manager.connect()

# 获取Queue的对象
task = manager.get_task_queue()
back = manager.get_back_queue()

for i in range(10):
    try:
        num = task.get(timeout=1)
        print('worker run task %d * %d...' % (num, num))
        result = '%d * %d = %d' % (num, num, num*num)
        time.sleep(1)
        back.put(result)
    except Queue.Empty as e:
        print('task queue is empty.')

print('work exit()')