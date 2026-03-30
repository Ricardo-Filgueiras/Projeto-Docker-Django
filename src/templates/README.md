# Estrutura de Templates - Projeto Lista

## 📁 Organização de Templates

```
src/templates/
├── base.html              # Template base principal
├── index.html             # Página inicial
├── partials/
│   ├── _header.html       # (Futuro) Header reutilizável
│   ├── _footer.html       # (Futuro) Footer reutilizável
│   └── _navbar.html       # (Futuro) Navbar reutilizável
└── app/
    └── ...                # (Futuro) Templates de apps específicos
```

## 📄 Herança de Templates

### base.html
- Template pai principal
- Contém estrutura HTML global
- Define blocos para estender em outras templates
- Importa CSS e JS estáticos

**Blocos disponíveis:**
```django
{% block title %}       # Título da página (SEO)
{% block extra_css %}   # CSS adicional por página
{% block content %}     # Conteúdo principal
```

### index.html
- Estende `base.html`
- Define title customizado
- Contém todo o conteúdo da página inicial
- Estruturado em seções semânticas

## 🎯 Boas Práticas Django

### Template Organization
- ✅ Usar herança de templates com `{% extends %}`
- ✅ Separar componentes em `{% include %}`
- ✅ Usar `{% load static %}` no início
- ✅ Sempre adicionar `alt` em imagens
- ✅ Usar `{% url %}` tag para URLs

### Static Files
- ✅ Todas as CSS e JS em `static/`
- ✅ Usar `{% static %}` para referenciar
- ✅ Organizar por tipo (css/, js/, images/)
- ✅ Minificar em produção

### URLs e Routing
- Template utiliza links internos (seções com #)
- Uso de âncoras para navegação
- Links de nav pontuam seções pelo `id`

## 🔐 Segurança em Templates

### Auto-escaping
```django
{{ variable }}              # Auto escapado (seguro vs XSS)
{{ variable|safe }}         # Não escapado (use com cuidado)
```

### CSRF Protection
```django
{% csrf_token %}  # Em forms POST/PUT/DELETE
```

### Template Context
- Não incluir dados sensíveis no contexto
- Validar dados no backend
- Sanitizar entrada de usuário

## 🚀 Estrutura por Seção

Cada seção da página é uma `<section>` com `id` único:
- `#features` - Funcionalidades
- `#tech` - Stack Tecnológico
- `#cta` - Call to Action
- etc.

Permite:
- Navegação interna via hash
- Scroll suave com JS
- SEO friendly

## 📱 Responsive Design

- Mobile-first approach
- Tailwind classes para responsivo
- Breakpoints: mobile, tablet, desktop
- Testar em DevTools (F12)

## ♿ Acessibilidade

- Semantic HTML (`<header>`, `<nav>`, `<main>`, `<footer>`)
- `lang="pt-BR"` no `<html>`
- Meta viewport configurada
- Links com texto descritivo
- Botões com aria-labels quando necessário

## 🎨 Customização Visual

### Adicionar nova seção
1. Criar `<section id="nova-secao">` em index.html
2. (Opcional) Adicionar link no nav
3. Usar classes de design-system.css
4. Testar responsivo

### Modificar estilos
1. Editar em `static/css/design-system.css`
2. Usar variáveis CSS quando possível
3. Manter convenção de nomenclatura
4. Documentar mudanças

## 🔄 Fluxo de Desenvolvimento

```
1. Criar HTML semântico em template
↓
2. Aplicar classes de design-system.css
↓
3. Verificar layout com browser
↓
4. Testar em mobile (DevTools)
↓
5. Validar acessibilidade (axe, WAVE)
↓
6. Commitar mudanças
```

## 🧪 Testes Úteis

- **Responsivo**: F12 → Device Toolbar
- **Acessibilidade**: axe DevTools Extension
- **Performance**: Lighthouse (F12)
- **SEO**: Google Mobile-Friendly Test
- **Validação**: W3C Markup Validator

## 📚 Referências

- [Django Templates](https://docs.djangoproject.com/en/6.0/topics/templates/)
- [Django Static Files](https://docs.djangoproject.com/en/6.0/howto/static-files/)
- [Template Inheritance](https://docs.djangoproject.com/en/6.0/topics/templates/#template-inheritance)
- [OWASP Template Security](https://owasp.org/www-community/attacks/xss/)
