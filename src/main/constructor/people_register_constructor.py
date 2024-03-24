from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():
    people_register_view = PeopleRegisterView()
    people_register_controller = PeopleRegisterController()

    new_person_information = people_register_view.register_person_view()
    response = people_register_controller.register(new_person_information)

    if response["sucess"]:
        people_register_view.register_person_sucess(response["message"])
    else:
        people_register_view.registry_person_fail(response["error"])

    return new_person_information