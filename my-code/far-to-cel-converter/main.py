def convert(s):
    f = float(s)
    # multiply the value by 5/9 to convert 180 degrees (far) into 100 (cel).
    c = (f - 32) * 5/9
    return c

far = int(input('enter temp in fahrenheit to convert to celsius: '))

print(convert(far))