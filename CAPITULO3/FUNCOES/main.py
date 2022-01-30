from functions.IdentificacaoDeFuncoes import*
inventario = []

print("PREENCHENDO")
preencherInventario(inventario)

print("EXIBINDO")
exibirInventario(inventario)

print("PESQUISANDO")
localizarPorNome(inventario)

print("ALTERANDO")
depreciarPorNome(inventario,90)

print("EXCLUINDO")
excluirPorSerial(inventario)

print("EXIBINDO")
exibirInventario(inventario)

print("RESUMINDO")
resumirValores(inventario)
