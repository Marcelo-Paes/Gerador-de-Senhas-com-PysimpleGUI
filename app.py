# Criar um programa de interface gráfica que deve fazer:
# Armazenar o site/software para qual a senha será gerada
# Armazenar a senha
# Possibilidade de configurar o tamanho da senha

import random
import PySimpleGUI as sg
import os
import time

class PassGen:
    def __init__(self):
    #layout da pagina
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))], 
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declarar a janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
       
        try:
            
            while True:
                
                evento, valores = self.janela.read()
                
                if evento == sg.WINDOW_CLOSED:
                    print("Evento de fechamento de janela")
                    break
                # Tratamento do evento "Gerar Senha"
                if evento == 'Gerar Senha':
                    try:
                        
                        nova_senha = self.gerar_senha(valores)
                        print(f"Nova senha gerada: {nova_senha}")
                        
                        self.salvar_senha(nova_senha, valores)
                        print("Senha salva")
                    except Exception as e:
                        print(f"Erro ao gerar senha: {e}")
                        sg.popup_error(f"Erro ao gerar senha: {e}")
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}")

        print("Fechando janela")
        self.janela.close()  # Fora do loop while, feche a janela quando a interação estiver concluída





    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass


    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")
      




gen = PassGen()
gen.Iniciar()