def top_border(rows=2, width=41, pattern="#"):
    for i in range(rows):
        print(pattern * width)

def bottom_border(rows=2, width=41, pattern="#"):
    for i in range(rows):
        print(pattern * width)

def circle_pattern(*args):
    if len(args) == 4:
        left_hash, dot_count, middle_hash, right_hash = args
        print("#" * left_hash + "." * dot_count + "#" * middle_hash + "." * dot_count + "#" * right_hash)
    elif len(args) == 5:
        left_hash, left_dots, middle_hash, right_dots, right_hash = args
        print("#" * left_hash + "." * left_dots + "#" * middle_hash + "." * right_dots + "#" * right_hash)

patterns = [
    (14,6,0,15),
    (12,8,0,13),
    (10,10,1,10,10),
    (9,6,11,6,9),
    (8,5,15,5,8),
    (7,4,19,4,7),
    (6,4,21,4,6),
    (5,4,23,4,5),
    (4,4,25,4,4),
    (4,3,27,3,4),
    (3,4,27,4,3),
    (3,3,29,3,3),
    (2,4,29,4,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,2,33,2,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,3,31,3,2),
    (2,4,29,4,2),
    (3,3,29,3,3),
    (3,4,27,4,3),
    (4,3,27,3,4),
    (4,4,25,4,4),
    (5,4,23,4,5),
    (6,4,21,4,6),
    (7,4,19,4,7),
    (8,5,15,5,8),
    (9,6,11,6,9),
    (10,10,1,10,10),
    (12,8,0,13),
    (14,6,0,15),

]

top_border()
for pattern in patterns:
    circle_pattern(*pattern)
bottom_border()