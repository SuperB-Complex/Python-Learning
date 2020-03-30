from operator import itemgetter

lists = [{'year':4, 'school':'a'}, {'year':4, 'school':'b'}, {'year':3, 'school':'a'}, {'year':2, 'school':'z'}]
result = sorted(lists, key=itemgetter('year', 'school'))
print(result) # [{'year': 2, 'school': 'z'}, {'year': 3, 'school': 'a'}, {'year': 4, 'school': 'a'}, {'year': 4, 'school': 'b'}]