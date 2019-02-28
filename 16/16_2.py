'''
12. 使用组合与继承设计一个学生选择课程的程序，
使老师和学生初始化都具有课程属性，
但是属性值为空，可以动态添加，
可打印出老师教授的的课程和学生学习的课程，
可以打印出课程名字和价格，尽量避免写重复代码
（提示：学生和老师都是属于人，都有课程属性）
'''

class course:
    def __init__(self,name):
        self.name = name

    def choose(self):
        print('choose course: ', self.name)
        if self.name == 'math':
            print('price: ', 10)
        else:
            print('price: ', 20)

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name', self.name)
        print('age', self.age)

class teacher(people):
    def __init__(self,name,age,salary):
        super().__init__(name, age)
        self.salary = salary

    def info(self):
        print('teacher')
        super().display()
        print('salary', self.salary)

class student(people):
    def __init__(self ,name,age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):
        print('student')
        super().display()
        print('score', self.score)

obj_teacher = teacher('ghy',18,3000)
obj_student = student('abc',20,11)

obj_course_teacher = course('math')
obj_course_student = course('music')

obj_teacher.course = obj_course_teacher
obj_student.course = obj_course_student

obj_teacher.info()
obj_teacher.course.choose()
print('\n')
print('--------------------------------')
obj_student.info()
obj_student.course.choose()










