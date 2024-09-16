Nome_Do_guerreiro = input("Informe seu nome de usuário: ")
print(f"Bem-vindo(a), {Nome_Do_guerreiro}!")

while True:
    try:
        Experiencia = int(input("\nDigite sua experiência atual (ou -1 para sair): "))
        
        if Experiencia == -1:
            print("Saindo...")
            break
        
        print("\n=== Sua experiência atual é: ===")
        print(Experiencia)

        if Experiencia <= 1000:
            print("Seu rank atual é Ferro")
        elif Experiencia <= 2000:
            print("Seu rank atual é Bronze")
        elif Experiencia <= 5000:
            print("Seu rank atual é Prata")
        elif Experiencia <= 7000:
            print("Seu rank atual é Ouro")
        elif Experiencia <= 8000:
            print("Seu rank atual é Platina")
        elif Experiencia <= 9000:
            print("Seu rank atual é Ascendente")
        elif Experiencia <= 10000:
            print("Seu rank atual é Imortal")
        else:
            print("Seu rank atual é Radiante")
    
    except ValueError:
        print("Por favor, insira um número válido para a experiência.")


#Nao lembro muito de Python enato isso aqui é o masi simples possivel que consegui fazer