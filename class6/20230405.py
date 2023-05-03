#
# class Person:
#    
#     def __init__(self,name,age,fav):
#         self.name=name
#         self.age=age
#         self.fav=fav
#     def Intro(self):
#         print('I am '+str(self.name)+'I am '+str(self.age)+'I love '+str(self.fav))
#     def shout(self,content):
#         print('shout'+content)
    
# #建立物件
# Amy=Person('Amy','15','apple')
# #呼叫行為
# Amy.shout('I hate you')



# #實體方法
# #人類類別
# class Person:
#     state='healthy'
#     #建立METHOD 
#     def getCold(self):
#         self.__class__.state='Sick'
# print('Origin: ',Person.state)
# person=Person()
# person.getCold
# print('after: ', Person.state)



# # 動態方法
# class Person:
#     def __init__(self,eye,hair):
#         self.eye=eye
#         self.hair=hair
#     @classmethod
#     def American(cls):
#         return cls('blue','brown')
#     @classmethod
#     def Taiwanese(cls):
#         return cls('black','black')
#     def intro(self):
#         print('My eye is {} and my hair is {}.'.format(self.eye, self.hair))

# amy=Person.American()
# ben=Person.Taiwanese()
# amy.intro()
# ben.intro()



# #靜態方法
# class Person:
#     @staticmethod
#     def workRate(time):
#         print('workinghour'+str(time))
# work=Person()
# work.workRate(8)





