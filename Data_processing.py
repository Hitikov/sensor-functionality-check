# Various functions for changes in datasets and results for further work with them
import numpy

# Get list of records within specified boundaries
def SliceData(datalist, minvalue, maxvalue):
   return datalist[next((i for i, x in enumerate(datalist[1:]) if float(x[0]) >= minvalue)) + 1:len(datalist) - next((i for i, x in enumerate(datalist[::-1]) if float(x[0]) <= maxvalue))]

# Returns true if blanks detected
def convert_to_float(dataset):
    blanks_detected = False
    previous_value = 0
    converted_dataset = []

    for sublist in dataset:
        # Check if amplitude data is missing
        if len(sublist[1]) == 0:
            # Recover data from previous record to save in current
            converted_dataset.append(
                (float(sublist[0]), float(previous_value))
            )
            blanks_detected = True
        else:
            converted_dataset.append(
                (float(sublist[0]), float(sublist[1]))
            )

        # Saving current amplitude value as backup for next record
        previous_value = sublist[1]

    return converted_dataset, blanks_detected

# Watts to decibels convertion
def convert_W_to_dB(dataset):
    for item in dataset:
        item[1] = -10 * numpy.log10(abs(item[1]))
    return dataset
