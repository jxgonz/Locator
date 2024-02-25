from django.db import models


class List(models.Model):
    listing_id = models.AutoField(primary_key=True)  # AutoField is usually a better choice for an ID
    freelancer = models.ForeignKey('Freelancer', on_delete=models.CASCADE, related_name='listings')
    description = models.TextField()
    price_rate = models.IntegerField()
    availability = models.BooleanField(default=True)
    rating_reviews = models.JSONField(default=list)
    bookings = models.JSONField(default=list)  # Storing bookings as a JSON list

    def update_availability(self, available):
        self.availability = available
        self.save()

    def add_review(self, review):
        self.rating_reviews.append(review)
        self.save()

    def view_bookings(self):
        return self.bookings
