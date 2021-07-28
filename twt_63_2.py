def frequency(text):
    return min(text.count(c)for c in {*text})


for _ in range(int(input())):
    text, freq = input().split()
    freq = int(freq)
    frequencies = [0]
    for start in range(len(text)):
        for end in range(start, len(text)):
            if frequency(text[start:end + 1]) >= freq:
                frequencies += [end - start + 1]
    print(max(frequencies))
