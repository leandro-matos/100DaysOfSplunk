
### Criação e Uso de Macros

**Descrever macros
**Gerenciar macros
**Crie uma macro básica
**Use uma macro básica
**Definir argumentos/variáveis ​​para uma macro
**Adicione e use argumentos com uma macro


### Overview sobre as Macros
**Útil quando você executa pesquisas ou relatórios com frequência com sintaxe de pesquisa semelhante
**O intervalo de tempo é selecionado no momento da pesquisa
**As macros podem ser uma string de pesquisa completa ou uma parte de uma pesquisa que pode ser reutilizada em vários lugares
**Permite que você defina um ou mais argumentos dentro do segmento de pesquisa
   - Passe os valores dos parâmetros para a macro em tempo de execução
   - A macro usa valores para resolver a string de pesquisa


### Criando uma Macro
**Settings -> Advanced search -> Search Macros
    1.	Click New Search Macro
    2.	Select the destination app
    3.	Enter a name
    4.	Type the search string
    5.	Save
**Obs: Teste sua string de pesquisa antes de salvar sua macro. 
**Você pode verificar o conteúdo de sua macro com atalhos de teclado (Command-Shift-E no Mac OS ou Control-Shift-E no Linux ou Windows) na barra de pesquisa na página de pesquisa.


### Utilizando a Macro
**Digite o nome da macro na barra de pesquisa
**Cerque o nome da macro com o caractere de crase (ou acento grave)
    - `macroname` != ‘macroname’
    - Não confunda com aspas simples (‘)
**Pipe para mais comandos ou preceda com string de pesquisa


### Adicionando Argumentos
**Inclui o número de argumentos entre parênteses após o nome da macro
    - vendas_mensais(3)
**Dentro da definição de pesquisa, use $arg$
    - moeda=$moeda$
    - simbolo=$simbolo$
    - taxa=$taxa$
**No campo Argumentos, insira o nome do(s) argumento(s)
**Fornece uma ou mais variáveis ​​da macro no momento da pesquisa

### Utilizando Argumentos
**Ao usar uma macro com argumentos, inclua o(s) argumento(s) entre parênteses após o nome da macro
**Certifique-se de passar os argumentos na mesma ordem em que os definiu
    **Query de Exemplo: sourcetype=vendor_sales VendorCountry=Germany | `monthly_sales(euro,€,0.79)`**

### Validação de Macros
**Você pode validar valores de argumento em sua macro
**Validation Expression: você pode inserir uma expressão para cada argumento
    - O argumento deve ser colocado entre cifrões
**Validation Error Message: mensagem que aparece quando você executa a macro
    **Obs: Não crie macros com barras verticais: alguém pode colocar uma barra vertical na frente da macro ao usá-la na string de pesquisa real.**