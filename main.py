#!/usr/bin/python

import argparse
import food_order

parser = argparse.ArgumentParser()
parser.add_argument("small_dogs", type=int, help="The number of small dogs in the shelter")
parser.add_argument("medium_dogs", type=int, help="The number of medium dogs in the shelter")
parser.add_argument("large_dogs", type=int, help="The number of large dogs in the shelter")
parser.add_argument("leftover_food", type=float, help="The amount of food leftover from the previous month in lbs")
args = parser.parse_args()

total_order = food_order.order_dog_food(args.small_dogs, args.medium_dogs, args.large_dogs, args.leftover_food)
print(f"Please order {total_order} lbs of food for this month.")
