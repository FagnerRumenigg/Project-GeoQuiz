class USA:
    def __init__(self):
        estates = {
                'Question 1': {
                    'question': 'Which one is the Alabama capital ?',
                    'right_answer': 'Montgomery',
                },
                'Question 2': {
                    'question': 'Which one is the Alasca capital ?',
                    'right_answer': 'Juneau',
                },
                'Question 3': {
                    'question': 'Which one is the Arizona capital ?',
                    'right_answer': 'Phoenix',
                },
                'Question 4': {
                    'question': 'Which one is the Arkansas capital  ?',
                    'right_answer': 'Little Rock',
                },
                'Question 5': {
                    'question': 'Which one is the Califórnia capital ?',
                    'right_answer': 'Sacramento',
                },
                'Question 6': {
                    'question': 'Which one is the North Carolina capital ?',
                    'right_answer': 'Raleigh',
                },
                'Question 7': {
                    'question': 'Which one is the South Carolina capital ?',
                    'right_answer': 'Columbia',
                },
                'Question 8': {
                    'question': 'Which one is the Colorado capital ? ',
                    'right_answer': 'Denver',
                },
                'Question 9': {
                    'question': 'Which one is the Connecticut capital ?',
                    'right_answer': 'Hartford',
                },
                'Question 10': {
                    'question': 'Which one is the North Dakota capital ? ',
                    'right_answer': 'Bismarck',
                },
                'Question 11': {
                    'question': 'Which one is the South Dakota capital ?',
                    'right_answer': 'Pierre',
                },
                'Question 12': {
                    'question': 'Which one is the Delaware capital  ?',
                    'right_answer': 'Dover',
                },
                'Question 13': {
                    'question': 'Qual a capital de Minas Gerais ?',
                    'right_answer': 'Belo Horizonte',
                },
                'Question 14': {
                    'question': 'Qual a capital do Pará ?',
                    'right_answer': 'Belem',
                },
                'Question 15': {
                    'question': 'Qual a capital da Paraíba ?',
                    'right_answer': 'João Pessoa',
                },
                'Question 16': {
                    'question': 'Qual a capital do Paraná ?',
                    'right_answer': 'Curitiba',
                },
                'Question 17': {
                    'question': 'Qual a capital do Pernambuco ?',
                    'right_answer': 'Recife',
                },
                'Question 18': {
                    'question': 'Qual a capital do Piauí ?',
                    'right_answer': 'Teresina',
                },
                'Question 19': {
                    'question': 'Qual a capital do Rio de Janeiro ?',
                    'right_answer': 'Rio de Janeiro',
                },
                'Question 20': {
                    'question': 'Qual a capital do Rio Grande do Norte ?',
                    'right_answer': 'Natal',
                },
                'Question 21': {
                    'question': 'Qual a capital do Rio Grande do Sul ?',
                    'right_answer': 'Porto Alegre',
                },
                'Question 22': {
                    'question': 'Qual a capital de Rondônia ?',
                    'right_answer': 'Porto Velho',
                },
                'Question 23': {
                    'question': 'Qual a capital de Roraima ?',
                    'right_answer': 'Boa Vista',
                },
                'Question 24': {
                    'question': 'Qual a capital de Santa Catarina ?',
                    'right_answer': 'Florianópolis',
                },
                'Question 25': {
                    'question': 'Qual a capital de São Paulo ?',
                    'right_answer': 'São Paulo',
                },
                'Question 26': {
                    'question': 'Qual a capital do Sergipe ?',
                    'right_answer': 'Aracaju',
                },
                'Question 27': {
                    'question': 'Qual a capital do Tocantins ?',
                    'right_answer': 'Palmas',
                },
            }
        print()

        result = 0
        for qk, qv in estates.items():
            print(f'{qk}: {qv["question"]}')

            print('Answer correctly ')

            user_answer = input('Your answer: ')

            if user_answer.lower() == 'sair':
                print("You did'nt finished your test.")
                break

            if user_answer.lower() == qv['right_answer'].lower():
                print("Good One")
                result += 1
            else:
                print("Better lucky next time")
                result += 0

        print()
        print(f'Yoy got {result} right questions')
        print()
