class myclass:
    """A simple example class"""
    i=12345
    def f(self):
        return 'hello world'
if __name__=="__main__":
    myc=myclass()

print(myc.i)
print(myc.f())
