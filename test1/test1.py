class person:
    def __init__(self, name ,age ):
        self.name=name
        self.age=age

    def say_hello(selg, to_name):
        print("안녕"+to_name+self.name)
    def introduce(self):
        print("내 이름은 "+self.name + "그리고 나는"+str(self.age)+"살이야.")

x=person("윤성",18)
x.introduce()

class police(person):
    def arrest(self,to_arrest):
        print("넌 체포됬다."+to_arrest)
y=police("겸희",1)
y.arrest("윤성")

class programmer(person):
    def creat(self,to_creat):
        print("오늘은 뭘 만들지?"+" 아, 이걸 만들어야 겠다. "+to_creat)
z=programmer("현도",123)
z.creat("파이썬")





