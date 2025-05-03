
def calculate_sum(start, end):
    """
    Calculate the sum of integers from start to end (inclusive).
    
    Args:
        start (int): The starting number
        end (int): The ending number
        
    Returns:
        int: The sum of all integers from start to end
    """
    return (end - start + 1) * (start + end) // 2
    

def main():
    """Calculate and display the sum from 1 to 100."""
    result = calculate_sum(1, 100)
    print(f"The sum of integers from 1 to 100 is: {result}")
    
    assert result == 5050, f"Expected 5050, but got {result}"
    
if __name__ == "__main__":
    main()
