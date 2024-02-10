import unittest

def more_than_seven_letters(names: list[str], max_character_count: int = 7) -> int:
    """
    Counts the number of names with more than 'max_character_count' characters.

    Args:
    - names: List of names to evaluate.
    - max_character_count: Maximum character count threshold.

    Returns:
    - Number of names exceeding the specified maximum character count.
    """
    count_above_threshold = 0
    for name in names:
        if len(name) > max_character_count:
            count_above_threshold += 1
            print(f"Name exceeds {max_character_count} characters: {name}")
        else:
            print(f"Name is less than or equal to {max_character_count} characters: {name}")
    return count_above_threshold


class TestNamesMethod(unittest.TestCase):
    def test_names_with_length_above_threshold(self):
        # List of names to test
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        
        # Call the function with the list of names and a new maximum character count threshold
        count_above_threshold = more_than_seven_letters(names=names_list, max_character_count=8)  # Change the value of max_character_count as needed
        
        # Expected value for the number of names exceeding the threshold
        expected_count = 4

        # Verify that the obtained result matches the expected value
        self.assertEqual(count_above_threshold, expected_count)

if __name__ == '__main__':
    unittest.main()
