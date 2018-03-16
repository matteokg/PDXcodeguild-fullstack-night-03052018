def peaks(heights):

    peaks = []
    for i in range(1,len(heights)-1):
        left = heights[i-1]
        middle = heights[i]
        right = heights[i+1]
        if left < middle > right:
            peaks.append(i)
    return peaks
def valleys(heights):

    valleys = []
    for i in range(1, len(heights)-1):
        left = heights[i-1]
        middle = heights[i]
        right = heights[i+1]
        if left > middle and right > middle:
            valleys.append(i)
    return valleys
def peaks_and_valleys(heights):

    for i in range (1, len(heights)-1):

        peaks2 = peaks(heights)
        valleys2 = valleys(heights)

    return sorted(peaks2 + valleys2)



if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print (peaks(data))
    print (valleys(data))
    print (peaks_and_valleys(data))
