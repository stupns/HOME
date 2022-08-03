class Friend:
    def __init__(self):
        self.job = "None"

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job


Alice = Friend()
Bob = Friend()

Alice.setJob("Carpenter")
Bob.setJob("Builder")

print(Bob.job)
print(Alice.job)
