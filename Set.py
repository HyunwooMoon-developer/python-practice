#Can not be duplicated / No order

my_set = {1,2,3,3,3}
print(my_set)

javaScript = {'I', 'HE' , 'SHE'}
python = set(['THEY', 'I'])

# 교집합(Intersection) available javascript and python
print(javaScript & python)
print(javaScript.intersection(python))

# 합집합(Union) available javascript or python
print(javaScript | python)
print(javaScript.union(python))

# 차집합(Difference) only available javascript
print(javaScript - python)
print(javaScript.difference(python))

# increase python

python.add('HE')
print(python)

# decrease javascript

javaScript.remove('HE')
print(javaScript)