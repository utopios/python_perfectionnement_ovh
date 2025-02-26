import ctypes

lib = ctypes.cdll.LoadLibrary('demo.so')
# pour windows
# lib = ctypes.windll.LoadLibrary('demo.dll')
print(lib.add_int(10,20))

var1 = ctypes.c_float(10.0)
var2 = ctypes.c_float(20.0)
lib.add_float.argtypes = [ctypes.c_float, ctypes.c_float]
lib.add_float.restype = ctypes.c_float
result = lib.add_float(var1, var2)

a = ctypes.c_float(10)
b = ctypes.c_float(20)
c = ctypes.c_float()

a_pointer = ctypes.pointer(a)
b_pointer = ctypes.pointer(b)
c_pointer = ctypes.pointer(c)
lib.add_float_ref(a_pointer, b_pointer, c_pointer)

list1 = [1,4,5,6]
list2 = [5,6,8,9]
tab1 = ((ctypes.c_int * len(list1))*list1)
tab2 = (ctypes.c_int * len(list2))(*list2)
result = (ctypes.c_int * len(list2))(0,0,0,0)
lib.add_two_array(tab1, tab2, result, len(list1))
list = [result[i] for i in range(len(list1))]
print(list)