from flask.views import MethodView
from services.people_service import PeopleServices
from utils.http_response import http_response
from flask import request

class PeopleAPI(MethodView):
    
    services = PeopleServices()
    
    
    def get(self, people_id=None): 
        service = self.services.service_get_peoples(people_id=people_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)