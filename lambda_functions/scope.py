# LEGB Rule:
# Local
# Enclosed
# Global
# Built-In

x = 10
l = lambda x: x * 2
# it will print 4 because x is 2 locally (within the print)
print(l(2))
print(x * 2)


def outer(x):
    def inner():
        print(x)
    inner()


# inner()  # cant access
outer("hello")


# def fizzbuzz():
#     while True:
#         n = input("End number?\n")
#         if n.isdigit():
#             n = int(n)
#             break
#
#     def fizzbuzz_run():
#         for i in range(1, n + 1):
#             if i % 15 == 0:
#                 print("FizzBuzz")
#             else:
#                 print(i)
#     fizzbuzz_run()
#
#
# fizzbuzz()

glob = "This is in the global scope"


def local_function():
    # print(glob.upper())
    def inner_function():
        print(__name__)
    inner_function()


local_function()
print("End")
