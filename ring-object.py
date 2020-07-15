class Josephus:
    def __init__(self, start, interval):
        self.start = start
        self.interval = interval
        self.people = []

    def append(self, person):
        self.people.append(person)

    def pop(self):
        self.people.pop()

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.people) > 1:
            self.start = (self.start + self.interval - 1) % len(self.people)
            self.people.pop(self.start)
           #print(self.people)
        return self.people

def information():
    fp = open('information.txt')
    people_information = fp.readlines()
    fp.close()
    people = []
    for line in people_information:
        line = list(line.strip().split(' '))
        people.append(line)
    return people
    
J1 = Josephus(2, 3)
people_information = information()
#print(people_information)
for i in range(8):
    J1.people.append(people_information[i])

last_people = next(J1)
for i in range(len(last_people)):
    print(last_people[i])


