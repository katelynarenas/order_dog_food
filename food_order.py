MAX_CAPACITY = 30  #the maximum amount of dogs the shelter can hold
SMALL_DOG_MULTIPLIER = 10 #the amount of food to order per small dog
MEDIUM_DOG_MULTIPLIER = 20 #the amount of food to order per medium dog
LARGE_DOG_MULTIPLIER = 30 #the amount of food to order per large dog


def order_dog_food(small_dogs: int, medium_dogs: int, large_dogs: int, leftover_food: float) -> float:
    """ Calculates the amount of food to order for the month given the number of dogs in each size category,
        the leftover food from the previous month in lbs, and a 20% buffer
        Returns the total_order in lbs
    """
    if not isinstance(small_dogs, int) or not isinstance(medium_dogs, int) or not isinstance(large_dogs, int):
        raise Exception(
            "Please enter whole numbers for each dog size category")

    if not isinstance(leftover_food, (int, float)):
        raise Exception(
            "Please enter a number for the amount of food in lbs leftover from the previous month."
        )

    if small_dogs < 0 or medium_dogs < 0 or large_dogs < 0:
        raise Exception("Please enter 0 or more dogs for each size category")

    sum_dogs = small_dogs + medium_dogs + large_dogs

    if sum_dogs > MAX_CAPACITY:
        raise Exception(
            f"You've entered {sum_dogs} which is more dogs than the shelter's max capacity of {MAX_CAPACITY}. Please check your numbers and try again."
        )

    minimum_order = (small_dogs * SMALL_DOG_MULTIPLIER) + (medium_dogs * MEDIUM_DOG_MULTIPLIER) + (large_dogs * LARGE_DOG_MULTIPLIER)

    #buffer order with 20% more than the minimum needed
    buffer_order = minimum_order * 1.2

    #subtract the amount of food leftover from the previous month
    total_order = buffer_order - leftover_food

    if total_order < 0:
        total_order = 0

    return total_order
