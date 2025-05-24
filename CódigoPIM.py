### PIM (Projeto Integrado Multidisciplinar)
### Universidade Paulista (UNIP)
### Projeto BitFuturo - Instituto de Tecnologia Social
### Henrique Oliveira Tavares | RA: H766CG6 | Turma: DS1S06
### Leticia Oliveira Silva | RA: H7645D3 | Turma: DS1S06
### Miguel de Oliveira | RA: H768CC6 | Turma: DS1S06
### Pedro Henrique Tavares de Oliveira | RA: R8337F9 | Turma: DS1S06
### Vinicius Mazieri e Silva | RA: H763O53 | Turma: DS1R06

### Função de cadastrar usuário | Verificação de e-mail válido ###

import re

def email_valido(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None



### Função de cadastrar usuário | Verificação de número de celular válido ###

def celular_valido(celular):
    return celular.isdigit() and len(celular) == 11



### Função de cadastrar usuário | Verificação de senha forte ###

def senha_segura(senha):
    if len(senha) < 8:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"\d", senha):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False
    return True



### Criando a funcionalidade de cadastro de usuário | Registrando informações em .json ###

import json  # Importa a biblioteca json para salvar dados dos usuários
import hashlib  # Importa a biblioteca hashlib para criptografar dados sensíveis do usuário

def cadastrar_usuario():
    print("Iniciando cadastro...")
    nome = input("Digite o nome do usuário: ")

    while True:
     cpf = input("Digite seu CPF (somente números): ")
     if cpf.isdigit() and len(cpf) == 11:
        break
     else:
        print("CPF inválido! Deve conter exatamente 11 números e nenhum caractere especial.")

    idade = input("Digite sua idade: ")

    while True:
     email = input("Digite seu e-mail: ")
     if email_valido(email):
        break
     else:
        print("E-mail inválido! Certifique-se de usar um formato como nome@dominio.com")

    while True:
     celular = input("Digite seu celular (somente números, ex: 11999999999): ")
     if celular_valido(celular):
        break
     else:
        print("Celular inválido! Digite apenas números e certifique-se de que contém 11 dígitos.")

    while True:
        senha = input("Digite a senha: ")
        if senha_segura(senha):
            break
        else:
            print("Senha fraca! A senha deve ter pelo menos 8 caracteres,\nIncluindo: Letra maiúscula, minúscula, número e símbolo especial.")



    # Criptografando a senha com SHA-256
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest() #.encode()	converte o texto para bytes | .hexdigest() retorna o hash como uma string legível criptografada
    # Criptografando o CPF com SHA-256
    cpf_criptografado = hashlib.sha256(cpf.encode()).hexdigest()

    # Tenta abrir o arquivo de usuários existente. 
    # Se não encontrar o arquivo (ex: primeira vez rodando o sistema), 
    # cria uma lista vazia para começar do zero.
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError: 
        usuarios = []

    # Verificando se ás informações passadas já são existentes no sistema
    for usuario in usuarios:
        if usuario["nome"] == nome:
            print("Esse nome de usuário já está sendo usado. Tente outro nome.")
            return
        if usuario["cpf"] == cpf:
            print("Este número de CPF já está cadastrado. Tente outro.")
            return
        if usuario["email"] == email:
            print("Este e-mail já está cadastrado. Tente outro endereço.")
            return
        if usuario["celular"] == celular:
            print("Este celular já está cadastrado. Tente outro número.")
            return

    # Adicionando o novo usuário
    novo_usuario = {
        "nome": nome,
        "cpf": cpf_criptografado,
        "idade": idade,
        "email": email,
        "celular": celular,
        "senha": senha_criptografada,
        "cursos": [],
        "certificados": [],
    }
    usuarios.append(novo_usuario)

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

    print("\n==========================================================")
    print("Usuário cadastrado na plataforma digital com sucesso!")
    print("Seja bem-vindo a BitDigital - Instituto de Tecnologia Social")
    print("==========================================================\n")



###======================================================================================###

### Criando a funcionalidade de exibir os cursos da palataforma ###

def exibir_cursos():
    print("\n===== BitFuturo | CURSOS DISPONÍVEIS =====")
    # Tenta abrir o arquivo de cursos. 
    # Se não existir (ex: primeira vez rodando o sistema), o erro é tratado no bloco 'except'.
    try:
        with open("cursos.json", "r") as arquivo:
            cursos = json.load(arquivo)
    except FileNotFoundError:
        # Cria um arquivo padrão com cursos iniciais, caso não exista
        cursos = [
            "Segurança Digital e Cidadania Online | Duração: 2 semanas",
            "Currículo Online e Mercado de Trabalho | Duração: 2 semanas",
            "Uso da Internet no Cotidiano | Duração: 3 semanas",
            "Introdução à Informática | Duração: 4 semanas",
            "Lógica de Programação | Duração: 4 semanas",
            "Fundamentos de Programação com Python | Duração: 6 semanas",
            "Desenvolvimento de Aplicações com Python | Duração: 8 semanas"
        ]
        with open("cursos.json", "w") as arquivo:
            json.dump(cursos, arquivo, indent=4)

    if not cursos:
        print("Nenhum curso foi cadastrado na plataforma ainda.")
        return

    for i, curso in enumerate(cursos, start=1):
        print(f"[{i}] {curso}")



### Criando função para o usuário conseguir se inscrever nos cursos disponíveis da plataforma ###

def inscrever_curso(usuario):
    print("\n===== INSCRIÇÃO EM CURSOS =====")

    # Carrega os cursos do arquivo
    try:
        with open("cursos.json", "r") as arquivo:
            cursos = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de cursos não encontrado.")
        return

    # Exibe os cursos com índice
    for i, curso in enumerate(cursos, start=1):
        print(f"[{i}] {curso}")

    escolha = input("Digite o número do curso para se inscrever: ")

    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(cursos):
        print("Opção inválida.")
        return

    curso_escolhido = cursos[int(escolha) - 1]

    # Verifica se o usuário já está com 2 cursos em andamento
    em_andamento = [c for c in usuario.get("cursos", []) if c["status"] == "em andamento"]
    if len(em_andamento) >= 2:
        print("Você já possui 2 cursos em andamento. Finalize um deles antes de se inscrever em outro.")
        return

    # Verifica se já está inscrito neste curso
    for c in usuario.get("cursos", []):
        if c["nome"].lower() == curso_escolhido.lower():
            print("Você já está inscrito neste curso.")
            return

    # Inscreve no novo curso
    usuario.setdefault("cursos", []).append({"nome": curso_escolhido, "status": "em andamento"})
    atualizar_usuario(usuario)
    print(f"Inscrição realizada no curso: {curso_escolhido}")



### Função para atualizar usuarios.json com novo estado do curso ###

def atualizar_usuario(usuario_atualizado):
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        return

    for i, u in enumerate(usuarios):
        if u["email"] == usuario_atualizado["email"]:
            usuarios[i] = usuario_atualizado
            break

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)



### Criando função para concluir um curso ###

def concluir_curso(usuario):
    print("\n===== CONCLUSÃO DE CURSOS =====")
    for i, c in enumerate(usuario["cursos"]):
        if c["status"] == "em andamento":
            print(f"[{i+1}] {c['nome']}")

    escolha = input("Digite o número do curso que você finalizou: ")
    try:
        indice = int(escolha) - 1
        curso_nome = usuario["cursos"][indice]["nome"]
        usuario["cursos"][indice]["status"] = "concluído"
        if curso_nome not in usuario["certificados"]:
            usuario["certificados"].append(curso_nome)
        atualizar_usuario(usuario)
        print(f"Curso '{curso_nome}' marcado como concluído e certificado gerado!")
    except:
        print("Opção inválida.")



### Criando função para exibir certificados conquistados pelo aluno ###

def exibir_certificados(usuario):
    print("\n===== CERTIFICADOS CONQUISTADOS =====")

    if not usuario["certificados"]:
        print("Você ainda não concluiu nenhum curso.")
        return

    for i, curso in enumerate(usuario["certificados"], start=1):
        print(f"[{i}] Certificado: {curso}")



### Criando função menu do aluno, que vai poder ser acessada ###
### através do menu exibido quando o usuário faz login: menu_usuario_logado(usuario) ###

def menu_aluno(usuario):
    while True:
        print(f"\n===== MENU DO ALUNO | {usuario['nome'].upper()} =====")
        print("[1] Ver meus dados")
        print("[2] Ver cursos disponíveis")
        print("[3] Inscrever-se em um curso")
        print("[4] Marcar curso como concluído")
        print("[5] Ver certificados")
        print("[6] Voltar para o menu anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n=== DADOS DO ALUNO ===")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Celular: {usuario['celular']}")

            if usuario["cursos"]:
                print("\n--- Cursos Inscritos ---")
                for i, curso in enumerate(usuario["cursos"], start=1):
                    print(f"[{i}] {curso['nome']} - Status: {curso['status']}")
            else:
                print("Você ainda não está inscrito em nenhum curso.")

        elif opcao == "2": #Função criada abaixo
            exibir_cursos()
        elif opcao == "3":
            inscrever_curso(usuario)
        elif opcao == "4":
            concluir_curso(usuario)
        elif opcao == "5":
            exibir_certificados(usuario)
        elif opcao == "6":
            print("Retornando ao menu anterior...")
            break
        else:
            print("Opção inválida. Tente novamente.")



###======================================================================================###

### Criando a funcionalidade de menu personalizado para o usuário que fizer login ###

def menu_usuario_logado(usuario):
    while True:
        print(f"\n===== BEM-VINDO(A), {usuario['nome'].upper()} =====")
        print("[1] Ver cursos disponíveis")
        print("[2] Informações sobre segurança digital")
        print("[3] Acessar menu do aluno")
        print("[4] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cursos()
        elif opcao == "2":
            exibir_informacoes_seguranca()
        elif opcao == "3":
            menu_aluno(usuario)
        elif opcao == "4":
            print("Retornando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")



### Criando a funcionalidade de login do usuário ###

def login_usuario():
    print("\n===== BitFuturo | LOGIN NA PLATAFORMA =====")
    identificador = input("Digite o seu e-mail ou CPF cadastrados: ")
    senha = input("Digite sua senha: ")

    # Criptografa a senha digitada para comparar com a senha salva
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
    # Criptografa o CPF digitado caso o usuário tenha usado CPF como forma de login
    identificador_criptografado = hashlib.sha256(identificador.encode()).hexdigest()

    # Verifica se o arquivo com o cadastro dos usuários existe
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum usuário cadastrado na plataforma ainda.")
        return

    for usuario in usuarios:
    # Verifica se o login foi feito com e-mail ou com CPF cadastrados
        if usuario["email"] == identificador or usuario["cpf"] == identificador_criptografado:
            if usuario["senha"] == senha_criptografada: 
                print(f"\nLogin bem-sucedido. \nBem-vindo(a) à plataforma digital da BitFuturo, {usuario['nome']}!")
                menu_usuario_logado(usuario)
                return
            else:
                print("A senha que você digitou está incorreta. Tente novamente.")
                return
        
    print("E-mail ou CPF digitados não foram encontrados no sistema.")



###======================================================================================###



### Criando a funcionalidade de login para área do administrador ###

def login_admin():
    print("\n===== BitFuturo | ÁREA DO ADMINISTRADOR =====")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "adminbit" and senha == "administradorinstitutobit250524":
        print("\nLogin de administrador realizado com sucesso.\nÁs funções administrativas serão exibidas:")
        menu_admin()
    else:
        print("Credenciais inválidas. Acesso administrativo negado.")



### Função adicionar curso no menu admin ###

def adicionar_curso():
    print("\n===== ADICIONAR NOVO CURSO =====")

    nome = input("Digite o nome do curso: ")
    duracao = input("Digite a duração do curso (ex: '4 semanas'): ")

    novo_curso = f"{nome} | Duração: {duracao}"

    try:
        with open("cursos.json", "r") as arquivo:
            cursos = json.load(arquivo)
    except FileNotFoundError:
        cursos = []

    # Verifica se o curso já existe
    for curso in cursos:
        if curso.lower() == novo_curso.lower():
            print("Este curso já está cadastrado.")
            return

    cursos.append(novo_curso)

    with open("cursos.json", "w") as arquivo:
        json.dump(cursos, arquivo, indent=4)

    print(f"Curso '{nome}' adicionado com sucesso!")



### Função editar curso no menu admin ###

def editar_curso():
    print("\n===== EDITAR CURSO EXISTENTE =====")

    try:
        with open("cursos.json", "r") as arquivo:
            cursos = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum curso cadastrado para editar.")
        return

    if not cursos:
        print("A lista de cursos está vazia.")
        return

    # Exibe os cursos disponíveis
    for i, curso in enumerate(cursos, start=1):
        print(f"[{i}] {curso}")

    escolha = input("Digite o número do curso que deseja editar: ")

    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(cursos):
        print("Opção inválida.")
        return

    indice = int(escolha) - 1
    curso_antigo = cursos[indice]

    print(f"Curso selecionado: {curso_antigo}")
    novo_nome = input("Digite o novo nome do curso (ou pressione Enter para manter): ").strip()
    nova_duracao = input("Digite a nova duração (ex: '4 semanas') (ou pressione Enter para manter): ").strip()

    # Extrai partes do curso antigo
    partes = curso_antigo.split(" | Duração: ")
    nome_antigo = partes[0]
    duracao_antiga = partes[1] if len(partes) > 1 else "Duração indefinida"

    nome_final = novo_nome if novo_nome else nome_antigo
    duracao_final = nova_duracao if nova_duracao else duracao_antiga

    cursos[indice] = f"{nome_final} | Duração: {duracao_final}"

    with open("cursos.json", "w") as arquivo:
        json.dump(cursos, arquivo, indent=4)

    print(f"Curso atualizado para: {cursos[indice]}")



### Função para excluir curso no menu admin ###

def excluir_curso():
    print("\n===== EXCLUSÃO DE CURSO =====")

    # Carrega os cursos existentes
    try:
        with open("cursos.json", "r") as arquivo:
            cursos = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de cursos não encontrado.")
        return

    if not cursos:
        print("Nenhum curso disponível para exclusão.")
        return

    # Exibe os cursos com índice
    for i, curso in enumerate(cursos, start=1):
        print(f"[{i}] {curso}")

    # Solicita escolha do curso a ser excluído
    escolha = input("Digite o número do curso que deseja excluir: ")

    # Validação da escolha
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(cursos):
        print("Opção inválida.")
        return

    indice = int(escolha) - 1
    curso_selecionado = cursos[indice]

    # Confirmação
    confirmacao = input(f"Tem certeza que deseja excluir o curso '{curso_selecionado}'? (s/sim): ").strip().lower()
    if confirmacao not in ["s", "sim"]:
        print("Exclusão cancelada.")
        return

    # Exclui o curso
    cursos.pop(indice)

    # Atualiza o arquivo
    with open("cursos.json", "w") as arquivo:
        json.dump(cursos, arquivo, indent=4)

    print(f"Curso '{curso_selecionado}' excluído com sucesso.")



### Função para mostrar dados dos usuários cadastrados na plataforma no menu admin ###

def ver_usuarios_cadastrados():
    print("\n===== USUÁRIOS CADASTRADOS NA PLATAFORMA =====")
    
    # Tenta abrir o arquivo de usuários
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        return

    # Verifica se há algum usuário cadastrado
    if not usuarios:
        print("Nenhum usuário foi cadastrado ainda.")
        return

    # Exibe os dados de cada usuário
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\n--- Usuário {i} ---")
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {usuario['email']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Celular: {usuario['celular']}")
        print(f"Cursos inscritos: {len(usuario.get('cursos', []))}")
        print(f"Certificados conquistados: {len(usuario.get('certificados', []))}")



### Criando função para exibir menu exclusivo dos administradores da plataforma ###

def menu_admin():
    while True:
        print("\n===== MENU DO ADMINISTRADOR | BitFuturo =====")
        print("[1] Ver cursos disponíveis")
        print("[2] Adicionar novo curso")
        print("[3] Editar curso existente")
        print("[4] Excluir curso")
        print("[5] Ver usuários cadastrados")
        print("[6] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cursos()
        elif opcao == "2":
            adicionar_curso()
            # função adicionar_curso()
        elif opcao == "3":
            editar_curso()
            # função editar_curso()
        elif opcao == "4":
            excluir_curso()
            # função excluir_curso()
        elif opcao == "5":
            ver_usuarios_cadastrados()
            # função ver_usuarios_cadastrados()
        elif opcao == "6":
            print("Retornando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")



###======================================================================================###

### Função para ler o arquivo .txt e exibir informações de segurança quando solicitadas ###

def exibir_informacoes_seguranca():
    print("\n===== BitFuturo | SEGURANÇA DIGITAL =====")

    try:
        with open("seguranca.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo de informações de segurança não encontrado.\nConsulte o administrador da plataforma.")



### Criando a função para exibir o menu inicial interativo da plataforma educacional ###

def menu():
    print("\n=================================================================================")
    print("=====| Plataforma Educacional | BitFuturo - Instituto de Tecnologia Social |=====")
    print("==================================================================================")
    print("[1] Cadastrar usuário")
    print("[2] Fazer login")
    print("[3] Ver cursos disponíveis")
    print("[4] Login como administrador")
    print("[5] Informações sobre segurança digital")
    print("[0] Sair")



# Chamando a função do menu
# Criando estrutura de repetição para manter o sistema em execução até o usuário sair
while True:
    menu()
    opcao = input("Escolha uma opção do menu: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        login_usuario()
    elif opcao == "3":
        exibir_cursos()
    elif opcao == "4":
        login_admin()
    elif opcao == "5":
        exibir_informacoes_seguranca()
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
