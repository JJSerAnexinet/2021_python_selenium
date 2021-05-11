def test_one():
    """Test case demo 1 """
    print("First test case")
    a = 5
    b = 3

assert a == b, 'A should be equal to b'

def test_two():
    """Test case demo 2"""
    print("Second test case")



"""Test Case fallado solo con exception """
def test_tres():
    """Test case demo 3 """
    print("Third test case")
    raise Exception ('Fail')


"""pytest --junitxml=report.xml Module_05/test_hello_world.py"""