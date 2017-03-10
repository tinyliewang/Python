# catday5-socket-server.py
#!/usr/bin/python
import socket   #socket模块
#import commands   #执行系统命令模块
HOST='17.100.0.235'
PORT=50007
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
s.bind((HOST,PORT))   #套接字绑定的IP与端口
s.listen(1)         #开始TCP监听
while 1:
       conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
       print('Connected by',addr)    #输出客户端的IP地址
       while 1:
              data=conn.recv(1024)    #把接收的数据实例化
              #cmd_status,cmd_result=commands.getstatusoutput(data)
              print(data)
              #data += 1
              #print(data)
              conn.sendall(data)
              break
print("close")
#conn.close()     #关闭连接
