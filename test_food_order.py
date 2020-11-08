import unittest
from food_order import order_dog_food

class TestOrderDogFood(unittest.TestCase):

    def test_happiest_path(self):
        self.assertEqual(order_dog_food(5,3,7,17),367)
    
    def test_leftover_food_decimal(self):
        self.assertEqual(order_dog_food(5,3,7,17.5),366.5)
   
    def test_zero_dogs(self):
        self.assertEqual(order_dog_food(1,0,0,17.5),0)

    def test_small_dog_amount(self):
        self.assertEqual(order_dog_food(1,0,0,0),12)
    
    def test_medium_dog_amount(self):
        self.assertEqual(order_dog_food(0,1,0,0),24)

    def test_large_dog_amount(self):
        self.assertEqual(order_dog_food(0,0,1,0),36)
    
    def test_leftover_greater_than_order(self):
        self.assertEqual(order_dog_food(1,1,0,50),0)
    
    def test_no_leftovers(self):
        self.assertEqual(order_dog_food(7,1,1,0),144)
    
    def test_max_dogs(self):
        self.assertEqual(order_dog_food(10,10,10,25),695)
    
    #Error cases
    
    def test_negative_dogs(self):
        with self.assertRaises(Exception) as context:
            order_dog_food(-5,3,7,17)

        self.assertEqual(
            'Please enter 0 or more dogs for each size category', 
            str(context.exception)
            )
   
    def test_more_dogs_than_max(self):
        with self.assertRaises(Exception) as context:
            order_dog_food(30,30,1,17)
        
        self.assertEqual(
            'You\'ve entered 61 which is more dogs than the shelter\'s max capacity of 30. Please check your numbers and try again.',
             str(context.exception)
             )

    def test_dog_string(self):
        with self.assertRaises(Exception) as context:
            order_dog_food(1,"Fuffy",7,17)
        
        self.assertEqual(
            'Please enter whole numbers for each dog size category', 
            str(context.exception)
            )

    def test_leftover_string(self):
        with self.assertRaises(Exception) as context:
            order_dog_food(1,2,7,"seven")
        
        self.assertEqual(
            'Please enter a number for the amount of food in lbs leftover from the previous month.', 
            str(context.exception)
            )
   
    def test_dog_decimal(self):
        with self.assertRaises(Exception) as context:
            order_dog_food(5,3,7.88,17)
        
        self.assertEqual(
            'Please enter whole numbers for each dog size category', 
            str(context.exception)
            )
   
if __name__ == '__main__':
    unittest.main()
