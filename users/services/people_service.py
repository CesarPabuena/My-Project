from querys.people_query import PeopleQuerys
from schemas.requests.people_schema import PeopleSchema
from utils.objects_model import DataResponse, MessagesPeopleServices
from http import HTTPStatus


class PeopleServices:
    
    people_schema = PeopleSchema()
    people_querys = PeopleQuerys()
    message = MessagesPeopleServices()    
    
    def service_get_peoples(self, people_id: int =None):
        data_response = DataResponse()
        
        
        try:
            if people_id:
                people = self.people_querys.get_people_by_id(people_id=people_id)
                if not people:
                    
                    data_response.status = HTTPStatus.BAD_REQUEST
                    data_response.message = self.message.NOT_SEARCH_PEOPLE
                    
                    return data_response
                
                data_response.data = dict(self.people_schema.dump(people))
                data_response.status = HTTPStatus.OK
                data_response.message = self.message.SEARCH_CORRECT_PEOPLE
                
                return data_response
            
            else:
                
                peoples = self.people_querys.get_all_peoples()
                
                data_response.data = self.people_schema.dump(peoples)
                data_response.status = HTTPStatus.OK
                data_response.message = self.message.SEARCH_CORRECT_PEOPLE
                
                return data_response
            
        except Exception as ex:
            
            data_response.message = self.message.ERROR_RETURN_PEOPLES
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            
            return data_response
    
