>>> type (3)
<class 'int'>
>>> ballots=1,341
>>> ballots
(1, 341)
>>> type(ballots)
<class 'tuple'>
>>> type (73.81)
<class 'float'>
>>> type("Hello World")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> num_candidates=3
>>> winning_percentage=73.81
>>> candidate="Diane"
>>> won_election=True
>>> counties = ["Arapahoe", "Denver, "Jefferson"]
  File "<stdin>", line 1
    counties = ["Arapahoe", "Denver, "Jefferson"]
                                      ^
SyntaxError: invalid syntax
>>> counties = ["Arapahoe", "Denver, "Jefferson"]
  File "<stdin>", line 1
    counties = ["Arapahoe", "Denver, "Jefferson"]
                                      ^
SyntaxError: invalid syntax
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties=[0]
>>> An index of a variable is its position in the array. Here are some general rules for indexing:
  File "<stdin>", line 1
    An index of a variable is its position in the array. Here are some general rules for indexing:
       ^
SyntaxError: invalid syntax
>>>
>>> Each item in a list has an index that specifies its position in the list.
  File "<stdin>", line 1
    Each item in a list has an index that specifies its position in the list.
         ^
SyntaxError: invalid syntax
>>> Indexing starts at 0. Therefore, the index of the first item is 0, the index of the second number is 1, and so on.
  File "<stdin>", line 1
    Indexing starts at 0. Therefore, the index of the first item is 0, the index of the second number is 1, and so on.
             ^
SyntaxError: invalid syntax
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties[0]
'Arapahoe'
>>> print(counties[2])
Jefferson
>>> len(counties)
3
>>> counties[0:2]
['Arapahoe', 'Denver']
>>> counties[0:1]
['Arapahoe']
>>> counties[:2]
['Arapahoe', 'Denver']
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2,"El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.remove("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop(3)
'El Paso'
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[2]="El Paso"
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties[1]="El Paso"
>>> counties
['Arapahoe', 'El Paso', 'Jefferson']
>>> counties.pop(0)
'Arapahoe'
>>> counties
['El Paso', 'Jefferson']
>>> counties.append("Denver")
>>> counties
['El Paso', 'Jefferson', 'Denver']
>>> counties.append("Arapahoe")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> counties_tuple=("Arapahoe","Denver","Jefferson")
>>> len(counties_tuple)
3
>>> counties_tuple[1]
'Denver'
>>> counties_dic={}
>>> counties_dic["Arapahoe"]=422829
>>> counties_dic
{'Arapahoe': 422829}
>>> counties_dic["Denver"]=463353
>>> counties_dic["Jefferson"]=432438
>>> counties_dic
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> len(counties_dict)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_dict' is not defined
>>> len(counties_dic)
3
>>> counties_dic.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dic.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dic.values()
dict_values([422829, 463353, 432438])
>>> counties_dic.get("Denver")
463353
>>> counties_dic.get("Arapahoe")
422829
>>> voting_data[]
  File "<stdin>", line 1
    voting_data[]
                ^
SyntaxError: invalid syntax
>>> voting_data=[]
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.append[1]({"county":"El Paso", "registered_voters": 461149})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> voting_data2=[]
>>> voting_data2.append([{'county': 'El Paso', 'registered_voters': 461149},
...
... {'county': 'Jefferson', 'registered_voters': 432438},
...
... {'county': 'Denver', 'registered_voters': 463353},
...
... {'county': 'Arapahoe', 'registered_voters': 422829}]
...
... )
>>> voting_data2
[[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]]
>>>