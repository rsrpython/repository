produtos=[]
quantidadesvendidas=[]
valoresdosprodutos=[]
valoresdosprodutoscomimpostos=[]
valoresdosprodutostotal=[]
lucros=[]
produtoscompras=[]
quantidadescompradas=[]
totaisdascompras=[]
valortotaldacompra=0
valordoprodutocomimposto=0
frete=0
imp1=12
imp2=6
imp3=3
valor1=0
valor2=0
valor3=0
while True:
    menu=float(input(
        "Escolha uma opção do menu abaixo:\n"
        "1 - Inserir produto no estoque\n"
        "2 - Atualizar o estoque de produtos\n"
        "3 - Imprimir os produtos no estoque\n"
        "4 - Excluir produto do estoque\n"
        "5 - Inserir produto na compra\n"
        "6 - Excluir produto da compra\n"
        "7 - Atualizar produto da compra\n"
        "8 - Fechar a compra\n"
        "9 - Sair\n"
    ))
    if menu==1:
        produto=input("Digite o nome do produto: ")
        valordoproduto=float(input("Digite o valor do produto: R$"))
        lucro=float(input("Digite a margem de lucro: "))
        produtos.append(produto)
        valoresdosprodutos.append(round(float(valordoproduto),2))
        lucros.append(round(float(lucro),2))
        valor1=round(float((valordoproduto*imp1)/100),2)
        valor2=round(float((valordoproduto*imp2)/100),2)
        valor3=round(float((valordoproduto*imp3)/100),2)
        valordoprodutocomimposto=round(float(valordoproduto+valor1+valor2+valor3),2)
        valoresdosprodutoscomimpostos.append(round(float(valordoprodutocomimposto),2))
        calclucro=round(float((valordoproduto*lucro)/100))
        valordoprodutototal=round(float(valordoprodutocomimposto+calclucro),2)
        valoresdosprodutostotal.append(round(float(valordoprodutototal),2))
        print(f"O preço do produto com impostos: R$",round(float(valordoprodutocomimposto),2))
        print(f"O preço do produto com impostos e mais a margem de lucro é: R$",round(float(valordoprodutototal),2))
        
    elif menu==2:
        produto_a_ser_atualizado=input("Digite o nome do produto a ser atualizado: ")
        if produto_a_ser_atualizado in produtos:
            indice=produtos.index(produto_a_ser_atualizado)
            novo_valor_produto=float(input("Digite o novo valor do produto: "))
            nova_margem_lucro=float(input("Digite a nova margem de lucro do produto: "))
            valoresdosprodutos[indice]=novo_valor_produto
            lucros[indice]=nova_margem_lucro
            novo_valor1_com_impostos=round(float((novo_valor_produto*imp1)/100),2)
            novo_valor2_com_impostos=round(float((novo_valor_produto*imp2)/100),2)
            novo_valor3_com_impostos=round(float((novo_valor_produto*imp3)/100),2)
            novo_valor_produto_com_impostos=round(float(novo_valor_produto+novo_valor1_com_impostos+novo_valor2_com_impostos+novo_valor3_com_impostos),2)
            valoresdosprodutoscomimpostos[indice]=novo_valor_produto_com_impostos
            novo_valor_produto_lucro=round(float((novo_valor_produto_com_impostos*nova_margem_lucro)/100),2)
            novo_valor_produto_total=round(float(novo_valor_produto_com_impostos+novo_valor_produto_lucro),2)
            valoresdosprodutostotal[indice]=round(float(novo_valor_produto_total),2)
            print(f"novo valor do produto: R$", round(float(valoresdosprodutos[indice])),2)
            print(f"nova margem de lucro do produto: ", round(float(lucros[indice]),2))
            print(f"novo preço do produto com impostos: R$", round(float(valoresdosprodutoscomimpostos[indice]),2))
            print(f"novo preço do produto com impostos e margem de lucro: R$", round(float(valoresdosprodutostotal[indice]),2))
            print("Dados atualizados com sucesso!")
        else:
            print("Produto não encontrado!")     
    elif menu==3:
        print("Listagem de produtos:")
        for i in range(len(produtos)):
            print(f"{produtos[i]}: R${valoresdosprodutostotal[i]}")
    elif menu==4:
        produto_a_ser_deletado=input("Digite o nome do produto a ser deletado: ")
        if produto_a_ser_deletado in produtos:
            indice=produtos.index[produto_a_ser_deletado]
            del produtos[indice]
            del lucros[indice]
            del valoresdosprodutoscomimpostos[indice]
            del valoresdosprodutostotal[indice]
            for i in range(len(produtos)):
                print(f"{produtos[i]}: R${valoresdosprodutostotal[i]}")
            print("Produto foi excluido com sucesso!")     
        else:
            print("Produto não encontrado!")    
    elif menu==5:
        produto_a_ser_comprado=input("Digite o nome do produto a ser comprado: ")
        if produto_a_ser_comprado in produtos:
            quantidade_a_ser_comprada=input(float("Digite a quantidade a ser comprada: "))
            produtoscompras.append(produto_a_ser_comprado)
            quantidadescompradas.append(quantidade_a_ser_comprada)
            indice=produtos.index(produto_a_ser_comprado)
            valor_da_compra=round(float(valoresdosprodutostotal[indice]*quantidade_a_ser_comprada),2)
            totaisdascompras.append(valor_da_compra)
            print(f"Total desse produto: R$", round(float(valor_da_compra),2))
        else:
            print("Produto não encontrado!")    
    elif menu==6:
        produto_a_ser_excluido=input("Digite o produto da compra a ser excluido: ")
        if produto_a_ser_excluido in produtoscompras:
            indice=produtoscompras.index(produto_a_ser_excluido) 
            del produtoscompras[indice]
            del quantidadescompradas[indice]
            del totaisdascompras[indice]
            for i in range(len(produtoscompras)):
                print(f"{produtoscompras[i]}: R${totaisdascompras[i]}")
            print("Produto foi excluido com sucesso!")
        else:
            print("Produto não encontrado!")    
    elif menu==7:
        produto_da_compra_a_ser_atualizado=input("Digite o produto da compra a ser atualizado: ")
        if produto_da_compra_a_ser_atualizado in produtoscompras:
            indice=produtoscompras.index(produto_da_compra_a_ser_atualizado)
            quantidadescompradas[indice]=input(float("Digite a quantidade desejada: "))
            valor_da_compra=round(float(valoresdosprodutostotal[indice]*quantidadescompradas[indice]),2)
            totaisdascompras[indice]=valor_da_compra
            print(f"{produtoscompras[indice]}: {totaisdascompras[indice]}")
            print("Produto da compra foi atualizado com sucesso!")

        else:
            print("Produto não existe na compra!")    
    elif menu==8:
        
        total_da_compra=round(float(0),2)
        for i in range(len(produtoscompras)):
            total_da_compra+=round(float(totaisdascompras[i]),2)
            print(f"{produtoscompras[i]} qtd: {round(float(quantidadescompradas[i]),2)} vl.total: {round(float(totaisdascompras[i]),2)}")
        print(f"Total da compra sem frete: R$", round(float(total_da_compra),2))    
        valor_do_frete=float(input("Digite o valor do frete: R$:"))
        print(f"Valor total da compra com o frete: R$", round(float(total_da_compra+valor_do_frete),2))
    elif menu==9:
        print("Bye, Bye... Volte sempre!")
        break        
    else:
        print("Opçâo inválida! Tente de novo.")