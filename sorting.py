#Sorting

my_list = [3, 5, 7, 2, 4, 1]

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
# https://stackoverflow.com/questions/895371/bubble-sort-homework
# this is much easier for me to understand than the code in lecture

    length = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i], lst[i+1] = lst[i+1], lst[i]


    return lst

        


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    #using bonnie's additions to lecture notes
    result_list = []
   
    while len(list1) > 0 or len(list2) > 0:
        # if items left in both lists
        # compare first items of each list
        if list1 == []:
            result_list.extend(list2)
            break
        elif list2 == []:
            result_list.extend(list1)
            break
        elif list1[0] < list2[0]:
            # append and remove first item of lst1
            result_list.append(list1.pop(0))
        else:
            # append and remove first item of lst2
            result_list.append(list2.pop(0))

 
    return result_list


##########ADVANCED##########
    def merge_sort(lst):
        """
        Given a list, returns a sorted version of that list.

        Finish the merge sort algorithm by writing another function that takes in a
        single unsorted list of integers and uses recursion and the 'merge_lists'
        function you already wrote to return a new sorted list containing all
        integers from the input list. In other words, the new function should sort
        a list using merge_lists and recursion.

        >>> merge_sort([6, 2, 3, 9, 0, 1])
        [0, 1, 2, 3, 6, 9]
        """

        print "calling merge_sort on", lst

        # this is the base case 
        if len(lst) < 2:  # if length of lst is 1 or zero, return the lst
            print "returning", lst
            return lst

        mid = int(len(lst) / 2)  # index at half the list
        list1 = merge_sort(lst[:mid])  # divide list in half
        list2 = merge_sort(lst[mid:])  # assign other half

        return merge_lists(list1, list2)
   

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
