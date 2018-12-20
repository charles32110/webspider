# -*- coding: utf-8 -*
#threading learning，代码来自china_python
import requests
import Queue
import threading


class testproxy():
    # 初始化参数
    def __init__(self):
        self.url = 'http://www.baidu.com/'
        self.ip_list_queue = Queue.Queue()  # 创建队列用于存储所有代理
        self.proxy_queue = Queue.Queue()  # 创建存储有效代理

    # 获取代理ip
    def get_ip(self):
        with open('thebigproxylist-18-12-19.txt') as f:
            ip_list = f.readlines()
        for ip in ip_list:
            ip = ip.strip()
            # proxy = {"http":"http://" + ip,"https":"http://" + ip,}
            self.ip_list_queue.put(ip)  # 存放到队列

    # 验证代理ip
    def check_ip(self):
        while True:
            ip = self.ip_list_queue.get()  # 在队列中取proxy
            try:
                proxy = {"http": "http://" + ip}
                requests.get(self.url, proxies=proxy, timeout=1)
                ip = ip
                print(ip)
            except:
                ip = None
            finally:
                self.proxy_queue.put(ip)  # 存入队列
            self.ip_list_queue.task_done()  # 队列计数减一

    # 写入可用ip
    def write_ip(self):
        while True:
            ip = self.proxy_queue.get()  # 取
            if ip is not None:
                with open('./proxy.txt', 'a') as f:
                    f.write(ip + '通过'+ '\n'+'_____________________'+ '\n' )
            self.proxy_queue.task_done()  # 减

    # 运行主逻辑
    def run(self):
        thread_list = []
        t_get_ip = threading.Thread(target=self.get_ip)
        thread_list.append(t_get_ip)
        for i in range(30):
            t_check_ip = threading.Thread(target=self.check_ip)
            thread_list.append(t_check_ip)
        t_write_ip = threading.Thread(target=self.write_ip)
        thread_list.append(t_write_ip)
        for t in thread_list:
            t.setDaemon(True)  # 守护线程
            t.start()
        for q in [self.ip_list_queue, self.proxy_queue]:
            q.join()
        print('运行结束')


if __name__ == '__main__':
    start = testproxy()
    start.run()


