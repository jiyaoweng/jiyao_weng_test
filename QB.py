# Python 3.6

# comparison of two versoin numbers in string
# Invoke: versionNumCompare(VersionNumInString, VersinNumInString)
# Return: return True if first version is greater than second,
#         otherwise, return False
def versionNumCompare(verStr1, verStr2):
    verFloat1 = float(verStr1)
    verFloat2 = float(verStr2)

    return verFloat1 > verFloat2


print(versionNumCompare("1.2", "1.1"))
print(versionNumCompare("1.2", "2.1"))
