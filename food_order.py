max_capacity = 30  #the maximum amount of dogs the shelter can hold


def order_dog_food(small: int, medium: int, large: int,
                   leftover: float) -> float:
    if not isinstance(small, int) or not isinstance(
            medium, int) or not isinstance(large, int):
        raise Exception(
            "Please enter whole numbers for each dog size category")

    if not isinstance(leftover, (int, float)):
        raise Exception(
            "Please enter a number for the amount of food in lbs leftover from the previous month."
        )

    if small < 0 or medium < 0 or large < 0:
        raise Exception("Please enter 0 or more dogs for each size category")

    sum_dogs = small + medium + large

    if sum_dogs > max_capacity:
        raise Exception(
            f"You've entered {sum_dogs} which is more dogs than the shelter's max capacity of {max_capacity}. Please check your numbers and try again."
        )

    minimum_order = (small * 10) + (medium * 20) + (large * 30)

    #buffer order with 20% more than the minimum needed
    buffer_order = minimum_order * 1.2

    #subtract the amount of food leftover from the previous month
    total_order = buffer_order - leftover

    if total_order < 0:
        total_order = 0

    return total_order
