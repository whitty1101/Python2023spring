#動態方法
class Lesson:
    def __init__(self,teacher,time):
        self.teacher=teacher
        self.time=time
    @classmethod
    def math(cls):
        return cls('Emma','Monday')
    @classmethod
    def english(cls):
        return cls('Peter','Thursday')
    def intro(self):
        print('This lesson is taught by {} on {}.'.format(self.teacher, self.time))
Emma=Lesson.math()
Peter=Lesson.english()
Emma.intro()
Peter.intro()