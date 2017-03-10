# catday5-socket-client.py
#!/usr/bin/python
import socket
HOST='17.100.0.235'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
       #cmd=input("Please input cmd:")       #与人交互，输入命令
       cmd = "1"
       cmd = cmd.encode('utf-8')
       print(cmd)
       s.sendall(cmd)      #把命令发送给对端
       data=s.recv(1024)     #把接收的数据定义为变量
       print (data)         #输出变量
       break
print("close")
s.close()   #关闭连接
