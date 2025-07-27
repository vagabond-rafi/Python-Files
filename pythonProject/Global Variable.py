g =10
def func():
    global g
    g = 90
    print("Function called")

print("The value of g before calling fun(): ",g)

print("The after of g before calling fun(): ",g)
func()
