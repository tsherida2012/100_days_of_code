def find_median(number_list):
    # Sort the list
    sorted_list = sorted(number_list)

    # Find the middle index
    n = len(sorted_list)
    middle = n // 2

    # Calculate the median
    if n % 2 == 0:  # Check if the number of elements is even
        # Average the two middle numbers
        median = (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        # Else its odd
        median = sorted_list[middle]

    return median


if __name__ == "__main__":
    # Examples
    even_list = [3, 5, 1, 4]
    odd_list = [3, 5, 1, 4, 2]

    median_even = find_median(even_list)
    median_odd = find_median(odd_list)
    print(f'Median even list {median_even}, median odd list {median_odd}')
