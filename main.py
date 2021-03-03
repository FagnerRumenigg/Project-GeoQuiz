from Countries import Brasil
from Countries import USA
menu = ''
answer = 's'

print("Seja bem-vindo ao quiz de estados e capitais mundiais, escolha qual país você quer tentar")
print("Brasil")
print("USA")
print("Digite da maneira escrita acima")
print("")

while answer != "n":

    menu = input("Digite o nome correto do País (Por favor, incluir os acentos): ")
    if menu.lower() == "Brasil".lower():
        brasil = Brasil.Brasil()
    elif menu.lower() == "USA".lower():
        usa = USA.USA()
    else:
        print("Nenhum foi escolhido")

    answer = input('do you wanna do again ? ? y/n: ')

    print("")
    print("Obrigado por participar")
