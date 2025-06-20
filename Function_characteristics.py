import numpy

# Main function of dataset analysis
def dataset_analysis(dataset):
    extremum_values = extremum_search(dataset)

    losses = extremum_values[1]
    contrast = losses - extremum_values[0]
    fsr = fsr_search(dataset)

    return  losses, contrast, fsr

# For define losses and interference contrast
# Extremum search for both directions, data must be collection of pairs
def extremum_search(data):
    first_max_reached = False
    first_min_reached = False

    i = 1

    lowest_max = 0
    highest_min = 0

    while i < len(data) - 1:
        # Determining minimum with the highest value
        if data[i][1] < data[i - 1][1] and data[i][1] < data[i + 1][1]:
            if not first_min_reached:
                highest_min = data[i][1]
            highest_min = max(data[i][1], highest_min)

        # Determining minimum with the highest value
        if data[i][1] > data[i - 1][1] and data[i][1] > data[i + 1][1]:
            if not first_max_reached:
                lowest_max = data[i][1]
            lowest_max = min(data[i][1], lowest_max)

        i += 1

    return highest_min, lowest_max


def fsr_search(data):
    fourier_result = numpy.fft.fft(data)

    return fourier_result # REDO!!! Add max amplitude search