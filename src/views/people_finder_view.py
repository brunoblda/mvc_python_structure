import os
from typing import Dict

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        name = input('Determine o nome da pessoa para busca: ')
        
        person_finder_information = {
            "name": name
        }

        return person_finder_information

    def find_person_sucess(self, message:  Dict) -> None:
        os.system('cls||clear')

        sucess_message = f"""
            Usiario encontrado com sucesso!
        
            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                name: {message["infos"]["name"]}
                age: {message["infos"]["age"]}
                height: {message["infos"]["height"]}
            """

        print(sucess_message)

    def find_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f"""
            Falha ao encontrar o usuario!
            
            Erro: {error} 
        """

        print(fail_message)