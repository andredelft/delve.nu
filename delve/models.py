from django.db import models


class PortfolioItem(models.Model):
    title = models.CharField(50)
    name = models.CharField(50)
    href = models.CharField(50)
    index = models.IntegerField(default=0)


class PortfolioImage(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/')
