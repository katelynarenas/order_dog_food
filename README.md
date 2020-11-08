# order_dog_food

order_dog_food contains a single function, order_dog_food. 

This function takes 4 arguments: the number of small, medium and large dogs in the shelter this month, and the amount of leftover food from the previous month.

It calculates the minimum food order based on the amount and size of dogs, buffers that amount by 20%, and subtracts the leftover food from the previous month.

It returns the total amount of dog food in lbs you should order for the coming month.

## Usage

This requires 3.6 or above

To run:
```bash
python3 main.py <small_dogs> <medium_dogs> <large_dogs> <leftover_food>
```
For more info:
```bash
python3 main.py -h
```

## Run tests:
```bash
python3 -m unittest
```
