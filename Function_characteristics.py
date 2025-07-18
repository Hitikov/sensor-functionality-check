import numpy as np
import scipy as sp

# Main function of dataset analysis
def dataset_analysis(dataset):
    extremum_values = extremum_search(dataset)

    # Sensor spectrum attributes
    losses = extremum_values['low_peak']
    contrast = losses - extremum_values['high_min']
    fsr = fsr_search(dataset)

    return losses, contrast, fsr, extremum_values['distorted']

# For definition of losses and interference contrast
# Extremum search for both directions, data must be collection of pairs
def extremum_search_old(data):
    first_max_reached = False
    first_min_reached = False

    i = 1

    lowest_max = 0
    highest_min = 0

    while i < len(data) - 1:
        # Determining minimum with the highest abs value
        if data[i][1] < data[i - 1][1] and data[i][1] < data[i + 1][1]:
            if not first_min_reached:
                highest_min = data[i][1]
            highest_min = min(data[i][1], highest_min)

        # Determining minimum with the lowest abs value
        if data[i][1] > data[i - 1][1] and data[i][1] > data[i + 1][1]:
            if not first_max_reached:
                lowest_max = data[i][1]
            lowest_max = max(data[i][1], lowest_max)

        i += 1

    return highest_min, lowest_max

# Extremum search for both directions
def extremum_search(dataset):
    values = np.array([item[1] for item in dataset])

    data_is_line = False

    # Value smoothing
    smoothed_values = sp.signal.savgol_filter(values, window_length=11, polyorder=3)

    # All maxima and minima indexes
    maxima, _ = sp.signal.find_peaks(smoothed_values, prominence=3, distance=10)
    minima, _ = sp.signal.find_peaks(-smoothed_values, prominence=3, distance=10)

    # Check if data have no expressed maxima or minima
    if len(maxima) == 0 or len(minima) == 0:
        data_is_line = True
        # All maxima and minima indexes with lower requirements
        maxima, _ = sp.signal.find_peaks(smoothed_values, prominence=0, distance=10)
        minima, _ = sp.signal.find_peaks(-smoothed_values, prominence=0, distance=10)

    # Values at maxima
    peak_values = values[maxima]

    # Highest value
    highest_peak_idx = maxima[np.argmax(peak_values)]
    highest_peak_val = values[highest_peak_idx]

    # Lowest value
    lowest_peak_idx = maxima[np.argmin(peak_values)]
    lowest_peak_val = values[lowest_peak_idx]

    # Values at minima
    minima_values = values[minima]

    # Highest value
    lowest_min_idx = minima[np.argmin(minima_values)]
    lowest_min_val = values[lowest_min_idx]

    # Lowest value
    highest_min_idx = minima[np.argmax(minima_values)]
    highest_min_val = values[highest_min_idx]

    return {
        'low_peak':lowest_peak_val,
        'high_peak':highest_peak_val,
        'low_min':lowest_min_val,
        'high_min':highest_min_val,
        'distorted':data_is_line
    }


# FSR search with usage of FFT
def fsr_search(dataset):
    # Division
    wavelengths = np.array([item[0] for item in dataset])
    values = np.array([item[1] for item in dataset])

    # Wave length record delta
    dw = wavelengths[1] - wavelengths[0]

    # FFTs
    fft_result = np.fft.fft(values - np.mean(values))

    # Acquire record spacing suitable for FTT
    fft_freq = np.fft.fftfreq(len(wavelengths), d=dw)

    # Amplitudes
    amplitude = np.abs(fft_result) / len(wavelengths)

    # Exclude zero frequency and negative frequencies
    positive_freq_mask = (fft_freq > 0)
    freqs = fft_freq[positive_freq_mask]
    amplitudes = amplitude[positive_freq_mask]

    # Frequency with max amplitude
    dominant_freq = freqs[np.argmax(amplitudes)]

    # FSR in wave numbers
    FSR_k = dominant_freq

    # Convert FSR_k to wavelength
    FSR_wavelength = 1 / FSR_k

    return FSR_wavelength

# Dataset validation according to requirements
def dataset_validation(set_results, loss_request, contrast_request):
    if set_results[0] < loss_request:
        return False
    if set_results[1] < contrast_request:
        return False
    return True