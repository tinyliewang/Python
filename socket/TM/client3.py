#Client
from tkinter import *
import socket, threading


def acceptMessage(sock, text):
    while True:
        RecvMessage = sock.recv(1024).decode()
        text.insert(END,RecvMessage+"\n")
        #text.insert(END,sock.recv(1024).decode() + "\n")

class Chat:
    def __init__(self):
        window = Tk()
        window.title("Chat")
        self.text = Text(window)
        self.text.pack()
        frame1 = Frame(window)
        frame1.pack()
        label = Label(frame1,text="Enter your Message: ")   # 创建标签
        self.Message = StringVar()
        entryMessage = Entry(frame1,textvariable=self.Message)
        btSend = Button(frame1, text="Send",
                           command=self.processSendButton)
        btLink = Button(window,text="Link",
                           command=self.processLinkButton)
        btLink.pack()

        label.grid(row=1,column=1)
        entryMessage.grid(row=1,column=2)
        btSend.grid(row=1,column=4)
        self.text.insert(END, "\t\t\t\t----------------\n\t\t\t\tWecolme to Chat \n\t\t\t\tEnjoy youself \n\t\t\t\t----------------\n\n\n")
        window.mainloop()

    def processSendButton(self):
        SendMessage = 'liewang说:' + self.Message.get()
        self.s.send(SendMessage.encode())
        print(self.Message.get())
        #if self.Message.get() == 'exit':
            #self.s.close()
        self.text.insert(END, "你说: "+self.Message.get()+"\n")

    def processLinkButton(self):
        self.s = socket.socket()         # 创建 socket 对象
        host = socket.gethostname() # 获取本地主机名
        port = 12345               # 设置端口好
        self.s.connect((host, port))
        self.text.insert(END, "Linked\n")
        t = threading.Thread(target=acceptMessage, args=(self.s, self.text,))
        t.start()
Chat()