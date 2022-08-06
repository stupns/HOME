class Phone:
    username = "Kate"                # public variable
    __serial_number = "11.22.33"     # private variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print("Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1
        print("Times was turned on: ", self.__how_many_times_turned_on )


my_phone = Phone()

# my_phone.__turn_on()
# my_phone._Phone__turn_on()
print(f"Correct serial number is {my_phone._Phone__serial_number}")
# my_phone._Phone__serial_number = "33.22.11"
# print(f"New serial number is {my_phone._Phone__serial_number}")
# # input(f"Press Enter to exit")

