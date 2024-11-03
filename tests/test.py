from myPackage import myModule

def test_topn():
    """Testing the function
    """
    
    assert myModule.top([9,8,6,10,1], 3) == [9,8,6], "Incorrect"
    assert myModule.top([6,10,1,4,6], 3) == [10,6,1], "Incorrect"
    assert myModule.top([9,8,6,10,1], 4) == [10,9,8,6], "Incorrect"