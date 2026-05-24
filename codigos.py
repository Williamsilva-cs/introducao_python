import pyautogui
import time
import pandas
import pyperclip
# passo 1: Entrar no link da empresa
pyautogui.PAUSE = 1.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=440, y=462, clicks=2)
pyautogui.click(x=440, y=462, clicks=1)
pyautogui.click(x=600, y=461, clicks=1)
pyautogui.click(x=776, y=566, clicks=1)
time.sleep(3)
# Até aqui, baixamos o aquivo do drive

caminho = r"C:\Users\willi\Downloads\Vendas - Dez.xlsx"
tabela = pandas.read_excel(caminho)
print(tabela)

# somar a quantidade de produtos e o faturamento

faturamento = tabela ["Valor Final"].sum()
qtde_produtos = tabela ["Quantidade"].sum()
print(faturamento)
print(qtde_produtos)
time.sleep(5)

# Abrir o e-mail
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com")
pyautogui.press ("enter")
time.sleep(4)
pyautogui.click(x=111, y=271)

#enviar e-mail
pyautogui.write("williamhotmail966@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

# escrever texto com caracteres especiais
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# conteúdo do e-mail
texto = f"""
Prezados,
Segue o relatório de vendas de hoje: 

Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {qtde_produtos:,}

Estou a disposição para qualquer dúvida.
Atenciosamente, William.

             """
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1234, y=978)