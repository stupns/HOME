class Static:
    @staticmethod
    def play():
        print("*playing music*")


Static.play()


class InsideStatic:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")


InsideStatic.play()
# InsideStatic.stop()


class CallStatic:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")


CallStatic.play()

obj = CallStatic()
obj.stop()
