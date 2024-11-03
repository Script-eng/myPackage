def top(items, n):
    """Returns the top n elements of an array provided as an array which is items

    Args:
        items (list): array provided
        n (individual items): _description_
        
    Return:
        def top([1,2, 3], 2)
        returns 1 and 2    
    """
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
   
    top = items[-n:]   
    
    return top[::-1]         
            