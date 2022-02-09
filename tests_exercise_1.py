from exercise_1 import bfs_with_level

test_1 = [
    [],        #0
    [2, 3, 6], #1
    [1, 8, 9], #2
    [1, 7],    #3
    [7, 8],    #4
    [7, 8],    #5
    [1, 8, 9], #6
    [3, 5],    #7
    [2, 5, 6], #8
    [2, 6]     #9
]

test_2 = [
    [1],          #0
    [0, 4, 5, 8], #1
    [5, 9],       #2
    [8],          #3
    [1, 5, 8, 9], #4
    [1, 2, 4],    #5
    [],           #6
    [],           #7
    [1, 3, 4, 9], #8
    [2, 4, 8]     #9
]

test_3 = [
    [2, 3],       # 0
    [2, 3, 5, 6], # 1
    [0, 1],       # 2
    [0, 1, 4, 9], # 3
    [3],          # 4
    [1, 7],       # 5
    [1],          # 6
    [5, 8],       # 7
    [7, 9],       # 8
    [3, 8]        # 9
]


def test_exercise_1():
    assert(bfs_with_level(test_1) == False)
    assert(bfs_with_level(test_2) == False)
    assert(bfs_with_level(test_3) == True)


if __name__ == "__main__":
    test_exercise_1()
    print("Everything passed in exercise 1")
