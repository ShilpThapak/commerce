from django.contrib.auth.models import AbstractUser
from django.db import models


class categories(models.Model):
    category = models.CharField(max_length=64)
    #categorylistings= *look at activelistings model*
    def __str__(self):
        return f"{self.category}"

class User(AbstractUser):
    pass
    #savedlistings = models.ManyToManyField(activelistings, blank=True, related_name="userswhosaved")
    #createdlistings = *look at activelistings*
    #userbid = *look at bids model*
    def __str__(self):
        return f"{self.username}"

class activelistings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    startingBid = models.IntegerField()
    imageurl = models.URLField(blank=True, null=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, blank=True, null=True, related_name="categorylistings")
    status = models.CharField(max_length=10, default="active", blank=True, null=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="createdlistings")
    #listingcomments = *look at comments model*
    #listingbid = *look at bids model*
    userswhosaved = models.ManyToManyField(User, blank=True, related_name="savedlistings")
    def __str__(self):
        return f"{self.title}"

class bids(models.Model):
    bidprice = models.IntegerField()
    biddinguser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userbid")
    listing = models.ForeignKey(activelistings, on_delete=models.CASCADE, related_name="listingbid")
    def __str__(self):
        return f"{self.id}: {self.bidprice} for {self.listing} by {self.biddinguser}"

class comments(models.Model):
    comment = models.CharField(max_length=140)
    listing = models.ForeignKey(activelistings, on_delete=models.CASCADE, related_name="lisingcomments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id}: {self.comment} on {self.listing}"