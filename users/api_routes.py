from views.people_views import PeopleAPI



def register_routes(app):

    people_view = PeopleAPI.as_view("people_api")
    app.add_url_rule("/api/peoples", defaults={"poeple_id": None}, view_func=people_view, methods=["GET"])
    app.add_url_rule("/api/peoples/<int:people_id>", view_func=people_view, methods=["GET"])