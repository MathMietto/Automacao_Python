
import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.getWindowsWithTitle("chrome")[0].maximize()
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=389, y=372)
pyautogui.write("m.mietto97@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=678, y=538)

time.sleep(2)

#Importando a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:    
    
    # Cadastrando os produtos
    pyautogui.click(x=399, y=257)
    # código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo 
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


