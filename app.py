from tkinter import * # Módulo para criar interfaces gráficas em Python
from tkinter.ttk import * # Módulo para trabalhar com datas e horários em Python
from time import strftime # Função para formatar objetos de tempo em strings


# Criação da janela principal
root = Tk() # -> Cria uma instância da classe Tk, que é a janela principal da aplicação
root.title('Relógio') # -> Define o título da janela como 'Relógio'

# Definição da função para atualizar o horário
def atualizar_horario(): # -> Esta função é chamada repetidamente para atualizar o horário exibido no rótulo a cada segundo.
    horario_atual = strftime('%H:%M:%S %p') # -> Obtém o horário atual formatado
    rotulo.config(text=horario_atual) # -> Configura o texto do rótulo como o horário atual
    rotulo.after(1000, atualizar_horario) # -> Aguarda 1000 milissegundos (1 segundo) e chama a função novamente

# Criação do rótulo para exibir o horário
rotulo = Label(root, font=('franklin gothic', 40, 'bold'), background='black', foreground='white')
rotulo.pack(anchor='center') # -> Posiciona o rótulo no centro da janela

# Chamada da função para iniciar a atualização do horário
atualizar_horario() 

# Loop principal da interface gráfica
root.mainloop() # -> Inicia o loop principal da interface gráfica, mantendo a janela aberta e aguardando as interações do usuário