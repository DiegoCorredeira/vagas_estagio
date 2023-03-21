# Documentação do Projeto - Estágios de TI no LinkedIn

## Introdução
Este projeto tem como objetivo capturar informações sobre vagas de estágio na área de Tecnologia da Informação (TI) no LinkedIn, tais como título da vaga, empresa contratante, local da vaga e descrição da vaga. A partir dessas informações, serão gerados dois arquivos de saída: um arquivo de texto com as descrições das vagas e um arquivo Excel com todas as informações coletadas.

## Instalação
Para executar o código, é necessário ter o Python e algumas bibliotecas instaladas. As bibliotecas necessárias são:

    selenium
    webdriver_manager
    pandas

Essas bibliotecas podem ser instaladas usando o gerenciador de pacotes pip. Para instalar as bibliotecas, basta executar o seguinte comando no terminal:

    pip install selenium webdriver_manager pandas

Além disso, o código utiliza o driver do Chrome para o Selenium, que pode ser instalado automaticamente usando o webdriver_manager. Certifique-se de que o Chrome também esteja instalado no seu sistema.
## Como Usar
O código deve ser executado a partir da linha de comando. Para executar o código, basta navegar até o diretório em que o arquivo Python foi salvo e executar o seguinte comando:

    python nome_do_arquivo.py

## Funcionamento

O código começa importando as bibliotecas necessárias: selenium, webdriver_manager, time e pandas.

Em seguida, é definido o URL da página de busca do LinkedIn. Esse URL é usado para acessar a página usando o driver do Selenium.

Depois que a página é carregada, o código começa a extrair informações das vagas disponíveis. Para cada vaga, o código clica na vaga, aguarda alguns segundos e extrai as informações de interesse, que são o título da vaga, empresa contratante, local da vaga e descrição da vaga.

O código faz isso para todas as vagas disponíveis na página de busca atual. Quando todas as vagas foram processadas, o código verifica se há mais vagas para serem processadas, se hover, repete o passo acima. Se não houver, adiciona as vagas em um arquivo Excel

## Parâmetros

    URL_LINKEDIN: A URL do LinkedIn para pesquisar as vagas desejadas.

## Saída
 1- vagas.xlsx: Um arquivo .xlsx contendo informações de vagas de emprego, incluindo título da vaga, empresa, local e descrição da vaga.
 2- descricao_vagas.txt: Um arquivo .txt contendo as descrições de todas as vagas de emprego extraídas.

## Limitações

    O script pode ser interrompido se ocorrerem erros na extração de informações de alguma vaga de emprego.
    O script pode demorar para ser executado, dependendo do número de vagas de emprego disponíveis na pesquisa.

Espero que esta documentação seja útil para você. Se você tiver alguma dúvida ou precisar de mais ajuda, sinta-se à vontade para perguntar.


<table>
    <h4>Contribuidor</h4>
  <tr>
    <td align="center"><a href="https://github.com/jpdutraa"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/91329576?v=4" width="100px;" alt=""/><br /><sub><b>João Pedro Dutra</b></sub></a><br/>👨🏻‍💻</a></td>
    </tr>
