Getter and Setter in Python
===============

- [@Property getter-setter](https://github.com/stupns/HOME/tree/master/Decorators)

A class can have one more variables (sometimes called properties). When you create objects each of those objects have
unique values for those variables.

Class variables need not be set directly: they can be set using class methods. This is the object orientated way and
helps you avoid mistakes.

Example
We create a class with a properties. From that class we create several objects.

```
class Friend:    
    def __init__(self):
        self.job = "None"

Alice = Friend()
Bob = Friend()
```

These objects do not have the property (job) set. To set it, we could set it directly but that’s a bad practice.
Instead, we create two methods: getJob() and setJob().

```
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
```

Two objects are created, both of them have unique values for the property job:
getter setter
