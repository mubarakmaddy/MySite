import re

str = """When you have imported the re module, you can start using regular expressions:
        Hello world hello world 
        The rain in 23 Spain"""

str2 = "hello world"


print(re.findall("[a-b]", str))
print(re.findall("[1-50]", str))
print(re.findall("\d", str))
print(re.findall("Sp..", str))
print(re.findall('^hello', str2))
print(re.findall('world$', str2))
print(re.findall('hel*', str))
print(re.findall('hel+', str))
x = re.findall("^hello", str)
if ():
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
