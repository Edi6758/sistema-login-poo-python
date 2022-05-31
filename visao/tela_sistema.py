class TelaSistema:
  def __init__(self):
    pass

  def mostrar_menu_inicial(self):
    print("============= SISTEMA =============")
    print("1 - Realizar login")
    print("2 - Cadastrar usuário")
    print("0 - Encerrar")
    opcao = int(input("Opção: "))
    return opcao