import input_value


def calculate_depth_increase(depths):
    previous_depth = depths[0]
    del depths[:1]
    count = 0
    for depth in depths:
        if depth > previous_depth:
            count += 1
        previous_depth = depth
    print(count)


calculate_depth_increase(input_value.input_value)
