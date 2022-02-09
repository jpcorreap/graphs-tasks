from exercise_5 import KruskalMST


graph_test_1 = [
  [0, 1, 5],
  [2, 3, 4],
  [2, 0, 7],
  [2, 4, 5],
  [4, 0, 3],
  [1, 2, 8]
]

v_number_1 = 5

graph_test_2 = [
  [0, 1, 3],
  [0, 2, 4],
  [2, 1, 7],
  [1, 3, 2],
  [2, 3, 3],
  [3, 4, 8],
  [4, 5, 5],
  [5, 0, 4],
  [5, 1, 7],
]

v_number_2 = 6

answer_1 = KruskalMST(graph_test_1, v_number_1)
answer_2 = KruskalMST(graph_test_2, v_number_2)

def test_exercise_5():
    assert(answer_1 == [[4, 0, 3], [2, 3, 4], [0, 1, 5], [2, 4, 5]])
    assert(answer_2 == [[1, 3, 2], [0, 1, 3], [2, 3, 3], [5, 0, 4], [4,5,5]])


if __name__ == "__main__":
    test_exercise_5()
    print("Everything passed in exercise 5")
