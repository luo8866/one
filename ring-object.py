import os
import zipfile
import csv
class Read:
    def get_file(self, filepath, josephus):
        with open(os.path.join(filepath, files[i]), 'r', encoding='UTF-8')as fp:
            for line in fp.readlines():
                line = line.split('\n', 1)[0]
                line = line.split(',')
                josephus.append(Person(line[0], line[1], line[2]))  

class File_txt:
    def get_file(self, filepath, josephus):  
        with open(os.path.join(filepath, files[i]), 'r', encoding='UTF-8')as fp:
            for line in fp.readlines():
                line = line.split('\n', 1)[0]
                line = line.split(',')
                josephus.append(Person(line[0], line[1], line[2]))
class File_csv:
    def get_file(self, filepath, josephus):
        with open(os.path.join(filepath, files[i]), 'r', encoding='UTF-8')as fp_csv:
            csv_file = csv.reader(fp_csv)#按行取（取出的已经是一行的内容了）
            for line in csv_file:
                josephus.append(Person(line[0], line[1], line[2]))

class File_zip:
    def get_file(self, filepath, josephus):
        unzip_path = './people/unzip'            
        #先判断解压
        if not os.path.exists(unzip_path):
            zip_file_path = os.path.join(filepath, files[i])
            with zipfile.ZipFile(zip_file_path) as zf:
                zf.extractall(path=unzip_path)

        for root, dirs, unzip in os.walk(unzip_path):
            dirs = []
            for k in range(len(unzip)):
                if unzip[k][-4:] == '.txt':
                    with open(os.path.join(unzip_path, unzip[k]), 'r', encoding='UTF-8')as fp_txt:
                        for line in fp_txt.readlines():
                            line = line.split('\n', 1)[0]
                            line = line.split(',')
                            josephus.append(Person(line[0], line[1], line[2]))

                elif unzip[k][-4: ] == '.csv':
                    with open(os.path.join(filepath, unzip[k]), 'r', encoding='UTF-8')as fp_csv:
                        csv_file = csv.reader(fp_csv)
                        for line in csv_file:
                            josephus.append(Person(line[0], line[1], line[2]))
            
class Person:
    def __init__(self, name, age, like):  # 人的信息：姓名、年龄、爱好
        self.name = name
        self.age = age
        self.like = like
        
class Josephus:
    def __init__(self, start, interval): 
        self.start = start
        self.interval = interval
        self.people = []

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.people) > 1:
            self.start = (self.start + self.interval - 1) % len(self.people)
            self.people.pop(self.start)
            remain_list = []
            #for i in range(len(self.people)):
            #    remain_list.append(self.people[i].name)
            #print(remain_list)
        return self.people

    def append(self, Person):
        self.people.append(Person)

    #def pop(self):
     #   self.people.pop()  #上面next用了pop后这里好像没起作用

test_ring = Josephus(3, 4)

for root, dirs, files in os.walk('D:\software\python\code\people'):
    dirs[:] = []
    for i in range(len(files)):
        if files[i][-4: ] == '.txt':
            read_file = File_txt()
            read_file.get_file('D:\software\python\code\people', test_ring)     
        elif files[i][-4: ] == '.csv':
            read_file = File_csv()
            read_file.get_file('D:\software\python\code\people', test_ring)     
        elif files[i][-4: ] == '.zip':
            read_file = File_zip()
            read_file.get_file('D:\software\python\code\people', test_ring)     
       
last_people = next(test_ring)
#for i in range(len(test_ring.people)):
#        print(test_ring.people[i].name)

for i in range(len(last_people)):
    print(last_people[i].name, last_people[i].age, last_people[i].like)
