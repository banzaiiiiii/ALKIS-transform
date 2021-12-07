from subprocess import *


def jarWrapper(filename, arg1, arg2, arg3, arg4):
    process = Popen(['java', '-jar', filename, arg1, arg2, arg3, arg4], stdout=PIPE, stderr=PIPE)
    result = process.communicate()
    print(result[0].decode('utf-8'))



# mappingFilePath : "Input/example-json-mapping.ttl"
# output path         "/Output"