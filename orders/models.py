from django.db import models

# Create your models here.

class PizzaOrder(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')
    pepperoni = models.BooleanField(default=False)
    extra_cheese = models.BooleanField(default=False)
    bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # def calculate_bill(self):
    #     bill = 0
    #     if self.size == 'S':
    #         bill += 50
    #     elif self.size == 'M':
    #         bill += 100
    #     elif self.size == 'L':
    #         bill += 150

    #     if self.pepperoni:
    #         if self.size == 'S':
    #             bill += 20
    #         else:
    #             bill += 30
        
    #     if self.extra_cheese:
    #         bill += 20

    #     self.bill = bill
    #     return bill


    # # overriding the save()
    # def save(self, *args, **kwargs):
    #     self.calculate_bill()
    #     super().save(*args, **kwargs)


    # def __str__(self):
    #     return f"Pizza Order: {self.size} - ₹{self.bill}"

"""When you call save(), Django doesn't automatically run any custom logic 
that you might have for setting fields based on other fields. For example, 
in your case, the bill depends on the pizza size and whether there are extra 
toppings like pepperoni and cheese.
By overriding save(), you ensure that whenever you save a PizzaOrder object, 
the calculate_bill() function is called automatically. This ensures that the 
bill field is always updated based on the most recent changes to the size, 
pepperoni, and extra_cheese attributes."""
