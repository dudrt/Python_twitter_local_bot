#Olá, para começar nós precisamos importar algumas bibliotecas.
from selenium import webdriver
#Selenium será o nosso navegador usado pelo python.
from selenium.webdriver.common.keys import Keys
#Keys vai servir para o selenium entender oque é enter ou outras teclas do nosso teclado ou mouse.
import tweepy
#Tweepy é a biblioteca que faz com que o python se comunique com o twitter.

#Primeiro você nomeia uma variavel para ser o navegador, neste caso está chrome ,pois foi oque eu usei.
#No site oficial do selenium onde está sua documentação, existe mais opções de navegadores.
chrome=webdriver.Chrome()

#Agora precisamos passar o link do site que o nosso navegador deve abrir.
chrome.get("https://www.google.com.br/")


#Neste eu quero pesquisar no google, e como o local de pesquisa possui o "name" = "q", consigo encontrar 
#o elemento e na mesma linha escrever oque quero pesquisar!
#É bom lembrar que existe diferentes maneiras de se localizar um elemento, name, id, class e xpath são alguns.
#Na documentação do Selenium existe todas as maneiras!
chrome.find_element_by_name('q').send_keys("dolar")
#Agora pense em como você pesquisa algo, logo após escrever oque gostaria de pesquisar, precisa apertar o enter.
#Novamente iremos identificar o elemento de pesquisa e desta vez, falaremos para o nosso navegador clicar no enter.
chrome.find_element_by_name('q').send_keys(Keys.ENTER)
#----------------------------------------------------------Importante-----------------------------------------
#Esta é uma parte que você precisa prestar atenção. Agora você encontrará o que deseja em uma página ou pesquisa, sabemos 
#que toda página html tem elementos,alguns possuem id, class, name, mas outros não, nestes casos você precisará obter o XPATH do elemento.
#talvez tudo o que você deseja obter tenha pelo menos classe ou nome, mas eu recomendo que você dê uma olhada em como pegar o XPATH de um elemento
#Então volte e veja o documento XPATH_EN-PT.md.

#Você pode escolher a melhor maneira de procurar um elemento, no documento READMETOBEGIN.md, deixei o site de documentação do selenium.
#Por xpath, id, class, name, o que você preferir.
#Na mesma linha você pode dar o comando get_attribute("whatever you want to get").

dolar=chrome.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

printdolar="💵 DÓLAR ESTÁ VALENDO R$:"+dolar
#fim pegar dolar


#---------------------------pegar imposto-----------------------------------------------------------------
impostototal=[]
impostoformat=[]
nu=""
chrome.get("https://impostometro.com.br/")
imposto=chrome.find_element_by_id('counterBrasil').text

tamanho=len(imposto)


for i in range (tamanho):
    testenumero=imposto[i].isnumeric()
    if testenumero:
        impostototal.append(imposto[i])
    

#-------------------------------------formatar o imposto--------------------------------------


#-------------------------------------------------entrar no twitter e publicar--------------------------

auth=tweepy.OAuthHandler('api key','api secret key')
auth.set_access_token('access token','secret access token')

tweet=tweepy.API(auth)

tweet.update_status(printdolar+'\n'+printeuro+'\n'+printbit+'\n'+printimposto)
