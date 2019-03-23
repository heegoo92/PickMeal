from django.db import models
from reviewBoard import models

# 아직 reviewBoard로 옮기지 않은 상태
class Restaurant(models.Model) :
    nations = (
        ("한식","한식"),
        ("중식","중식"),
        ("일식","일식"),
        ("양식","양식"),
    )
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=nations)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name 


