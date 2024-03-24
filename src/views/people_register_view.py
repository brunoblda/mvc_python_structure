import os
from typing import Dict

class PeopleRegisterView:
    def register_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')
        name = input('Determine o nome da pessoa: ')
        age = input('Determine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')
        
        new_person_information = {
            "name": name,
            "age": age,
            "height": height
        }

        return new_person_information 

    def register_person_sucess(self, message: Dict) -> None:
        os.system('cls||clear')

        sucess_message = f"""
            Usuário Cadastrado com Sucesso!

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                Nome: {message["attributes"]["name"]}
                Idade: {message["attributes"]["age"]}
                Altura: {message["attributes"]["height"]}
        """

        print(sucess_message)

    def registry_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f"""
            Falha ao cadastrar o usuario ! 

            Erro: {error}
        """

        print(fail_message)