# 📋 Projeto Lista - Plataforma de Gerenciamento Operacional

[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-FFA500?style=flat-square)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 📖 Visão Geral

**Projeto Lista** é uma plataforma web moderna de gerenciamento operacional construída com **Django 6.0**, containerizada com **Docker** e otimizada com **UV**. Combina robustez enterprise com simplicidade de uso para equipes que precisam organizar, rastrear e executar listas de tarefas com eficiência.

### 🎯 Objetivo Principal

Fornecer uma solução production-ready que demonstra:
- ✅ **Arquitetura Django escalável** - Seguindo melhores práticas
- ✅ **Containerização moderna** - Docker e Docker Compose
- ✅ **Performance otimizada** - UV para gerenciamento de dependencies
- ✅ **Segurança em primeiro lugar** - OWASP Top 10, HTTPS, CSRF protection
- ✅ **Código profissional** - Bem estruturado, testável e documentado

---

## 🚀 Aplicações & Funcionalidades

### Core Features

#### 👥 **Gerenciamento de Usuários**
- Sistema de autenticação seguro com hashing PBKDF2
- Registro de novos usuários com validação rigorosa
- Perfis de usuário customizáveis
- Controle de sessão com timeout
- Rate limiting em login para prevenção de brute force

#### 📊 **Dashboard Principal**
- Visão geral consolidada de todas as listas
- Estatísticas em tempo real
- Interface intuitiva e responsiva
- Acesso rápido a recursos mais usados

#### 🛡️ **Painel de Administração**
- Admin Django nativo e poderoso
- Gerenciamento de usuários e permissões
- Auditoria de atividades
- Controle granular de acesso (RBAC)

#### 📱 **Design Responsivo**
- Mobile-first approach
- Funciona em desktop, tablet e mobile
- Performance otimizada
- Sem dependências desnecessárias

#### 🔐 **Segurança Avançada**
- Autenticação robusta
- Proteção CSRF em todos os formulários
- Criptografia TLS/HTTPS
- XSS prevention com auto-escaping
- SQL Injection prevention via ORM
- HSTS headers habilitados

---

## 🏗️ Arquitetura

### Arquitetura em Camadas

```
┌─────────────────────────────────────────┐
│         Frontend Layer                   │
│  HTML5 + CSS3 + Tailwind + JavaScript   │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Django Application Layer            │
│  ├─ URL Routing (core/urls.py)          │
│  ├─ Views (app/*/views.py)              │
│  ├─ Models (app/*/models.py)            │
│  ├─ Forms (app/*/forms.py)              │
│  └─ Middleware & Signals                │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Business Logic & Services           │
│  ├─ Authentication                      │
│  ├─ Authorization                       │
│  ├─ Data Validation                     │
│  └─ Business Rules                      │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Database Layer                      │
│  ├─ Django ORM                          │
│  ├─ Migrations                          │
│  └─ PostgreSQL (Prod) / SQLite (Dev)    │
└─────────────────────────────────────────┘
```

### Estrutura de Diretórios

```
Projeto-Docker-Django/
├── src/                           # Código-fonte princi pal
│   ├── manage.py                  # Django CLI
│   ├── core/                      # Configuração central
│   │   ├── settings.py            # Configurações por ambiente
│   │   ├── urls.py                # URL routing
│   │   ├── wsgi.py                # WSGI application
│   │   └── asgi.py                # ASGI application
│   ├── app/                       # Django apps
│   │   ├── user/                  # App de usuários
│   │   │   ├── models.py          # User model, UserProfile
│   │   │   ├── views.py           # Auth views, profile
│   │   │   ├── forms.py           # Login, Register forms
│   │   │   ├── urls.py            # URL patterns
│   │   │   ├── signals.py         # Signal handlers
│   │   │   ├── apps.py            # App config
│   │   │   ├── admin.py           # Admin configuration
│   │   │   ├── tests.py           # Unit tests
│   │   │   ├── migrations/        # DB migrations
│   │   │   └── templates/
│   │   │       ├── login.html
│   │   │       ├── register.html
│   │   │       └── profile.html
│   │   └── home/                  # App principal
│   │       ├── models.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       ├── apps.py
│   │       ├── admin.py
│   │       ├── migrations/
│   │       └── templates/
│   ├── templates/                 # Shared templates
│   │   ├── base.html              # Template base
│   │   ├── index.html             # Página inicial
│   │   └── partials/
│   │       ├── _header.html
│   │       ├── _footer.html
│   │       └── _message.html
│   └── static/                    # Arquivos estáticos
│       ├── css/
│       │   ├── design-system.css  # Design tokens e componentes
│       │   └── layout.css         # Layouts e tipografia
│       ├── js/
│       │   └── main.js            # Interatividade
│       └── images/                # Imagens e ícones
├── scripts/                       # Scripts úteis
│   ├── entrypoint_prod.sh         # Inicialização produção
│   ├── makemigrations.sh
│   ├── migrate.sh
│   ├── collectstatic.sh
│   ├── runserver.sh
│   ├── start_gunicorn.sh
│   └── wait_psql.sh               # Aguardar DB
├── docker-compose.yml             # Orquestração local
├── Dockerfile                     # Imagem do app
├── .python-version                # Python 3.12
├── requirements.txt               # Dependências (pip)
├── pyproject.toml                 # Projeto UV config
├── .env.example                   # Template de .env
├── .gitignore
├── README.md                      # Este arquivo
└── data/                          # Volume persistente (Docker)
    └── web/
        ├── static/                # Collected static files
        └── media/                 # User uploads
```

### Fluxo de Dados

```
   User Request (HTTP/HTTPS)
           │
           ▼
   ┌──────────────────┐
   │   URL Router     │  (core/urls.py)
   └────────┬─────────┘
            │
            ▼
   ┌──────────────────┐
   │  Middleware      │  (Security, CSRF, etc)
   └────────┬─────────┘
            │
            ▼
   ┌──────────────────┐
   │  View Handler    │  (views.py)
   └────────┬─────────┘
            │
            ├─→ ORM Query  ──→  ┌──────────────┐
            │                   │   Database   │
            │                   └──────┬───────┘
            │                          │
            ├─→ Model Processing ◄─────┘
            │
            ├─→ Form Validation
            │
            └─→ Template Rendering
                    │
                    ▼
            ┌──────────────────┐
            │  HTML Response   │
            └──────────────────┘
```

---

## 🛠️ Stack Tecnológico

### Backend
| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| **Django** | 6.0 | Framework web principal |
| **Python** | 3.12 | Linguagem |
| **PostgreSQL** | 15+ | Banco de dados (produção) |
| **SQLite3** | - | Banco de dados (desenvolvimento) |

### DevOps & Deployment
| Tecnologia | Propósito |
|-----------|----------|
| **Docker** | Containerização |
| **Docker Compose** | Orquestração local |
| **Gunicorn** | Servidor WSGI |
| **WhiteNoise** | Servir static files |

### Package Management
| Tecnologia | Propósito |
|-----------|----------|
| **UV** | Gerenciador de packages ultra-rápido |
| **pip** | Alternativa tradicional |

### Frontend & Styling
| Tecnologia | Propósito |
|-----------|----------|
| **HTML5** | Markup semântico |
| **Tailwind CSS** | Utility-first CSS framework |
| **JavaScript (Vanilla)** | Interatividade |
| **Iconify** | Sistema de ícones |

### Security & Performance
| Tecnologia | Propósito |
|-----------|----------|
| **HTTPS/TLS** | Criptografia em trânsito |
| **CSRF Tokens** | Proteção contra CSRF |
| **PBKDF2** | Hashing de senhas |
| **Content Security Policy** | XSS prevention |

---

## 🚀 Como Começar

### Pré-requisitos

- **Python 3.12+** - [Instalar](https://www.python.org/downloads/)
- **Docker & Docker Compose** - [Instalar](https://www.docker.com/products/docker-desktop)
- **UV** - [Instalar](https://github.com/astral-sh/uv#installation) (opcional, alternativa a pip)
- **Git** - [Instalar](https://git-scm.com/)

### Instalação Local (Desenvolvimento)

#### 1. Clone o repositório
```bash
git clone https://github.com/Ricardo-Filgueiras/Projeto-Docker-Django.git
cd Projeto-Docker-Django
```

#### 2. Crie um arquivo `.env`
```bash
cp .env.example .env
# Editar .env com suas configurações
```

#### 3. Instale dependências com UV
```bash
# Instalar UV (se não tiver)
pip install uv

# Instalar dependências
uv sync
```

#### 4. Execute migrações
```bash
uv run python src/manage.py migrate
```

#### 5. Crie um superuser
```bash
uv run python src/manage.py createsuperuser
```

#### 6. Colete arquivos estáticos
```bash
uv run python src/manage.py collectstatic --noinput
```

#### 7. Inicie o servidor
```bash
uv run python src/manage.py runserver
```

Acesse: http://127.0.0.1:8000/

### Com Docker Compose (Recomendado)

#### 1. Build e inicie os containers
```bash
docker-compose up -d
```

#### 2. Crie migrações
```bash
docker-compose exec web python src/manage.py migrate
```

#### 3. Crie superuser
```bash
docker-compose exec web python src/manage.py createsuperuser
```

#### 4. Colete static files
```bash
docker-compose exec web python src/manage.py collectstatic --noinput
```

Acesse: http://localhost

Para parar:
```bash
docker-compose down
```

---

## 📦 Deployment

### Produção com Docker

#### 1. Build da imagem
```bash
docker build -t projeto-lista:latest .
```

#### 2. Push para registro (ECR, DockerHub, etc)
```bash
docker push seu-registry/projeto-lista:latest
```

#### 3. Deploy (exemplo AWS ECS, Heroku, etc)
```bash
# Varia por plataforma
# Ver documentação de seu serviço
```

### Variáveis de Ambiente (Produção)

```env
DEBUG=0
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
SECRET_KEY=sua-chave-secreta-segura-gerada-aleatoramente
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=projeto_lista_prod
POSTGRES_USER=admin_db
POSTGRES_PASSWORD=senha-segura
POSTGRES_HOST=db.c.seu-provider.com
POSTGRES_PORT=5432
SECURE_SSL_REDIRECT=1
SESSION_COOKIE_SECURE=1
CSRF_COOKIE_SECURE=1
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=1
SECURE_HSTS_PRELOAD=1
```

---

## 🔐 Segurança

### Implementações de Segurança

#### ✅ Autenticação
- Hashing de senha com PBKDF2-SHA256
- Rate limiting em endpoints de login
- Session timeout automático
- Login com email ou username

#### ✅ Autorização
- Sistema de permissões granular (Django ORM)
- RBAC (Role-Based Access Control)
- Auditoria de atividades
- Proteção de dados sensíveis

#### ✅ Criptografia
- HTTPS/TLS obrigatório em produção
- HSTS headers habilitados
- Cookies seguros (HttpOnly, Secure, SameSite)
- Secrets em variáveis de ambiente

#### ✅ Proteção contra Ataques Comuns
- **CSRF**: Django middleware + tokens em formulários
- **XSS**: Auto-escaping em templates
- **SQL Injection**: ORM Django previne via parameterization
- **Clickjacking**: X-Frame-Options headers
- **Security Headers**: Content Security Policy, X-Content-Type-Options

#### ✅ Validação
- Validação rigorosa de entrada
- Escape de saída HTML
- Sanitização de dados
- Validadores Django customizados

### OWASP Top 10 Mitigações

| Vulnerabilidade | Mitigação |
|---|---|
| Injection | ORM Django + parameterized queries |
| Broken Auth | PBKDF2, rate limiting, session management |
| Broken Access Control | Permissões granulares, RBAC |
| XML External Entities | Não processamos XML (low risk) |
| Broken Access Control | Middleware de verificação |
| CSRF | Django CSRF middleware + tokens |
| XSS | Auto-escaping em templates |
| Insecure Deserialization | Não usamos pickle/unsafe serialization |
| Using Components with Vulns | Dependency scanning contínuo |
| Insufficient Logging | Audit logging implementado |

### Checklist de Segurança Pré-Deploy

- [ ] `DEBUG=False` em produção
- [ ] `SECRET_KEY` único e seguro
- [ ] `ALLOWED_HOSTS` configurado
- [ ] SSL/TLS certificate válido
- [ ] Database backup automatizado
- [ ] Logs centralizados (Sentry, ELK, etc)
- [ ] WAF (Web Application Firewall) configurado
- [ ] DDoS protection ativo
- [ ] Fail2ban ou similar para rate limiting
- [ ] Secrets em variáveis de ambiente
- [ ] Dependências auditadas e atualizadas

---

## 🧪 Testing

### Rodar Testes
```bash
uv run python src/manage.py test
```

### Coverage
```bash
uv run coverage run --source='.' src/manage.py test
uv run coverage report
```

### Estrutura de Testes
```python
src/app/user/tests.py      # Testes do app user
src/app/home/tests.py      # Testes do app home
```

---

## 📚 Documentação Adicional

- [Django Documentation](https://docs.djangoproject.com/en/6.0/)
- [Docker Guide](https://docs.docker.com/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [OWASP Security](https://owasp.org/)

---

## 🔄 Fluxo de Desenvolvimento

```
1. Branch Feature
   └─ git checkout -b feature/minha-feature

2. Desenvolver (local)
   └─ uv run python src/manage.py runserver

3. Testes
   └─ uv run python src/manage.py test

4. Commit
   └─ git commit -am "feat: descrição clara"

5. Push
   └─ git push origin feature/minha-feature

6. Pull Request
   └─ Revisão de código e CI/CD

7. Merge & Deploy
   └─ Automático via CI/CD
```

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'whitenoise'"
```bash
uv sync
# ou
pip install whitenoise
```

### Erro: "database is locked" (SQLite)
- Feche outras conexões ao banco
- Considere migrar para PostgreSQL

### Erro: "Cannot connect to database"
```bash
# Verificar status do Docker
docker ps

# Verificar logs
docker-compose logs db
```

### Porta já está em uso
```bash
# Mudar porta no runserver
uv run python src/manage.py runserver 0.0.0.0:8001
```

---

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código
- PEP 8 para Python
- Black formatter para formatação
- Flake8 para linting
- isort para ordenação de imports
- Type hints quando possível

---

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---
## Agradecimentos

- Django Community
- Docker Team
- Tailwind CSS
- Todas as dependências open-source

## Roadmap Futuro

- [ ] Suporte a múltiplas línguas (i18n)
- [ ] Notificações em tempo real (WebSockets)
- [ ] API REST com Django REST Framework
- [ ] Integração com Celery para tasks assíncronas
- [ ] Dashboard avançado com Django Charts
- [ ] Integração com OAuth (Google, GitHub)
- [ ] Mobile app (React Native)
- [ ] Monitoring e Analytics

---

**Happy Coding! 🚀**
