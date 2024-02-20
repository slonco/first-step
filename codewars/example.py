# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!

def better_than_average(class_points, your_points):
    return True if (sum(class_points) + your_points)/(len(class_points)+1) < your_points else False

# best way
# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)