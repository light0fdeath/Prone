from django.db import models
from django.conf import settings


class College(models.Model):
    type_uni = [("Western Sydney Uni", ("Western Sydney Uni")),
                ("University of Wollonggong", ("University of Wollonggong"))]
    University = models.CharField(max_length=200, blank=True, null=False, choices=type_uni)

    type_course = [("VET-Diploma", ("VET-Diploma")), ("Bachelors", ("Bachelors")), ("Masters", ("Masters")),
                   ("PHD", ("PHD"))]
    Course_Name = models.CharField(max_length=200, blank=True, null=False, choices=type_course)

    Actual_Course_Name = models.CharField(max_length=200)

    type_location = [("New South Wales", ("New South Wales")), ("Queensland", ("Queensland")),
                     ("South Australia", ("South Australia")), ("Tasmania", ("Tasmania")), ("Victoria", ("Victoria")),
                     ("Queensland", ("Queensland")), ("Western Australia", ("Western Australia")),
                     ("Australian Capital Territory", ("Australian Capital Territory")),
                     ("Northern Territory", ("Northern Territory"))]
    Location = models.CharField(max_length=200, blank=True, null=False, choices=type_location)

    type_fees = [("< $5000 Per Year", ("< $5000 Per Year")), ("$5000-$10000 Per Year", ("$5000-$10000 Per Year")),
                 ("$10000-$20000 Per Year", ("$10000-$20000 Per Year")), ("> $20000 Per Year", ("> $20000 Per Year"))]
    Fees = models.CharField(max_length=100, blank=True, null=False, choices=type_fees)
    Actual_Fees = models.TextField(max_length=200)

    type_duration = [("0-6 Months", ("0-6 Months")), ("6 Months - 1 Year", ("6 Months - 1 Year")),
                     ("1-2 Years", ("1-2 Years")), ("> 2 Years", ("> 2 Years"))]
    Duration = models.CharField(max_length=100, blank=True, null=False, choices=type_duration)
    Actual_Duration = models.TextField(max_length=200)

    course_information = models.CharField(max_length=500)


    def __str__(self):
        return self.Actual_Course_Name