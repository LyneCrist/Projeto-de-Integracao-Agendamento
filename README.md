## Sobre
***Projeto de Integração e Agendamento*** é um *code camp* que aprensenta uma estrutura básica de operações **CRUD - Create (criar), Read (ler), Update (atualizar) e Delete (apagar)**. O core operacional é baseado na inclusão de registro para paciente e agendamento de transporte.

O projeto é desenvolvido na linguagem [**Python 3.12.2**](https://www.python.org/downloads/release/python-3122/),  framework [**Django 5.0.4**](https://docs.djangoproject.com/en/5.0/releases/5.0.4/) e banco de dados [**SQLite**](https://www.sqlite.org/)

## Instalação
Necessário antes clonar o repo para um diretório local de sua escolha. O script abaixo pode ser executado usando um terminal **powershell** ou vinculado o terminal do VSCode usando o próprio **powershell**. *Todo o script deverá ser executado para a criação e execução do ambiente no primeiro acesso a aplicação* O suporte mencionado estende apenas para ambiente operacional Windows. Aquele que for atuar deverá ter o conhecimento mínimo de terminal e linguagem Python.

Criando ambiente virtual
```powershell
python -m venv .venv
```
Ativando ambiente virtual
```powershell
.\.venv\Scripts\activate
```
Instalando dependências usando arquivo de *requirements*
```powershell
pip install -r requirements.txt
```
Verificando a instalação do Django
```powershell
python -m django --version
```
Executando migrate para acesso a base de dados em **SQLite**
```powershell
python manage.py migrate
```
Executa o serviço Django para acesso ao site
```powershell
python manage.py runserver
```

## Execução
A execução abaixo se faz necessária para o funcionamento do site, todo o processo é baseado no serviço Django.

Ativando ambiente
```powershell
.\.venv\Scripts\activate 
```
Baixando atualizações
```powershell
git pull
```
Atualizando estrutura da base de dados
```powershell
python manage.py migrate
```
Executando o serviço Django
```powershell
python manage.py runserver
```

## Modelo de negócio

### Transporte

Sempre que um transporte for solicitado para um paciente, a mesma página que comporta o formulário de transporte deve também contemplar o formulário de condição do paciente, garantindo que o pedido de transporte seja exclusivo aquela condição.
