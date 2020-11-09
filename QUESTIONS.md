# Questions

## Should the leftover food amount be subtracted before or after adding 20% to the minimum order?
I assumed, despite the example math that shows otherwise, that the leftover food amount should be subtracted after adding 20% to the minimum order. I did this to ensure that the shelter always has 20% more than the minimum needed for the month. 

## How will this function be used?
I added main.py for an easy way to call this function manually, and I did do some input validation, but I assumed that this function would be part of a library. I added type hints and a doc string to help developers calling the function.

## What if more dogs are added mid month?
We have accounted for dogs being adopted mid month, as we just take the leftover food amount in to consideration when ordering next month, but what if more dogs come in to the shelter mid month? Should we have another function, or maybe another argument for this function, that takes in to account the number of days remaining in the month and helps us make a mid month food order?

## What if some dogs have dietary restrictions?
What if not all dogs can eat the same type of food? Should we add more arguments to account for dogs in each size category that need a grain free diet, prescription diet, etc?