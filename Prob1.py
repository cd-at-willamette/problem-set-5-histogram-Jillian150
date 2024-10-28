from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    max_val = max(data) + 1
    histogram = [0] * max_val
    for num in data:
        histogram[num] += 1
    return histogram

#1b
def print_histogram(hist:list[int]) -> None:
    for i in range(len(hist)):
        print(f"{i}: {'*' * hist[i]}")

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    
    max_val = max(hist)
    column_width = width // len(hist)
    unit_height = height // (max_val + 1)
    
    gw = GWindow(width, height)
    for i in range(len(hist)):
        column_height = hist[i] * unit_height
        my_rect(i * column_width, height - column_height, column_width, column_height, "red")

    pass

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
#print_histogram(hist) # uncomment to test
#graph_histogram(hist, 400, 400) # uncomment to test

