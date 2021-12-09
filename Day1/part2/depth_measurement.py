import input_value


def calculate_depth_increase(depths):
    previous_total = 0
    count = -1
    for i in range(len(depths)):
        try:
            first_depth = depths[i]
            second_depth = depths[i+1]
            third_depth = depths[i+2]
            total = first_depth + second_depth + third_depth
            if total > previous_total:
                count += 1
            previous_total = total
        except:
            break
    print(count)


calculate_depth_increase(input_value.input_value)
