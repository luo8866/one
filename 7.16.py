import zipfile
import csv, os

class Person:
    def __init__(self, name, gender, age):  # 初始化,构造函数
        self.name = name
        self.gender = gender
        self.age = age

class Reader:
    def __init__(self):
        pass
    def ReadData(self, filepath, josephus):
        #遍历filepath 路径下的所有文件，files是该文件夹下的文件list
        for root, dirs, files in os.walk(filepath):
            #忽略filepath下的子目录
            dirs[:] = []

            for i in range(len(files)):
                if files[i][-3: ] == 'txt':
                    with open(os.path.join(filepath, files[i]), 'r', encoding='UTF-8')as f:
                        for line in f.readlines():
                            line = line.split('\n', 1)[0]
                            line = line.split(',')
                            josephus.append(Person(line[0], line[1], line[2]))

                elif files[i][-3: ] == 'csv':
                    csv_file = csv.reader(open(os.path.join(filepath, files[i]), 'r'))
                    for line in csv_file:
                        josephus.append(Person(line[0], line[1], line[2]))

                elif files[i][-3: ] == 'zip':
                    unzip_path = './people/unzip'

                    #解压
                    if not os.path.exists(unzip_path):
                        zf = zipfile.ZipFile(os.path.join(filepath, files[i]))
                        zf.extractall(path=unzip_path)
                        zf.close()

                    for root, dirs, unzip in os.walk(unzip_path):
                        dirs[:] = []
                        for k in range(len(unzip)):
                            if unzip[k][-3:] == 'txt':
                                with open(os.path.join(unzip_path, unzip[k]), 'r', encoding='UTF-8')as f:
                                    for line in f.readlines():
                                        line = line.split('\n', 1)[0]
                                        line = line.split(',')
                                        josephus.append(Person(line[0], line[1], line[2]))
                            elif unzip[k][-3:] == 'csv':
                                csv_file = csv.reader(open(os.path.join(unzip_path, unzip[k]), 'r'))
                                for line in csv_file:
                                    josephus.append(Person(line[0], line[1], line[2]))

class Josephus:
    def __init__(self, start, interval):
        self.start = start
        self.interval = interval
        self.people = []

    def append(self, Person):
        self.people.append(Person)

    def pop(self):
        self.people.pop()

    def __iter__(self):
        return self

    def __next__(self):
        new_start = self.start
        while len(self.people) > 1:
            new_start = (new_start + self.interval - 1) % len(self.people)
            self.people.pop(new_start)
        return self.people

if __name__ == '__main__':
    j = Josephus(3, 4)
    reader = Reader()
    reader.ReadData('D:\software\python\code\people', j)

    for i in range(len(j.people)):
        print(j.people[i].name)

    luckyone = next(j)

    for i in range(len(luckyone)):
        print(luckyone[i].name, luckyone[i].gender, luckyone[i].age)

   

   
