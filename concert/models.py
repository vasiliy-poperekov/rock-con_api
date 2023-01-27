from django.db import models


class Concert(models.Model):
    group = models.ForeignKey("users.GroupSinger", related_name="concert_group_singer", on_delete=models.CASCADE)
    place = models.ForeignKey("users.Place", related_name="concert_place", on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        db_table = "concert"
        verbose_name = "Концерт"
        verbose_name_plural = "Концерты"

    def __str__(self):
        return self.group.name + " - " + self.place.name
