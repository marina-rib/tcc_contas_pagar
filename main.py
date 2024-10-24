from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, Button, Frame, GROOVE
import mysql.connector

janela = Tk()
janela.title("Menu")
janela.configure(background='#006633')
janela.geometry("1000x500")
janela.resizable(True, True)
janela.maxsize(width=800, height=700)
janela.minsize(width=500, height=300)

margem = 0.05
relwidth = 1 - 2 * margem
relheight = 1 - 2 * margem
relx = margem
rely = margem

frame_1 = Frame(janela, bd=4, bg='#FFFFFF', highlightbackground='#006633', highlightthickness=3)
frame_1.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

def menu():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_contas_pagas.destroy()
        bt_fornecedor.destroy()
        bt_pagamento.destroy()
        bt_banco.destroy()
        bt_status_contas.destroy()

    def tela_contas():
        destruir_campos()
        contas_pagas1()

    def fornecedores_():
        destruir_campos()
        fornecedores()

    def pagamentos_():
        destruir_campos()
        pagamentos()

    def bancos_():
        destruir_campos()
        bancos()

    def status_contas_():
        destruir_campos()
        status_contas()

    label_bem_vindo = Label(frame_1, text="Bem-vindo", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_contas_pagas = Button(frame_1, command=tela_contas, text='Cadastrar Contas', bg='SlateGray4', fg='white',
                             font=("verdana", 12, "bold"))
    bt_contas_pagas.place(relx=0.12, rely=0.4, relwidth=0.25, relheight=0.15)

    bt_fornecedor = Button(frame_1, command=fornecedores_, text='Fornecedor', bg='SlateGray4', fg='white',
                           font=("verdana", 12, "bold"))
    bt_fornecedor.place(relx=0.12, rely=0.65, relwidth=0.25, relheight=0.15)

    bt_pagamento = Button(frame_1, command=pagamentos_, text='Pagamento', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_pagamento.place(relx=0.65, rely=0.4, relwidth=0.25, relheight=0.15)

    bt_banco = Button(frame_1, command=bancos_, text='Bancos', bg='SlateGray4', fg='white',
                      font=("verdana", 12, "bold"))
    bt_banco.place(relx=0.65, rely=0.65, relwidth=0.25, relheight=0.15)

    bt_status_contas = Button(frame_1, command=status_contas_, text='Status Contas', bg='SlateGray4', fg='white',
                              font=("verdana", 12, "bold"))
    bt_status_contas.place(relx=0.389, rely=0.65, relwidth=0.25, relheight=0.15)


def contas_pagas1():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Quality"
    )

    def destruir_campos():
        label_bem_vindo.destroy()
        bt_banco.destroy()
        bt_menu.destroy()
        lb_num_conta.destroy()
        num_conta_entry.destroy()
        lb_num_doc.destroy()
        num_doc_entry.destroy()
        lb_valor.destroy()
        valor_entry.destroy()
        lb_cnpj.destroy()
        cnpj_entry.destroy()
        lb_vencimento.destroy()
        vencimento_entry.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def cadastrar():
        num_conta1 = num_conta_entry.get()
        CNPJ_contas1 = cnpj_entry.get()
        num_documento1 = num_doc_entry.get()
        vencimento = vencimento_entry.get()
        valor = valor_entry.get()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO contas_pagar (num_conta, CNPJ_contas, num_documento, vencimento,valor) VALUES (%s, %s, %s, %s, %s)",
                (num_conta1, CNPJ_contas1, num_documento1, vencimento, valor))
            conexao.commit()
            messagebox.showinfo("Mensagem", "Dados inceridos com sucesso.")

        except mysql.connector.Error as erro:
            print("Erro ao inserir os dados:", erro)
            messagebox.showinfo("Mensagem", "Erro ao inserir os dados.")

    label_bem_vindo = Label(frame_1, text="Cadastrar Contas", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_banco = Button(frame_1, command=cadastrar, text='Cadastrar', bg='SlateGray4', fg='white',
                      font=("verdana", 12, "bold"))
    bt_banco.place(relx=0.65, rely=0.65, relwidth=0.25, relheight=0.15)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.85, relwidth=0.25, relheight=0.15)

    lb_num_conta = Label(frame_1, text="Número da conta", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_num_conta.place(relx=0.05, rely=0.35)
    num_conta_entry = Entry(frame_1, font=("Arial", 14))
    num_conta_entry.place(relx=0.05, rely=0.4, relwidth=0.28)

    lb_num_doc = Label(frame_1, text="Número do documento", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_num_doc.place(relx=0.35, rely=0.35)
    num_doc_entry = Entry(frame_1, font=("Arial", 14))
    num_doc_entry.place(relx=0.35, rely=0.4, relwidth=0.28)

    lb_valor = Label(frame_1, text="Valor", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_valor.place(relx=0.65, rely=0.35)
    valor_entry = Entry(frame_1, font=("Arial", 14))
    valor_entry.place(relx=0.65, rely=0.4, relwidth=0.28)

    lb_cnpj = Label(frame_1, text="CNPJ", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_cnpj.place(relx=0.05, rely=0.55)
    cnpj_entry = Entry(frame_1, font=("Arial", 14))
    cnpj_entry.place(relx=0.05, rely=0.6, relwidth=0.28)

    lb_vencimento = Label(frame_1, text="Vencimento", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_vencimento.place(relx=0.35, rely=0.55)
    vencimento_entry = Entry(frame_1, font=("Arial", 14))
    vencimento_entry.place(relx=0.35, rely=0.6, relwidth=0.28)


def fornecedores_crud():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Quality"
    )

    def destruir_campos():
        tel_r_entry.destroy()
        lb_tel_r.destroy()
        tel_entry.destroy()
        lb_tel.destroy()
        estado_entry.destroy()
        lb_estado.destroy()
        cidade_entry.destroy()
        lb_cidade.destroy()
        bairro_entry.destroy()
        lb_bairro.destroy()
        endereco_entry.destroy()
        lb_endreco.destroy()
        cep_entry.destroy()
        lb_cep.destroy()
        raz_soc_entry.destroy()
        lb_raz_soc.destroy()
        cnpj_entry.destroy()
        lb_cnpj.destroy()
        bt_menu.destroy()
        bt_buscar.destroy()
        bt_excluir.destroy()
        bt_alterar.destroy()
        bt_cadastrar.destroy()
        label_bem_vindo.destroy()

    def menu_():
        destruir_campos()
        menu()

    def limpar_tela():
        tel_r_entry.delete(0, END)
        tel_entry.delete(0, END)
        estado_entry.delete(0, END)
        cidade_entry.delete(0, END)
        bairro_entry.delete(0, END)
        endereco_entry.delete(0, END)
        cep_entry.delete(0, END)
        raz_soc_entry.delete(0, END)
        cnpj_entry.delete(0, END)

    def alterar_for():
        cnpj_ = cnpj_entry.get()
        raz_ = raz_soc_entry.get()
        cep_ = cep_entry.get()
        endereco_ = endereco_entry.get()
        bairro_ = bairro_entry.get()
        cidade_ = cidade_entry.get()
        estado_ = estado_entry.get()
        tel_ = tel_entry.get()
        tel_r_ = tel_r_entry.get()

        try:
            cursor = conexao.cursor()
            query = """
            UPDATE fornecedor
            SET Razaosocial = %s, CEP = %s, endereco = %s, bairro = %s, cidade = %s, estado = %s, telefone = %s, Telefonereserva = %s
            WHERE CNPJ = %s
            """
            cursor.execute(query, (raz_, cep_, endereco_, bairro_, cidade_, estado_, tel_, tel_r_, cnpj_))
            conexao.commit()
            messagebox.showinfo("Mensagem", "Alteração realizada.")

        except mysql.connector.Error as e:
            print("Erro ao atualizar o fornecedor:", e)
            messagebox.showinfo("Mensagem", "Alteração não realizada.")

        finally:
            limpar_tela()
            tel_r_entry.config(state='disabled')
            tel_entry.config(state='disabled')
            estado_entry.config(state='disabled')
            cidade_entry.config(state='disabled')
            bairro_entry.config(state='disabled')
            endereco_entry.config(state='disabled')
            cep_entry.config(state='disabled')
            raz_soc_entry.config(state='disabled')
            cnpj_entry.config(state='normal')
            bt_excluir.config(state='disabled')
            bt_alterar.config(state='disabled')
            bt_cadastrar.config(state='disabled')

    def cadastrar_for():
        cnpj_ = cnpj_entry.get()
        raz_ = raz_soc_entry.get()
        cep_ = cep_entry.get()
        endereco_ = endereco_entry.get()
        bairro_ = bairro_entry.get()
        cidade_ = cidade_entry.get()
        estado_ = estado_entry.get()
        tel_ = tel_entry.get()
        tel_r_ = tel_r_entry.get()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO fornecedor (CNPJ, Razaosocial, CEP, endereco, bairro,cidade,estado,telefone,Telefonereserva) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (cnpj_, raz_, cep_, endereco_, bairro_, cidade_, estado_, tel_, tel_r_))
            conexao.commit()
            messagebox.showinfo("Mensagem", "Dados inseridos.")
        except mysql.connector.Error as erro:
            print("Erro ao inserir os dados:", erro)
            messagebox.showinfo("Mensagem", "Erro ao inserir os dados.")
        finally:
            limpar_tela()
            tel_r_entry.config(state='disabled')
            tel_entry.config(state='disabled')
            estado_entry.config(state='disabled')
            cidade_entry.config(state='disabled')
            bairro_entry.config(state='disabled')
            endereco_entry.config(state='disabled')
            cep_entry.config(state='disabled')
            raz_soc_entry.config(state='disabled')
            cnpj_entry.config(state='normal')
            bt_excluir.config(state='disabled')
            bt_alterar.config(state='disabled')
            bt_cadastrar.config(state='disabled')

    def excluir_for():
        try:
            cursor = conexao.cursor()
            texto_digitado = cnpj_entry.get()
            sql = "DELETE FROM fornecedor WHERE CNPJ = %s"
            cursor.execute(sql, (texto_digitado,))
            conexao.commit()
            texto_digitado = cnpj_entry.get()
            cursor.execute("SELECT COUNT(*) FROM fornecedor WHERE CNPJ = %s", (texto_digitado,))
            count = cursor.fetchone()[0]
            if count == 0:
                messagebox.showinfo("Mensagem", "Exclusão realizada.")
            else:
                messagebox.showinfo("Mensagem", "Exclusão não realizada.")
        except mysql.connector.Error as erro:
            print("Erro ao deletar o dado:", erro)
            messagebox.showinfo("ERRO", "exclusão não realizada. chave estrangeira")
        finally:
            limpar_tela()
            tel_r_entry.config(state='disabled')
            tel_entry.config(state='disabled')
            estado_entry.config(state='disabled')
            cidade_entry.config(state='disabled')
            bairro_entry.config(state='disabled')
            endereco_entry.config(state='disabled')
            cep_entry.config(state='disabled')
            raz_soc_entry.config(state='disabled')
            cnpj_entry.config(state='normal')
            bt_excluir.config(state='disabled')
            bt_alterar.config(state='disabled')
            bt_cadastrar.config(state='disabled')

    def buscar_for():
        try:
            cursor = conexao.cursor()
            texto_digitado = cnpj_entry.get()
            cursor.execute("SELECT COUNT(*) FROM fornecedor WHERE CNPJ = %s", (texto_digitado,))
            count = cursor.fetchone()[0]
            if count > 0:
                consulta_sql = "SELECT * FROM fornecedor WHERE CNPJ = %s"
                cursor.execute(consulta_sql, (texto_digitado,))
                resultados = cursor.fetchall()
                for linha in resultados:
                    tel_r_entry.config(state='normal')
                    tel_entry.config(state='normal')
                    estado_entry.config(state='normal')
                    cidade_entry.config(state='normal')
                    bairro_entry.config(state='normal')
                    endereco_entry.config(state='normal')
                    cep_entry.config(state='normal')
                    raz_soc_entry.config(state='normal')
                    raz_soc_entry.delete(0, END)
                    cep_entry.delete(0, END)
                    endereco_entry.delete(0, END)
                    bairro_entry.delete(0, END)
                    cidade_entry.delete(0, END)
                    estado_entry.delete(0, END)
                    tel_entry.delete(0, END)
                    tel_r_entry.delete(0, END)
                    raz_soc_entry.insert(0, linha[1])
                    cep_entry.insert(0, linha[2])
                    endereco_entry.insert(0, linha[3])
                    bairro_entry.insert(0, linha[4])
                    cidade_entry.insert(0, linha[5])
                    estado_entry.insert(0, linha[6])
                    tel_entry.insert(0, linha[7])
                    tel_r_entry.insert(0, linha[8])
                    bt_excluir.config(state='normal')
                    bt_alterar.config(state='normal')

                    cnpj_entry.config(state='disabled')
            else:
                cnpj_entry.config(state='disabled')
                bt_cadastrar.config(state='normal')
                tel_r_entry.config(state='normal')
                tel_entry.config(state='normal')
                estado_entry.config(state='normal')
                cidade_entry.config(state='normal')
                bairro_entry.config(state='normal')
                endereco_entry.config(state='normal')
                cep_entry.config(state='normal')
                raz_soc_entry.config(state='normal')

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")

    label_bem_vindo = Label(frame_1, text="Fornecedores opções", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_cadastrar = Button(frame_1, command=cadastrar_for, text='Cadastrar', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_cadastrar.place(relx=0.65, rely=0.85, relwidth=0.25, relheight=0.1)
    bt_cadastrar.config(state='disabled')

    bt_alterar = Button(frame_1, command=alterar_for, text='Alterar', bg='SlateGray4', fg='white',
                        font=("verdana", 12, "bold"))
    bt_alterar.place(relx=0.65, rely=0.73, relwidth=0.25, relheight=0.1)
    bt_alterar.config(state='disabled')

    bt_excluir = Button(frame_1, command=excluir_for, text='Excluir', bg='SlateGray4', fg='white',
                        font=("verdana", 12, "bold"))
    bt_excluir.place(relx=0.65, rely=0.6, relwidth=0.25, relheight=0.1)
    bt_excluir.config(state='disabled')

    bt_buscar = Button(frame_1, command=buscar_for, text='Buscar', bg='SlateGray4', fg='white',
                       font=("verdana", 12, "bold"))
    bt_buscar.place(relx=0.05, rely=0.6, relwidth=0.25, relheight=0.1)

    bt_menu = Button(frame_1, command=menu_, text='Menu', bg='SlateGray4', fg='white', font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.85, relwidth=0.25, relheight=0.15)

    lb_cnpj = Label(frame_1, text="CNPJ", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_cnpj.place(relx=0.05, rely=0.2)
    cnpj_entry = Entry(frame_1, font=("Arial", 14))
    cnpj_entry.place(relx=0.05, rely=0.25, relwidth=0.28)

    lb_raz_soc = Label(frame_1, text="Razão social", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_raz_soc.place(relx=0.65, rely=0.48)
    raz_soc_entry = Entry(frame_1, font=("Arial", 14))
    raz_soc_entry.place(relx=0.65, rely=0.53, relwidth=0.28)
    raz_soc_entry.config(state='disabled')

    lb_cep = Label(frame_1, text="CEP", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_cep.place(relx=0.65, rely=0.35)
    cep_entry = Entry(frame_1, font=("Arial", 14))
    cep_entry.place(relx=0.65, rely=0.4, relwidth=0.28)
    cep_entry.config(state='disabled')

    lb_endreco = Label(frame_1, text="Endereço", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_endreco.place(relx=0.05, rely=0.48)
    endereco_entry = Entry(frame_1, font=("Arial", 14))
    endereco_entry.place(relx=0.05, rely=0.53, relwidth=0.28)
    endereco_entry.config(state='disabled')

    lb_bairro = Label(frame_1, text="Bairro", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_bairro.place(relx=0.35, rely=0.2)
    bairro_entry = Entry(frame_1, font=("Arial", 14))
    bairro_entry.place(relx=0.35, rely=0.25, relwidth=0.28)
    bairro_entry.config(state='disabled')

    lb_cidade = Label(frame_1, text="Cidade", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_cidade.place(relx=0.65, rely=0.2)
    cidade_entry = Entry(frame_1, font=("Arial", 14))
    cidade_entry.place(relx=0.65, rely=0.25, relwidth=0.28)
    cidade_entry.config(state='disabled')

    lb_estado = Label(frame_1, text="Estado", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_estado.place(relx=0.35, rely=0.48)
    estado_entry = Entry(frame_1, font=("Arial", 14))
    estado_entry.place(relx=0.35, rely=0.53, relwidth=0.28)
    estado_entry.config(state='disabled')

    lb_tel = Label(frame_1, text="Telefone", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_tel.place(relx=0.05, rely=0.35)
    tel_entry = Entry(frame_1, font=("Arial", 14))
    tel_entry.place(relx=0.05, rely=0.4, relwidth=0.28)
    tel_entry.config(state='disabled')

    lb_tel_r = Label(frame_1, text="Telefone reserva", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_tel_r.place(relx=0.35, rely=0.35)
    tel_r_entry = Entry(frame_1, font=("Arial", 14))
    tel_r_entry.place(relx=0.35, rely=0.4, relwidth=0.28)
    tel_r_entry.config(state='disabled')


def fornecedores():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_menu.destroy()
        lista_fornecedor.destroy()
        scroolLista.destroy()
        bt_crud.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def fornecedores_c():
        destruir_campos()
        fornecedores_crud()

    def buscar_fornecedores():
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )
            cursor = conexao.cursor()
            consulta_sql = "SELECT * FROM fornecedor"
            cursor.execute(consulta_sql)
            resultados = cursor.fetchall()
            for linha in resultados:
                lista_fornecedor.insert("", END, values=linha)

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    label_bem_vindo = Label(frame_1, text="Fornecedores", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.15)

    bt_crud = Button(frame_1, command=fornecedores_c, text='CRUD', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_crud.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.15)

    lista_fornecedor = ttk.Treeview(frame_1, height=3,
                                    columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
    lista_fornecedor.heading("#0", text="")
    lista_fornecedor.heading("#1", text="CNPJ")
    lista_fornecedor.heading("#2", text="Razaosocial")
    lista_fornecedor.heading("#3", text="CEP")
    lista_fornecedor.heading("#4", text="Endereco")
    lista_fornecedor.heading("#5", text="Bairro")
    lista_fornecedor.heading("#6", text="Cidade")
    lista_fornecedor.heading("#7", text="Estado")
    lista_fornecedor.heading("#8", text="Telefone")
    lista_fornecedor.heading("#9", text="Telefonereserva")
    lista_fornecedor.column("#0", width=1)
    lista_fornecedor.column("#1", width=100)
    lista_fornecedor.column("#2", width=100)
    lista_fornecedor.column("#3", width=70)
    lista_fornecedor.column("#4", width=80)
    lista_fornecedor.column("#5", width=60)
    lista_fornecedor.column("#6", width=100)
    lista_fornecedor.column("#7", width=50)
    lista_fornecedor.column("#8", width=100)
    lista_fornecedor.column("#9", width=100)
    lista_fornecedor.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.55)

    scroolLista = Scrollbar(frame_1, orient='vertical')
    lista_fornecedor.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.90, rely=0.43, relwidth=0.04, relheight=0.50)

    buscar_fornecedores()


def pagamentos():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Quality"
    )

    def destruir_campos():
        lb_forma_pag.destroy()
        forma_pag_entry.destroy()
        conta_entry.destroy()
        lb_conta.destroy()
        acrescimo_entry.destroy()
        lb_acrescimo.destroy()
        juros_entry.destroy()
        lb_juros.destroy()
        multa_pag_entry.destroy()
        lb_multa_pag.destroy()
        valor_pag_entry.destroy()
        lb_valor_pag.destroy()
        data_pag_entry.destroy()
        lb_data_pag.destroy()
        num_conta_entry.destroy()
        lb_num_conta.destroy()
        num_pag_entry.destroy()
        lb_num_pag.destroy()
        bt_menu.destroy()
        bt_cadastrar.destroy()
        label_bem_vindo.destroy()
        bt_tabela.destroy()
        bt_confirmar.destroy()

    def limpar_tela():
        forma_pag_entry.delete(0, END)
        conta_entry.delete(0, END)
        acrescimo_entry.delete(0, END)
        juros_entry.delete(0, END)
        multa_pag_entry.delete(0, END)
        valor_pag_entry.delete(0, END)
        data_pag_entry.delete(0, END)
        num_conta_entry.delete(0, END)
        num_pag_entry.delete(0, END)
        
    
    def pesquisar_conta2():
        limpar_tela()
        try:
            cursor = conexao.cursor()
            texto_digitado = num_conta_entry.get() 
            consulta_sql = "SELECT valor FROM contas_pagar WHERE num_conta = %s"
            cursor.execute(consulta_sql, (texto_digitado,))
            resultados = cursor.fetchall()
            for linha in resultados: 
                valor_pag_entry.insert(0, linha[0] )
                
                
        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.shoaskyesnowinfo("Mensagem", "pesquisa não realizada.")
        
        
        
    def menu1():
        destruir_campos()
        menu()

    def tabela_pagamento():
        destruir_campos()
        tabela_pg()

    def cadastrar_pag():
        num_pag1 = num_pag_entry.get()
        num_cont1 = num_conta_entry.get()
        data_pag1 = data_pag_entry.get()
        valor_pag1 = valor_pag_entry.get()
        multa_pag1 = multa_pag_entry.get()
        juros_pag1 = juros_entry.get()
        acrescimo_pag1 = acrescimo_entry.get()
        conta_pag1 = conta_entry.get()
        forma_pag1 = forma_pag_entry.get()

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )

            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO pagamento (num_pagamento, num_conta, data_pgto, valor_pgto, multa, juros, acrescimo, conta, forma_pgto)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                num_pag1, num_cont1, data_pag1, valor_pag1, multa_pag1, juros_pag1, acrescimo_pag1, conta_pag1,
                forma_pag1))

            conexao.commit()
            messagebox.showinfo("Mensagem", "Dados inseridos com sucesso.")

        except mysql.connector.Error as erro:
            print("Erro ao inserir os dados:", erro)
            messagebox.showinfo("Erro", f"Erro ao inserir os dados: {erro}")

        finally:
            limpar_tela()

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT num_conta FROM contas_pagar ")
        count = [item[0] for item in cursor.fetchall()]
        
        
    except mysql.connector.Error as e:
        print("Erro ao atualizar o fornecedor:", e)

    label_bem_vindo = Label(frame_1, text="Pagamento", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_cadastrar = Button(frame_1, command=cadastrar_pag, text='Cadastrar', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_cadastrar.place(relx=0.65, rely=0.85, relwidth=0.25, relheight=0.15)

    bt_menu = Button(frame_1, command=menu1, text='Menu', bg='SlateGray4', fg='white', font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.85, relwidth=0.25, relheight=0.15)

    bt_tabela = Button(frame_1, command=tabela_pagamento, text='Tabela', bg='SlateGray4', fg='white',
                       font=("verdana", 12, "bold"))
    bt_tabela.place(relx=0.35, rely=0.85, relwidth=0.25, relheight=0.15)

    lb_num_pag = Label(frame_1, text="Número do pagamento", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_num_pag.place(relx=0.05, rely=0.35)
    num_pag_entry = Entry(frame_1, font=("Arial", 14))
    num_pag_entry.place(relx=0.05, rely=0.4, relwidth=0.28)

    lb_num_conta = Label(frame_1, text="Número da conta", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_num_conta.place(relx=0.35, rely=0.35)
    num_conta_entry = ttk.Combobox(frame_1, values=count,
                                   state="readonly", font=("verdana", 14))
    num_conta_entry.set("Selecione")
    num_conta_entry.place(relx=0.35, rely=0.45, relwidth=0.20, relheight=0.05)
    
    bt_confirmar = Button(frame_1, command=pesquisar_conta2 ,text='Pesquisar', bg='SlateGray4', fg='white',
                       font=("verdana", 5, "bold"))
    bt_confirmar.place(relx=0.55, rely=0.45, relwidth=0.09, relheight=0.05)

    lb_data_pag = Label(frame_1, text="Data do pagamento", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_data_pag.place(relx=0.65, rely=0.35)
    data_pag_entry = Entry(frame_1, font=("Arial", 14))
    data_pag_entry.place(relx=0.65, rely=0.4, relwidth=0.28)

    lb_valor_pag = Label(frame_1, text="Valor do pagamento", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_valor_pag.place(relx=0.05, rely=0.55)
    valor_pag_entry = Entry(frame_1, font=("Arial", 14))
    valor_pag_entry.place(relx=0.05, rely=0.6, relwidth=0.28)

    lb_multa_pag = Label(frame_1, text="Multa", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_multa_pag.place(relx=0.65, rely=0.55)
    multa_pag_entry = Entry(frame_1, font=("Arial", 14))
    multa_pag_entry.place(relx=0.65, rely=0.6, relwidth=0.28)

    lb_juros = Label(frame_1, text="Juros", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_juros.place(relx=0.35, rely=0.2)
    juros_entry = Entry(frame_1, font=("Arial", 14))
    juros_entry.place(relx=0.35, rely=0.25, relwidth=0.28)

    lb_acrescimo = Label(frame_1, text="Acrescimo", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_acrescimo.place(relx=0.65, rely=0.2)
    acrescimo_entry = Entry(frame_1, font=("Arial", 14))
    acrescimo_entry.place(relx=0.65, rely=0.25, relwidth=0.28)

    lb_conta = Label(frame_1, text="Conta", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_conta.place(relx=0.35, rely=0.55)
    conta_entry = Entry(frame_1, font=("Arial", 14))
    conta_entry.place(relx=0.35, rely=0.6, relwidth=0.28)

    lb_forma_pag = Label(frame_1, text="Forma de pagamento", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_forma_pag.place(relx=0.01, rely=0.2)
    forma_pag_entry = ttk.Combobox(frame_1, values=["Pix", "Cheque", "Transferencia", "Dinheiro", "Cartão"],
                                   state="readonly")
    forma_pag_entry.set("Selecione")
    forma_pag_entry.place(relx=0.05, rely=0.25)


def constas_abertas():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_menu.destroy()
        lista_contas_pagas.destroy()
        scroolLista.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def pesquisar_tabela_pagos():
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )
            cursor = conexao.cursor()
            consulta_sql = "SELECT * FROM contas_pagar WHERE status_conta = %s"
            cursor.execute(consulta_sql, ('Em aberto',))
            resultados = cursor.fetchall()

            for item in lista_contas_pagas.get_children():
                lista_contas_pagas.delete(item)
            for linha in resultados:
                lista_contas_pagas.insert("", 'end', values=linha)

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")


    label_bem_vindo = Label(frame_1, text="Contas Pendentes", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.04, rely=0.05, relwidth=0.2, relheight=0.15)

    lista_contas_pagas = ttk.Treeview(frame_1, height=3,
                                      columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",))
    lista_contas_pagas.heading("#0", text="")
    lista_contas_pagas.heading("#1", text="Conta")
    lista_contas_pagas.heading("#2", text="CNPJ")
    lista_contas_pagas.heading("#3", text="Documento")
    lista_contas_pagas.heading("#4", text="Vencimento")
    lista_contas_pagas.heading("#5", text="Valor")
    lista_contas_pagas.heading("#6", text="Status")
    lista_contas_pagas.column("#0", width=1)
    lista_contas_pagas.column("#1", width=100)
    lista_contas_pagas.column("#2", width=100)
    lista_contas_pagas.column("#3", width=100)
    lista_contas_pagas.column("#4", width=100)
    lista_contas_pagas.column("#5", width=80)
    lista_contas_pagas.column("#6", width=100)

    lista_contas_pagas.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.55)

    # Scrollbar para a Treeview
    scroolLista = Scrollbar(frame_1, orient='vertical')
    lista_contas_pagas.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.90, rely=0.43, relwidth=0.04, relheight=0.50)

    # Chamar a função de pesquisa
    pesquisar_tabela_pagos()


def status_contas():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_pg_aberto.destroy()
        bt_pg_pagos.destroy()
        bt_atualizar.destroy()
        bt_menu.destroy()
        bt_menu.destroy()
        bt_todas_contas.destroy()
        label_bem_vindo.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def atualizar_status_():
        destruir_campos()
        atualizar_status()

    def tabela_contas_pagar_():
        destruir_campos()
        tabela_contas_pagar()

    def contas_pagas_():
        destruir_campos()
        contas_pagas()

    def contas_abertas_():
        destruir_campos()
        constas_abertas()

    label_bem_vindo = Label(frame_1, text="Status Contas", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_pg_aberto = Button(frame_1, command=contas_abertas_, text='Pendentes', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_pg_aberto.place(relx=0.12, rely=0.4, relwidth=0.25, relheight=0.15)

    bt_pg_pagos = Button(frame_1, command=contas_pagas_, text='Pagas', bg='SlateGray4', fg='white',
                         font=("verdana", 12, "bold"))
    bt_pg_pagos.place(relx=0.65, rely=0.4, relwidth=0.25, relheight=0.15)

    bt_atualizar = Button(frame_1, command=atualizar_status_, text='Atualizar', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_atualizar.place(relx=0.65, rely=0.65, relwidth=0.25, relheight=0.15)

    bt_todas_contas = Button(frame_1, command=tabela_contas_pagar_, text='Todas', bg='SlateGray4', fg='white',
                             font=("verdana", 12, "bold"))
    bt_todas_contas.place(relx=0.389, rely=0.65, relwidth=0.25, relheight=0.15)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.12, rely=0.65, relwidth=0.25, relheight=0.15)


def tabela_contas_pagar():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_menu.destroy()
        lista_contas_pagar.destroy()
        scroolLista.destroy()
        bt_pesquisar.destroy()
        data_entry.destroy()
        lb_data.destroy()
        bt_voltar.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def pesquisar_tabela():

        for item in lista_contas_pagar.get_children():
            lista_contas_pagar.delete(item)
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )
            cursor = conexao.cursor()
            consulta_sql = "SELECT * FROM contas_pagar"
            cursor.execute(consulta_sql)
            resultados = cursor.fetchall()
            for linha in resultados:
                lista_contas_pagar.insert("", END, values=linha)

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def pesquisar_data():
        for item in lista_contas_pagar.get_children():
            lista_contas_pagar.delete(item)
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )
            data = data_entry.get()
            cursor = conexao.cursor()
            consulta_sql = "SELECT * FROM contas_pagar WHERE vencimento = %s"
            cursor.execute(consulta_sql, (data,))
            resultados = cursor.fetchall()
            lista_contas_pagar

            for linha in resultados:
                lista_contas_pagar.insert("", END, values=linha)


        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")

    label_bem_vindo = Label(frame_1, text="Contas", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.15)

    bt_pesquisar = Button(frame_1, command=pesquisar_data, text='Pesquisar', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_pesquisar.place(relx=0.8, rely=0.12, relwidth=0.15, relheight=0.1)

    bt_voltar = Button(frame_1, command=pesquisar_tabela, text='Voltar', bg='SlateGray4', fg='white',
                       font=("verdana", 12, "bold"))
    bt_voltar.place(relx=0.8, rely=0.25, relwidth=0.15, relheight=0.1)

    lb_data = Label(frame_1, text="Data (AAAA/MM/DD)", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_data.place(relx=0.65, rely=0.049)
    data_entry = Entry(frame_1, bg="#D3D3D3", font=("Arial", 14))
    data_entry.place(relx=0.65, rely=0.12, relwidth=0.1, relheight=0.05)

    lista_contas_pagar = ttk.Treeview(frame_1, height=3,
                                      columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",))
    lista_contas_pagar.heading("#0", text="")
    lista_contas_pagar.heading("#1", text="Conta")
    lista_contas_pagar.heading("#2", text="CNPJ")
    lista_contas_pagar.heading("#3", text="Documento")
    lista_contas_pagar.heading("#4", text="Vencimento")
    lista_contas_pagar.heading("#5", text="Valor")
    lista_contas_pagar.heading("#6", text="Status")
    lista_contas_pagar.column("#0", width=1)
    lista_contas_pagar.column("#1", width=100)
    lista_contas_pagar.column("#2", width=100)
    lista_contas_pagar.column("#3", width=100)
    lista_contas_pagar.column("#4", width=100)
    lista_contas_pagar.column("#5", width=80)
    lista_contas_pagar.column("#6", width=100)

    lista_contas_pagar.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.55)

    scroolLista = Scrollbar(frame_1, orient='vertical')
    lista_contas_pagar.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.90, rely=0.43, relwidth=0.04, relheight=0.50)
    pesquisar_tabela()


def contas_pagas():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_menu.destroy()
        lista_contas_pagas.destroy()
        scroolLista.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def pesquisar_tabela_pagos():
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )
            cursor = conexao.cursor()
            consulta_sql = "SELECT * FROM contas_pagar WHERE status_conta = %s"
            cursor.execute(consulta_sql, ('Pago',))
            resultados = cursor.fetchall()

            for item in lista_contas_pagas.get_children():
                lista_contas_pagas.delete(item)
            for linha in resultados:
                lista_contas_pagas.insert("", 'end', values=linha)

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    label_bem_vindo = Label(frame_1, text="Contas Pagas", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.15)

    lista_contas_pagas = ttk.Treeview(frame_1, height=3,
                                      columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7",))
    lista_contas_pagas.heading("#0", text="")
    lista_contas_pagas.heading("#1", text="Conta")
    lista_contas_pagas.heading("#2", text="CNPJ")
    lista_contas_pagas.heading("#3", text="Documento")
    lista_contas_pagas.heading("#4", text="Vencimento")
    lista_contas_pagas.heading("#5", text="Valor")
    lista_contas_pagas.heading("#6", text="Status")
    lista_contas_pagas.column("#0", width=1)
    lista_contas_pagas.column("#1", width=100)
    lista_contas_pagas.column("#2", width=100)
    lista_contas_pagas.column("#3", width=100)
    lista_contas_pagas.column("#4", width=100)
    lista_contas_pagas.column("#5", width=80)
    lista_contas_pagas.column("#6", width=100)

    lista_contas_pagas.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.55)

    # Scrollbar para a Treeview
    scroolLista = Scrollbar(frame_1, orient='vertical')
    lista_contas_pagas.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.90, rely=0.43, relwidth=0.04, relheight=0.50)

    # Chamar a função de pesquisa
    pesquisar_tabela_pagos()


def atualizar_status():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Quality"
    )

    def destruir_campos():
        lb_status.destroy()
        status_entry.destroy()
        label_bem_vindo.destroy()
        bt_menu.destroy()
        lb_num_conta.destroy()
        num_conta_entry.destroy()
        bt_confirmar.destroy()

    def limpar_tela():
        status_entry.delete(0, END)
        num_conta_entry.delete(0, END)

    def menu_voltar():
        destruir_campos()
        menu()

    def atualizar_conta():
        num_conta = num_conta_entry.get()
        status_conta = status_entry.get()
        try:
            cursor = conexao.cursor()
            query = """
            UPDATE contas_pagar
            SET status_conta = %s
            WHERE num_conta = %s
            """
            cursor.execute(query, (status_conta, num_conta))
            conexao.commit()
            messagebox.showinfo("Mensagem", "Alteração realizada.")

        except mysql.connector.Error as e:
            print("Erro ao atualizar o fornecedor:", e)
            messagebox.showinfo("Mensagem", "Alteração não realizada.")
        finally:
            limpar_tela()

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT num_conta FROM contas_pagar ")
        count = [item[0] for item in cursor.fetchall()]
    except mysql.connector.Error as e:
        print("Erro ao atualizar o fornecedor:", e)
        messagebox.showinfo("Mensagem", "Alteração não realizada.")

    label_bem_vindo = Label(frame_1, text="Atualizar Status", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    lb_status = Label(frame_1, text="Status", bg='#dfe3ee', fg='#107db2', font=("verdana", 16, "bold"))
    lb_status.place(relx=0.09, rely=0.25)
    status_entry = ttk.Combobox(frame_1, values=["Pago", "Em aberto"],
                                state="readonly", font=("verdana", 14))
    status_entry.set("Selecione")
    status_entry.place(relx=0.05, rely=0.35)

    lb_num_conta = Label(frame_1, text="Número da conta", bg='#dfe3ee', fg='#107db2', font=("verdana", 16, "bold"))
    lb_num_conta.place(relx=0.45, rely=0.25)
    num_conta_entry = ttk.Combobox(frame_1, values=count,
                                   state="readonly", font=("verdana", 14))
    num_conta_entry.set("Selecione")
    num_conta_entry.place(relx=0.45, rely=0.35, relwidth=0.28)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.03, rely=0.77, relwidth=0.25, relheight=0.15)

    bt_confirmar = Button(frame_1, command=atualizar_conta, text='Confirmar', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_confirmar.place(relx=0.78, rely=0.3, relwidth=0.17, relheight=0.15)


def tabela_pg():
    def destruir_campos():
        label_bem_vindo.destroy()
        bt_menu.destroy()
        lista_pagamento.destroy()
        scroolLista.destroy()

    def menu_voltar():
        destruir_campos()
        menu()

    def buscar_pagamento():

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Quality"
            )
            cursor = conexao.cursor()
            consulta_sql = "SELECT * FROM pagamento"
            cursor.execute(consulta_sql)
            resultados = cursor.fetchall()
            for linha in resultados:
                lista_pagamento.insert("", END, values=linha)

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    label_bem_vindo = Label(frame_1, text="Pagamento", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.15)

    lista_pagamento = ttk.Treeview(frame_1, height=3,
                                   columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9",))
    lista_pagamento.heading("#0", text="")
    lista_pagamento.heading("#1", text="pagamento")
    lista_pagamento.heading("#2", text="num conta")
    lista_pagamento.heading("#3", text="data")
    lista_pagamento.heading("#4", text="valor")
    lista_pagamento.heading("#5", text="multa")
    lista_pagamento.heading("#6", text="juros")
    lista_pagamento.heading("#7", text="acrescimo")
    lista_pagamento.heading("#8", text="conta")
    lista_pagamento.heading("#9", text="forma pagamento")
    lista_pagamento.column("#0", width=1)
    lista_pagamento.column("#1", width=60)
    lista_pagamento.column("#2", width=80)
    lista_pagamento.column("#3", width=70)
    lista_pagamento.column("#4", width=80)
    lista_pagamento.column("#5", width=60)
    lista_pagamento.column("#6", width=50)
    lista_pagamento.column("#7", width=50)
    lista_pagamento.column("#8", width=50)
    lista_pagamento.column("#9", width=100)
    lista_pagamento.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.55)

    scroolLista = Scrollbar(frame_1, orient='vertical')
    lista_pagamento.configure(yscroll=scroolLista.set)
    scroolLista.place(relx=0.90, rely=0.43, relwidth=0.04, relheight=0.50)

    buscar_pagamento()


def bancos():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Quality"
    )

    def destruir_campos():
        label_bem_vindo.destroy()
        bt_menu.destroy()
        bt_buscar.destroy()
        bt_excluir.destroy()
        bt_alterar.destroy()
        bt_cadastrar.destroy()
        des_nome_entry.destroy()
        lb_desc_nome.destroy()
        num_cont_entry.destroy()
        lb_num_cont.destroy()
        agencia_entry.destroy()
        lb_agencia.destroy()
        banco_entry.destroy()
        lb_banco.destroy()
        num_entry.destroy()
        lb_num.destroy()

    def limpar_tela():
        des_nome_entry.delete(0, END)
        num_cont_entry.delete(0, END)
        agencia_entry.delete(0, END)
        banco_entry.delete(0, END)
        num_entry.delete(0, END)

    def menu_voltar():
        destruir_campos()
        menu()

    def excluir_bancos():

        try:
            cursor = conexao.cursor()
            texto_digitado = num_entry.get()

            cursor.execute("SELECT COUNT(*) FROM bancos WHERE numero = %s", (texto_digitado,))
            count = cursor.fetchone()[0]

            if count > 0:
                sql = "DELETE FROM bancos WHERE numero = %s"
                cursor.execute(sql, (texto_digitado,))
                conexao.commit()

                cursor.execute("SELECT COUNT(*) FROM bancos WHERE numero = %s", (texto_digitado,))
                count = cursor.fetchone()[0]

                if count == 0:
                    messagebox.showinfo("Mensagem", "Exclusão realizada.")
                else:
                    messagebox.showinfo("Mensagem", "Exclusão não realizada.")
            else:
                messagebox.showinfo("Mensagem", "Registro não encontrado.")
        except mysql.connector.Error as erro:
            print("Erro ao deletar o dado:", erro)
            messagebox.showinfo("ERRO", "Exclusão não realizada.")
        finally:
            limpar_tela()
            bt_excluir.config(state='disabled')
            bt_alterar.config(state='disabled')
            bt_cadastrar.config(state='disabled')
            des_nome_entry.config(state='disabled')
            num_cont_entry.config(state='disabled')
            agencia_entry.config(state='disabled')
            banco_entry.config(state='disabled')
            num_entry.config(state='normal')

    def cadastrar_banco():
        desc_ = des_nome_entry.get()
        num_cont = num_cont_entry.get()
        agencia_ = agencia_entry.get()
        banco_ = banco_entry.get()
        num_ = num_entry.get()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO bancos (numero, banco, agencia, num_contacorrente, descricao_nome) VALUES (%s, %s, %s, %s, %s)",
                (num_, banco_, agencia_, num_cont, desc_))
            conexao.commit()
            messagebox.showinfo("Mensagem", "Dados inseridos com sucesso.")

        except mysql.connector.Error as erro:
            print("Erro ao inserir os dados:", erro)
            messagebox.showinfo("Mensagem", "Erro ao inserir os dados.")
        finally:
            limpar_tela()
            bt_cadastrar.config(state='disabled')
            des_nome_entry.config(state='disabled')
            num_cont_entry.config(state='disabled')
            agencia_entry.config(state='disabled')
            banco_entry.config(state='disabled')
            num_entry.config(state='normal')

    def alterar_banco():
        banco_ = banco_entry.get()
        agencia_ = agencia_entry.get()
        num_cont = num_cont_entry.get()
        nome_ = des_nome_entry.get()
        num_ = num_entry.get()

        try:
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE bancos SET banco = %s, agencia = %s, num_contacorrente = %s, descricao_nome = %s WHERE numero = %s",
                (banco_, agencia_, num_cont, nome_, num_))
            conexao.commit()
            messagebox.showinfo("Mensagem", " Alteração feita com sucesso.")

        except mysql.connector.Error as e:
            print("Erro ao atualizar :", e)
        finally:
            limpar_tela()
            bt_alterar.config(state='disabled')
            bt_cadastrar.config(state='disabled')
            bt_excluir.config(state='disabled')
            des_nome_entry.config(state='disabled')
            num_cont_entry.config(state='disabled')
            agencia_entry.config(state='disabled')
            banco_entry.config(state='disabled')
            num_entry.config(state='normal')

    def pesquisar_banco():
        try:
            cursor = conexao.cursor()
            num_cont_ = num_entry.get()
            cursor.execute("SELECT COUNT(*) FROM bancos WHERE numero = %s", (num_cont_,))
            count = cursor.fetchone()[0]
            if count > 0:
                consulta_sql = "SELECT * FROM bancos WHERE numero = %s"
                cursor.execute(consulta_sql, (num_cont_,))
                resultados = cursor.fetchall()

                bt_alterar.config(state='normal')
                bt_excluir.config(state='normal')
                banco_entry.config(state='normal')
                agencia_entry.config(state='normal')
                des_nome_entry.config(state='normal')
                num_cont_entry.config(state='normal')
                num_entry.config(state='disabled')

                for linha in resultados:
                    banco_entry.delete(0, END)
                    agencia_entry.delete(0, END)
                    des_nome_entry.delete(0, END)
                    num_cont_entry.delete(0, END)
                    banco_entry.insert(0, linha[1])
                    agencia_entry.insert(0, linha[2])
                    des_nome_entry.insert(0, linha[3])
                    num_cont_entry.insert(0, linha[4])

            else:
                bt_cadastrar.config(state='normal')
                num_cont_entry.config(state='normal')
                banco_entry.config(state='normal')
                agencia_entry.config(state='normal')
                des_nome_entry.config(state='normal')
                num_entry.config(state='disabled')

        except mysql.connector.Error as erro:
            print("Erro ao pesquisar o dado:", erro)
            messagebox.showinfo("Mensagem", "Pesquisa não realizada.")

    label_bem_vindo = Label(frame_1, text="Bancos", bg='#dfe3ee', font=("verdana", 24, "bold"))
    label_bem_vindo.config(bd=5, relief=GROOVE, padx=10, pady=10)
    label_bem_vindo.pack(pady=20)

    bt_menu = Button(frame_1, command=menu_voltar, text='Menu', bg='SlateGray4', fg='white',
                     font=("verdana", 12, "bold"))
    bt_menu.place(relx=0.05, rely=0.85, relwidth=0.25, relheight=0.15)

    lb_num = Label(frame_1, text="Número", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_num.place(relx=0.05, rely=0.35)
    num_entry = Entry(frame_1, font=("Arial", 14))
    num_entry.place(relx=0.05, rely=0.4, relwidth=0.13)

    lb_banco = Label(frame_1, text="Banco", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_banco.place(relx=0.35, rely=0.35)
    banco_entry = Entry(frame_1, font=("Arial", 14))
    banco_entry.place(relx=0.35, rely=0.4, relwidth=0.28)
    banco_entry.config(state='disabled')

    lb_agencia = Label(frame_1, text="Agencia", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_agencia.place(relx=0.65, rely=0.35)
    agencia_entry = Entry(frame_1, font=("Arial", 14))
    agencia_entry.place(relx=0.65, rely=0.4, relwidth=0.28)
    agencia_entry.config(state='disabled')

    lb_num_cont = Label(frame_1, text="Número C.Corrente", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_num_cont.place(relx=0.05, rely=0.55)
    num_cont_entry = Entry(frame_1, font=("Arial", 14))
    num_cont_entry.place(relx=0.05, rely=0.6, relwidth=0.28)
    num_cont_entry.config(state='disabled')

    lb_desc_nome = Label(frame_1, text="Descrição/nome", bg='#dfe3ee', fg='#107db2', font=("verdana", 12, "bold"))
    lb_desc_nome.place(relx=0.35, rely=0.55)
    des_nome_entry = Entry(frame_1, font=("Arial", 14))
    des_nome_entry.place(relx=0.35, rely=0.6, relwidth=0.28)
    des_nome_entry.config(state='disabled')

    bt_cadastrar = Button(frame_1, command=cadastrar_banco, text='Cadastrar', bg='SlateGray4', fg='white',
                          font=("verdana", 12, "bold"))
    bt_cadastrar.place(relx=0.65, rely=0.5, relwidth=0.25, relheight=0.12)
    bt_cadastrar.config(state='disabled')

    bt_alterar = Button(frame_1, command=alterar_banco, text='Alterar', bg='SlateGray4', fg='white',
                        font=("verdana", 12, "bold"))
    bt_alterar.place(relx=0.65, rely=0.65, relwidth=0.25, relheight=0.12)
    bt_alterar.config(state='disabled')

    bt_excluir = Button(frame_1, command=excluir_bancos, text='Excluir', bg='SlateGray4', fg='white',
                        font=("verdana", 12, "bold"))
    bt_excluir.place(relx=0.65, rely=0.80, relwidth=0.25, relheight=0.12)
    bt_excluir.config(state='disabled')

    bt_buscar = Button(frame_1, command=pesquisar_banco, text='Buscar', bg='SlateGray4', fg='white',
                       font=("verdana", 12, "bold"))
    bt_buscar.place(relx=0.22, rely=0.4, relwidth=0.10, relheight=0.08)


menu()

janela.mainloop()
