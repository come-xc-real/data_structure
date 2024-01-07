import random


class Student1:
    def __init__(self, num, name, grade):
        self.num = num
        self.name = name
        self.grade = grade
        self.data = []

    def creat_data(self, count):
        for i in range(count):
            r = random.randint(1, 100)
            self.data.append(Student1(i + 1, f"student{i + 1}", r))

    def show_data_by_num(self, num):
        print(self.data[num - 1].num)
        print(self.data[num - 1].name)
        print(self.data[num - 1].grade)

    def show_data_average(self):
        sum = 0
        for s in self.data:
            sum += s.grade
        print(sum / len(self.data))


class Student2:
    def __init__(self, num, name, grade):
        self.num = num
        self.name = name
        self.grade = grade
        self.next = None

    def create_data(self, count):
        self.head = Student2(1, "headStudent", 100)
        next_s = Student2(2, "testStudent2", 100)
        self.head.next = next_s
        for i in range(2, count):
            r = random.randint(1, 100)
            next_s.next = Student2(i+1, f"student{i+1}", r)
            next_s = next_s.next

    def show_data_by_num(self, num):
        j = 0
        p = self.head
        while j <= num and p is not None:
            j += 1
            p = p.next
        if num >= 0 and p is not None:
            print(str(p.num), p.name, str(p.grade))

    def show_data_average(self):
        sum = 0
        p = self.head
        counts = 0
        while p is not None:
            sum += p.grade
            p = p.next
            counts += 1
        print(sum/counts)


if __name__ == '__main__':
    s1 = Student1(1, "a", 1) # 实例化对象用于使用其功能参数无意义
    s1.creat_data(10)        # 选择创建多少个数据
    s1.show_data_by_num(10)  # 使用num 搜索相应的data
    s1.show_data_average()   # 打印平均值

    s2 = Student2(1, "b", 1) # 同上
    s2.create_data(19)
    s2.show_data_by_num(13)
    s2.show_data_average()

