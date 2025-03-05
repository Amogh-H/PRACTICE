#THIS EDIT IS DONE TO CHECK THE GITHUB ACTIONS

def print_pyramid(height):
    for i in range(1, height + 1):
        # Print leading spaces
        print(" " * (height - i), end="")
        # Print stars
        print("*" * (2 * i - 1))
    print("UPDATED ONE //////////////////")
    print("UPDATED ONE //////////////////")
    print("UPDATED ONE //////////////////")
    print("UPDATED ONE //////////////////")
    print("UPDATED ONE //////////////////")


        


# Example usage
height = 5  # You can change this value to adjust the size of the pyramid
print_pyramid(height)
