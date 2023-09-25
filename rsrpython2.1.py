produtos=["arroz","feijão","macarrão","óleo de soja","litro de leite","pão integral","pasta de amendoim","aveia","1kl de bananas","1/2kl de café","1l de yogourt"]
custos=[4.50,3.75,4.10,5.20,5.60,7.20,6.80,9.10,4.10,6.30,9.20]
quantidades=[5,2,4,2,6,3,2,2,3,3,4]
imp1=12
imp2=6
imp3=3
frete=50.00
for i in range(len(produtos)):
    produto=produtos[i]
    custo=custos[i]
    quantidade=quantidades[i]
    lucro=60
    custoimp1=((custo*imp1)/100)
    custoimp2=((custo*imp2)/100)
    custoimp3=((custo*imp3)/100)
    precocusto=(custo+custoimp1+custoimp2+custoimp3)
    margemdelucro=((precocusto*lucro)/100)
    precovenda=(precocusto+margemdelucro)
    vendaproduto=(precovenda*quantidade)
    precovendacomfrete=(quantidade/frete)
    print(f"produto: ", produto, "custo s/ imposto: ", round(custo,2), "custo c/ imposto: ", round(precocusto,2), "preço de venda: ", round(precovenda,2), "quantidade: ", round(quantidade), "total da venda: ", round(vendaproduto,2), "preço de venda com frete: ", round(precovendacomfrete,2))