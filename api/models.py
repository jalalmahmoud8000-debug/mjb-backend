from django.db import models

class WatchType(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "نوع الساعة"
        verbose_name_plural = "انواع الساعات"

    def __str__(self):
        return self.name


class Watch(models.Model):
    type = models.ForeignKey(WatchType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class WatchImage(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='watch_images/')

    def __str__(self):
        return f"صورة ل {self.watch.name}"