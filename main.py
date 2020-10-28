import re

srcfile = open("source.txt", "r")
resfile = open("result.txt", "w")

text = srcfile.read()

srcfile.close()

num1 = r"\b[7-8]\d{10}"
num2 = r"\b9\d{9}"

results = re.findall(num1, text) + re.findall(num2, text)


for elem in results:
    resfile.writelines(elem + '\n')

resfile.close()