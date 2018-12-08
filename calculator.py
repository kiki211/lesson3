def calculator(string):
    try:
        string = string.lower().replace(' ', '')
        parts = string.split('+')
        for plus in range(len(parts)):
            if "-" in parts[plus]:
                parts[plus] = parts[plus].split("-")
        print(parts)
        for plus in range(len(parts)):
            parts[plus] = precalculator(parts[plus])
        print(parts)
        result= sum(parts)
    except ValueError:
        return "Enter digits please!"
    except ZeroDivisionError:
        return "Can't delete on 0, try again."
    return result

def precalculator(part):
    if type(part) is str:
        if '*' in part:
            result =1
            for subpart in part.split('*'):
                result *= precalculator(subpart)
            return result
        elif '/' in part:
            parts = list(map(precalculator, part.split('/')))
            result = parts[0]
            for subpart in parts[1:]:
                result /= subpart
            return result
        else:
            return float(part)

    elif type(part) is list:
        for i in range(len(part)):
            part[i] = precalculator(part[i])
        return part[0] - sum(part[1:])

    return part





    print(parts)

if __name__=="__main__":
    print(calculator('23+ 10 + 2*3*2 -4 + 3/2'))
    # print(calculator('3-1 + 3/0'))
    #print(precalculator([10,'6/2',4]))
    #print(precalculator('3*2*3.9'))
    #print(precalculator('10/2/1.5'))
