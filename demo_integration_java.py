import jpype

# Start Java virtual machine

jvmPath = jpype.getDefaultJVMPath()

jpype.startJVM(jvmPath)

# Specify Java classpath and import class

classpath = "path/to/MyClass.class"

jpype.addClassPath(classpath)

MyClass = jpype.JClass("MyClass")

# Invoke Java function and print output

myVar = MyClass.myMethod()

print(myVar)

# Shutdown JVM

jpype.shutdownJVM()