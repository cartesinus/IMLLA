import exercise_1

def test_introduction():
    """
    This function checks if the introduction function from exercise_1.py returns the correct
    string.
    """
    expected_output = "Introduction to Machine Learning for Linguistic Applications"
    output = exercise_1.introduction()

    if output == expected_output:
        print("Test passed!")
        return True
    else:
        print(f"Test failed! Expected '{expected_output}', but got '{output}'")
        return False

if __name__ == "__main__":
    test_introduction()
