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

