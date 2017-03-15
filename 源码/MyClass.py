class myclass:
    
    @staticmethod
    def staticmethod1():
        print("static method!")

    @classmethod
    def classmethod1(cls):
        print("class method！",cls)


myclass.staticmethod1()
myclass.classmethod1()
