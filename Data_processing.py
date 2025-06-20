# Various functions for changes in datasets and results for further work with them

def SliceData(datalist, minvalue, maxvalue):
   return datalist[next((i for i, x in enumerate(datalist[1:]) if float(x[0]) >= minvalue)) + 1:len(datalist) - next((i for i, x in enumerate(datalist[::-1]) if float(x[0]) <= maxvalue))]

def convert_to_float(dataset):
    return [[float(item) for item in sublist] for sublist in dataset]
