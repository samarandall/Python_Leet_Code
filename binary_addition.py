a = "1"
b = "11"

def addBinary(a,b):
    carry_over = "0"
    total_sum = ''
    while len(a) > 0 or len(b) > 0 or carry_over == '1':
        a_digit = '0'
        b_digit = '0'
        len_of_a = len(a)
        len_of_b = len(b) 
        if a:
            a_digit = a[len_of_a-1:len_of_a]
            a = a[0:len_of_a-1]
        if b:
            b_digit = b[len_of_b-1:len_of_b]
            b = b[0:len_of_b-1]

        if a_digit and b_digit:
            if a_digit == '1' and b_digit == '1': 
                if carry_over == '1':               # 1+1+1 =11
                    total_sum += '1'
                    carry_over ='1'

                else:                               # 1+1+0 = 10
                    total_sum += '0'
                    carry_over = '1'

            elif a_digit == '1' or b_digit == '1':  
                if carry_over == '1':               # 1+0+1 = 10
                    total_sum += '0'
                    carry_over = '1'
                else:                               # 1+0+1
                    total_sum += '1'
                    carry_over = '0'
            else:
                if carry_over == '1':
                    total_sum += '1'
                    carry_over = '0'
                else:
                    total_sum += '0'
                    carry_over = '0'

        elif a == '1' or b =='1':
            if carry_over == '1':
                total_sum += '0'
                carry_over = '1'

            else:
                total_sum += '1'
                carry_over = '0'
        
        else:
            if carry_over == '1':
                total_sum += '1'
                carry_over = '0'
            else:
                total_sum += '0'

    return total_sum[::-1]

print(addBinary(a,b))