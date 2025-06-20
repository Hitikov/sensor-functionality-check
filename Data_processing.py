# Various functions for changes in datasets and results for further work with them
import numpy

def SliceData(datalist, minvalue, maxvalue):
   return datalist[next((i for i, x in enumerate(datalist[1:]) if float(x[0]) >= minvalue)) + 1:len(datalist) - next((i for i, x in enumerate(datalist[::-1]) if float(x[0]) <= maxvalue))]

def convert_to_float(dataset):
    return [[float(item) for item in sublist] for sublist in dataset]

def convert_W_to_dB(dataset):
    for item in dataset:
        item[1] = -10 * numpy.log10(abs(item[1]))
    return dataset

def record_assembly(number, losses, contrast, fsr, spectrum, condition):
    return [number, losses, contrast, fsr, spectrum, condition]
