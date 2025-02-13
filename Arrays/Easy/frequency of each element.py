def countFreq():
    frequency={}
    for i in arr:
        if i in frequency:
            frequency[i] = frequency[i]+1
        else:
            frequency[i]=1
    return frequency



if __name__ == "__main__":
    arr = [10,5,10,15,10,5]
    n = len(arr)
    print(countFreq())
