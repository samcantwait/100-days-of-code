import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])
df = pandas.DataFrame(
    {
        'Fur Color': ['gray', 'red', 'black'], 
        'Count': [grey, red, black]
    })
csv = df.to_csv('squirrel_file.csv')

    