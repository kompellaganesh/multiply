def mularrays(m1, m2):
    # function that will return 2d arrays where each array is product of m1 and 1 number in m2
    if len(m1) == 0 or len(m2) == 0:
        return [0]
    n1 = len(m1)
    n2 = len(m2)
    arrays = []
    for i in range(n2-1, -1, -1):
        # carry value for adding
        carry = 0
        # array of fixed maximum size which of len(m1)+len(m2) will be populated later
        array = [0 for i in range(n1+n2)]
        mul1 = m2[i]
        for j in range(n1-1, -1, -1):
            mul2 = m1[j]
            sum = (mul1*mul2)+carry
            val = (sum % 10)
            carry = int(sum/10)
            array[i+j+1] = val
        if carry != 0:
            array[i] = carry
        arrays.append(array)
    return arrays


def addarrays(arrays):
    # function that will take 2d arrays of same length and return sum as array
    rows = len(arrays)
    cols = len(arrays[0])
    array = []
    carry = 0
    for i in range(cols-1, -1, -1):
        sum = 0
        for j in range(rows):
            sum += arrays[j][i]
        sum += carry
        val = sum % 10
        carry = int(sum/10)
        array.append(val)
    if carry != 0:
        array.append(carry)
    # reverse the array
    array = array[::-1]
    return array


def multiply(m1, m2):
    isneg = False
    # identifying if the final output is positive or negative
    if (m1[0] == '-' and m2[0] != '-') or (m1[0] == '-' and m2[0] != '-'):
        isneg = True
    # remove + , - characters from arrays
    if m1[0] == '-' or m1[0] == '+':
        m1 = m1[1:]
    if m2[0] == '-' or m2[0] == '+':
        m2 = m2[1:]
    # get different arrays when 1 number of m2 multiplys with the m1 
    arrays = mularrays(m1, m2)
    # add all the arrays from the above step
    arr = addarrays(arrays)
    # remove first contiguous zeros from array
    i = 0
    while(i < len(arr)):

        if arr[i] == 0:
            i += 1
        else:
            break
    arr = arr[i:]
    # add negative symbol to output
    if isneg:
        a = ['-']
        a.extend(arr)
        return a
    return arr


if __name__ == "__main__":
    m1 = [4,4,4,4,4,4]
    m2 = [6,6,6,6,6,6]
    output=multiply(m1, m2)
    print(output)
    m1 = ['-',9,9,9]
    m2 = [9,9,9,9]
    output=multiply(m1, m2)
    print(output)
    m1 = ['-',8,7,9]
    m2 = ['-',9,8]
    output=multiply(m1, m2)
    print(output)
