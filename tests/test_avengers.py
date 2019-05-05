Avengers_data = np.array([["Thor","Hulk","Spiderman","Starlord","Drax"],["lightning","green","friendly","terran","destroyer"],[0,0,0,1,2]]).T
Avengers_data
# array([['Thor', 'avengers', '0'],
#        ['Hulk', 'avengers', '0'],
#        ['Spiderman', 'avengers', '0'],
#        ['Starlord', 'guardians', '2'],
#        ['Drax', 'guardians', '2'],
#     dtype='<U9')

# Index with ints `.iloc`
Avengers_data[3,1]
'avengers'

fields = ["hero","attribute","meta"]
observations = ["a1","a2","a3","a4","a5"]

# Index with labels `.loc`
Avengers_data[3,fields.index("hero")]

# Timing
DF_data = pd.DataFrame(Avengers_data, columns=fields, index=observations)
%timeit DF_data.iloc[3,1]
%timeit Avengers_data[3,1]