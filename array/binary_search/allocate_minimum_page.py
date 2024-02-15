"""
Allocate minimum page
Minimize the max number of pages read by a student.
Student can read book in continues order only.
To allocate things in continues fashion we can use binary search

"""

from typing import List

def min_pages(books_pages: List[int], students: int) -> int:

    min_pages_to_read_by_one_student = max(books_pages)
    max_pages_to_be_read_by_one_student = sum(books_pages)
    res = 0
    # Using binary search, discarding one half, time complexity here is O(nlogn)
    while (min_pages_to_read_by_one_student <= max_pages_to_be_read_by_one_student):
        mid = (min_pages_to_read_by_one_student + max_pages_to_be_read_by_one_student)//2
        if is_feasible(books_pages, students, mid):
            res = mid
            max_pages_to_be_read_by_one_student = mid-1
        else:
            min_pages_to_read_by_one_student = mid + 1

    return res

def is_feasible(books_pages: List[int], students: int, mid: int) -> bool:
    # "Calculate the number of students required to read and return false 
    # if required more than available number of students(means combination isn't correct)"

    res = 0
    student_count = 1
    for pages in books_pages:
        if (res + pages) <= mid:
            res+=pages
        else:
            student_count+=1
            res = pages
    return student_count <= students
    

if __name__ == "__main__":
    # print(min_pages([10, 20, 5, 15, 5], 2))
    assert min_pages([10, 20, 5, 15, 5], 2) == 30
    assert min_pages([10, 5, 20], 2) == 20
    assert min_pages([10, 10, 20, 30], 2) == 40
    assert min_pages([10, 20, 5, 15, 5], 3) == 25
    assert min_pages([10, 20, 5, 15, 5, 30, 35], 4) == 35

