import pandas
# f= open("guru99.txt","w+")
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print (Dict['Tiffany'])
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print((Dict['Tiffany']))

result = pandas.read_csv('Image/Emissions.csv')
print(result)

oldstring = 'i am not good'
newstring = oldstring.replace('good', 'bad')
print(newstring)
print(':'.join('python'))
string = '12345'
print(reverse(string))
>>> df['year'] = pd.DatetimeIndex(df['birth_date']).year
>>> df.head()