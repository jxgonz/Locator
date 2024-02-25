from django.db import models
from models import User
from django.core.exceptions import ObjectDoesNotExist


class Freelancer(User):
    credentials = models.JSONField(default=list)  # Storing credentials as a JSON list
    services_offered = models.JSONField(default=list)  # Storing services offered as a JSON list
    portfolio = models.JSONField(default=list)  # Storing portfolio items as a JSON list

    # Define methods for Freelancer here
    def post_service(self, service_info):
        self.services_offered.append(service_info)
        self.save()

    def update_service(self, service_id, new_info):
        found = False
        for service in self.services_offered:
            if service['id'] == service_id:
                service.update(new_info)
                found = True
                break
        if found:
            self.save()
        else:
            raise ObjectDoesNotExist("Service %s does not exist." %service_id)

    def delete_service(self, service_id):
        self.services_offered = [service for service in self.services_offered if service['id'] != service_id]
        self.save()
