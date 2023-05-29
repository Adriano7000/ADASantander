print("--- Moisés, bem-vindo ao App Ada Poupança ---")
saldo = 1000
poupanca = 500
valor = 0
i = 0

while i != 3 :
    i = int(input("Digite 1 para APLICAR, 2 para RESGATAR e 3 para SAIR: "))
    if i == 1:
        valor = int(input("Valor da aplicação: "))
        if valor > saldo :
            print("Saldo de conta corrente insuficiente")
        else:
            saldo = saldo - valor
            poupanca = poupanca + valor
            print( "Aplicação realizada com sucesso")  
    elif(i == 2):
        valor = int(input("Valor do resgate: "))
        if valor > poupanca:
            print("Saldo de poupança insuficiente")
        else:
            saldo += valor
            poupanca += valor
            print("Resgate realizado com sucesso")
    else:
        print("Ate logo")
        
        
                
      