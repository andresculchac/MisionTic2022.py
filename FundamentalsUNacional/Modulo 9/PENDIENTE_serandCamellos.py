input_key=int(input())
for xy in range(input_key):
  c=input().split("_")
  magic_un=""
  for serp in c:
    magic_un+=serp.capitalize()
  print(magic_un)