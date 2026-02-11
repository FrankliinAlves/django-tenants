### Django Multi-Tenant SaaS Platform
Base inicial arquitetural para aplicações SaaS utilizando **Django**, **PostgreSQL** e **django-tenants**, com isolamento de dados por schema e provisionamento automatizado de novos clientes.

---
### Visão Geral

Este projeto implementa uma arquitetura **Multi-Tenant Database-Isolated**, onde cada empresa (tenant) possui seu próprio **schema isolado dentro do PostgreSQL**.

Diferente de modelos onde os dados são compartilhados em uma única estrutura lógica, aqui cada tenant possui:

- Suas próprias tabelas
- Seus próprios usuários
- Seu próprio contexto de autenticação
- Isolamento físico e lógico no banco

O objetivo é fornecer uma base sólida para aplicações SaaS privadas, com foco em segurança, organização e escalabilidade.

---
### Arquitetura da Solução

#### 1. Isolamento por Schema (PostgreSQL)

Cada tenant possui um schema dedicado no banco de dados.  
Isso garante:

- Separação real de dados entre empresas
- Redução de riscos de vazamento entre tenants
- Melhor organização estrutural
- Facilidade para backup ou manutenção individual

#### 2. Provisionamento Automatizado

A criação de um novo tenant ocorre de forma automática utilizando:

- Django Signals
- Transações sincronizadas com o banco

Fluxo ao cadastrar um novo cliente:

1. Criação do schema
2. Execução das migrations no novo schema
3. Criação automática de um usuário Master exclusivo

Esse processo elimina etapas manuais e reduz erros operacionais.

#### 3. Modelo de Segurança (Private SaaS)

A aplicação foi projetada como uma plataforma SaaS privada:

- Todas as rotas protegidas por autenticação
- Acesso apenas para usuários previamente criados
- Redirecionamento automático para login em caso de acesso não autenticado
- Gestão de usuários realizada pelo Master do tenant ou administrador global

#### 4. Gestão de Domínios Dinâmicos

O sistema identifica automaticamente o tenant a partir do domínio ou subdomínio.

---
#### 5. Guia de Instalação Rápida e configuração do Ambiente

1. Clone o repositório
```bash
git clone https://github.com/FrankliinAlves/django-tenants.git
```
2. Crie ambiente Virtual
```bash
python -m venv venv
```
3. Ative ambiente
```bash
# Windows
venv\Scripts\activate
```
```bash
# Linux/Mac
source venv/bin/activate
```
4. Instale dependências
```bash
# Atualizar pip
pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt
```
5. Variáveis de Ambiente e Infraestrutura<br/>
> Renomeie o arquivo .env.example para .env e inicie o banco de dados via Docker:
```bash
docker compose up -d
```
6. Aplique migrações
```bash
python manage.py makemigrations
python manage.py migrate_schemas --shared
```
7. Configure o domínio public<br/>
> Acesse o shell do Django para criar o tenant gestor:
```bash
python manage.py shell
```
```bash
# No shell >>>
tenant = Client(schema_name="public", name="Administração")
tenant.save()

domain = Domain()
domain.domain = "localhost"
domain.tenant = tenant
domain.is_primary = True
domain.save()
quit()
```
8. Crie seu superusuário
```bash
python manage.py createsuperuser
```
> Rode o servidor
```bash
python manage.py runserver
```
> Em http://localhost:8000/ já está disponível a tela de login da a aplicação
9. Criar primeiro cliente<br/>
- No acesso gerenciador em http://localhost:8000/admin/ entre com suas credenciais e adicione um novo tenant.<br/>
Exemplo:<br/>

  * schema name: empresa1
  * name: Primeiro Cliente
  * domain: empresa1.localhost
  
O sistema criará o esquema e o usuário Master automaticamente para o seu novo cliente.<br/>
- A Credencial de acesso padrão do usuário master está definida no signals.py:<br/>

  usuário: admin-empresa1<br/>
  senha: senha102030<br/>

Acesse em: http://empresa1.localhost:8000/

Ao realizar o login, o usuário acessa exclusivamente o ambiente do seu tenant, visualizando apenas os dados pertencentes à sua organização. 
A partir dessa base, é possível evoluir o sistema com novos templates, views, módulos e regras de negócio específicas para cada contexto empresarial.

---
#### Referência
Documentação oficial do django-tenants > https://django-tenants.readthedocs.io/en/latest/install.html













