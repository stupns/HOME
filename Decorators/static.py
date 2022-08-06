class Static:
    @staticmethod
    def play():
        print("*playing music*")


# Example 2
class InsideStatic:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")


# Example 3
class CallStatic:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")


if __name__ == "__main__":
    Static.play()
    print('\nExample 2:')

    InsideStatic.play()
    # InsideStatic.stop()
    print('\nExample 3:')

    CallStatic.play()
    CallStatic().stop()
