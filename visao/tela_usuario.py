class TelaUsuario:
  def __init__(self):
    pass
  def mostra_tela_login(self):
    print("============= LOGIN =============")
    nome = input("nome: ")
    senha = input("senha: ")

    return {"nome": nome, "senha": senha}

  def mostra_mensagem(self, mensagem: str):
    print(mensagem)

  def mostra_tela_opcoes(self):
    print("============= CADASTRAR USUÁRIOS =============")
    print("1 - incluir usuário")
    print("2 - alterar usuário")
    print("3 - excluir usuário")
    print("4 - listar usuário")
    print("0 - Retornar")
    opcao = int(input("opção: "))
    return opcao
    
    