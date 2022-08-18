#Olá, para começar nós precisamos importar algumas bibliotecas.
from selenium import webdriver
#Selenium será o nosso navegador usado pelo python.
from selenium.webdriver.common.keys import Keys
#Keys vai servir para o selenium entender oque é enter ou outras teclas do nosso teclado ou mouse.
import tweepy
#Tweepy é a biblioteca que faz com que o python se comunique com o twitter.

#Primeiro você nomeia uma variavel para ser o navegador, neste caso está 'chrome' ,pois foi oque eu usei.
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
#Esta é uma parte que você precisa prestar atenção. Agora você encontrará o que deseja em uma página ou pesquisa. Sabemos 
#que toda página html tem elementos,alguns possuem id, class, name, mas outros não, nestes casos você precisará obter o XPATH do elemento.
#talvez tudo o que você deseja obter tenha pelo menos classe ou nome, mas eu recomendo que você dê uma olhada em como pegar o XPATH de um elemento
#Então volte e veja o documento XPATH_EN-PT.md.

#Você pode escolher a melhor maneira de procurar um elemento(no documento READMETOBEGIN.md, deixei o site de documentação do selenium).
#Por xpath, id, class, name, o que você preferir.
#E na mesma linha você pode dar o comando get_attribute("Oque-você-quiser").

dolar=chrome.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute("data-value")

#Se você quiser, pode enfeitar e/ou formatar o dado que conseguiu obter sem nenhum problema. 
printdolar="💵 DÓLAR ESTÁ VALENDO R$:"+dolar

#E pronto, a parte mais básica está pronta você já consegue fazer coisas legais com estes comandos. Procure mais comandos no site oficial do selenium.
#Agora começa a parte mais complicada, que é conectar o tweepy com o twitter. Para esta parte eu recomendo que você pesquise em alguns videos ou sites
#como conseguir o nível de acesso nescessário para postar conteúdo.

#Basicamente você deve entrar no site do desenvolvedor do twitter https://developer.twitter.com e fazer login com o a conta do twitter do seu bot
#e logo após isso deve seguir as instruções primárias.Logo após, você precisa do nível de acesso de desenvolvedor, ou "Nível de autenticação 2".


#-------------------------------------------------entrar no twitter e publicar--------------------------
#Agora que você conseguiu o nível de acesso nescessário para postar coisas no twitter
#para postar alguma frase ou palavra no twitter basta alguns códigos.
veri=tweepy.OAuthHandler('api key','api secret key')
veri.set_access_token('access token','secret access token')

#Básicamente é como se a variável "veri" guardasse suas keys e tokens para validá-las quando for chamada pela API.
tweet=tweepy.API(veri)

#E é basicamente isso, para postar algo no twitter basta você colocar este comando e pronto.
tweet.update_status(printdolar)

#Neste caso eu estou postando a variavel "printdolar", mas você pode postar uma frase também, basta apenas deixá-la entre "aspas"

#------------------------------------------------Obrigado----------------------------------------
#Espero ter conseguido te ensinar algo, se precisar de alguma ajuda que esteja ao meu alcance me chame no discord.
#eduard#8394

#Caso você não me ache no discord ou prefira, comente aqui e eu irei lhe responder.Valeu! 

