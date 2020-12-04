from subprocess import call

class  CallPy(object):

    def _init_ (self,path ='/Users/lauranicolebermudezsanta/Documents/Proyecto/Game 2 players.py'):
        self.path = path

    def call_python_file(self):
        call(["ifconfig"])

if __name__ == "__main__":
    c = CallPy()
    c.call_phyton_file()
