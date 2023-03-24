def merge_two_halves(a, b):
    x = y = 0
    merge_and_sorted = []
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            merge_and_sorted.append(a[x])
            x += 1
        else:
            merge_and_sorted.append(b[y])
            y += 1
    return merge_and_sorted



def get_merge_sorted_list(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    mid_point = int((len(unsorted_list))//2)

    first_half = unsorted_list[:mid_point]
    #:mid_point ":" means from the beginning to the midpoint
    second_half = unsorted_list[mid_point:]
    #midpoint: means     from midpoint to when elements ends

    half_a = get_merge_sorted_list(first_half)
    half_b = get_merge_sorted_list(second_half)
    
    return merge_two_halves(half_a, half_b)
    
if __name__ == "__main__":
    pass#get_merge_sorted_list(5)