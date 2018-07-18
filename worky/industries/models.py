from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        "self",
        blank = True,
        null = True,
        related_name = "children", 
        on_delete = models.CASCADE
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        path = [self.name]

        prev_category = self.parent

        while prev_category is not None:
            path.append(prev_category.name)
            prev_category = prev_category.parent
        
        return "-> ".join(path[::-1])