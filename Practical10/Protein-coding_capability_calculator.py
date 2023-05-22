def calculator(seq):
    """determine whether a given DNA sequence is likely to be protein-coding or not"""
    data = seq.upper()
    start = data.find("ATG")
    stop = data.find("TGA")
    total = len(data)
    coding = stop - start
    coding_percentage = (coding/total) * 100
    if coding_percentage > 50:
        label = "protein-coding"
    elif coding_percentage < 10:
        label = "non-coding"
    else:
        label = "unclear"
    return coding_percentage, label

# give an example
DNA = "accAtGgccatgaaacgctaTgAcat"
result = calculator(DNA)
print(result)
