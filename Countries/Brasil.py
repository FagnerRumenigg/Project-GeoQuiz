class Brasil:
    def __init__(self):
        estates = {
            'Question 1': {
                'question': 'Qual a capital do Acre ?',
                'right_answer': 'Rio Branco',
            },
            'Question 2': {
                'question': 'Qual a capital de Alagoas ?',
                'right_answer': 'Maceió',
            },
            'Question 3': {
                'question': 'Qual a capital de Amapá ?',
                'right_answer': 'Macapá',
            },
            'Question 4': {
                'question': 'Qual a capital do Amazonas ?',
                'right_answer': 'Manaus',
            },
            'Question 5': {
                'question': 'Qual a capital da Bahia ?',
                'right_answer': 'Salvador',
            },
            'Question 6': {
                'question': 'Qual a capital do Ceará ?',
                'right_answer': 'Fortaleza',
            },
            'Question 7': {
                'question': 'Qual a capital do Distrito Federal ?',
                'right_answer': 'Brasília',
            },
            'Question 8': {
                'question': 'Qual a capital do Espirito Santo',
                'right_answer': 'Vitória',
            },
            'Question 9': {
                'question': 'Qual a capital do Goiás ?',
                'right_answer': 'Goiânia',
            },
            'Question 10': {
                'question': 'Qual a capital do Maranhão ?',
                'right_answer': 'São Luís',
            },
            'Question 11': {
                'question': 'Qual a capital do Mato Grosso ?',
                'right_answer': 'Cuiabá',
            },
            'Question 12': {
                'question': 'Qual a capital do Mato Grosso do Sul ?',
                'right_answer': 'Campo Grande',
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

            print('Responda corretamente: ')

            user_answer = input('Sua resposta: ')

            if user_answer.lower() == 'sair':
                print("Você não terminou seu teste.")
                break

            if user_answer.lower() == qv['right_answer'].lower():
                print("Correto.")
                result += 1
                print('')
            else:
                print("Mais sorte na proxima.")
                result += 0
                print('')

        qtd_perguntas = len(estates)

        print("")
        print(f'Você acertou {result} de {qtd_perguntas}')
        print("")
