marks={
    'harry':34,
    'sai':34,
    'shyam':44
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get('sai'))
# marks.update({"mahish":40,"ranuka":70,"harry":100})
#  print(marks)
print(marks.pop("sai"))
print(marks)
print(marks.get("harry2"))#prints none
print(marks["harry2"])#returns an error