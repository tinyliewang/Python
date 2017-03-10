name = "whole global name";

class Person:
    name = "Class name";
    def __init__(self, newPersionName):
        self.name = newPersionName;
        name = newPersionName;

    def sayYourName(self):
        # 此处由于开始正确的初始化了self对象，使得其中有了name变量，所以此处可以正确访问了name值了，可以正确的输出了：
        # My name is crifan
        print('My name is %s' % (self.name))
        print('My name is %s' % (name))
        print('My name is %s' % (Person.name))

def selfAndInitDemo():
    persionInstance = Person("crifan");
    persionInstance.sayYourName();

if __name__ == "__main__":
    selfAndInitDemo();