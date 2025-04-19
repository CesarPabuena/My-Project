class DataResponse():
    
    message: str = ""
    errors: dict | list = {}
    data: dict | list = {}
    status: int = 200
    
    
class MessagesPeopleServices:
    NOT_SEARCH_PEOPLE = "People not found"
    SEARCH_CORRECT_PEOPLE = "Return data peoples"
    ERROR_RETURN_PEOPLES = "Error return data peoples"