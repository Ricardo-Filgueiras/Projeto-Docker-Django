# Estrutura de Arquivos Estáticos - Projeto Lista

## 📁 Organização de Arquivos

```
src/
├── static/
│   ├── css/
│   │   ├── design-system.css      # Design tokens, componentes base, utilidades
│   │   └── layout.css             # Layouts, grids, typography, responsive
│   ├── js/
│   │   └── main.js                # Interatividade, smooth scroll, acessibilidade
│   └── images/                    # Imagens (favicon, logos, etc)
│
└── templates/
    ├── base.html                   # Template base com imports de CSS/JS
    ├── index.html                  # Página inicial (extends base)
    └── partials/                   # Componentes reutilizáveis
        ├── _header.html
        └── ...
```

## 📄 Descrição dos Arquivos

### `design-system.css`
- **Propósito**: Componentes reutilizáveis e design tokens
- **Contém**:
  - Variáveis CSS (cores, espaçamento, tipografia)
  - Componentes base (buttons, badges, inputs)
  - Utilidades e classes genéricas
  - Estilos de navegação, cards, ícones

### `layout.css`
- **Propósito**: Layouts responsivos e tipografia
- **Contém**:
  - Grid system utilities
  - Flexbox utilities
  - Responsive breakpoints
  - Typography scales
  - Spacing system

### `main.js`
- **Propósito**: Interatividade e funcionalidades
- **Contém**:
  - Smooth scrolling
  - Navigation active state
  - Button interactions (ripple effect)
  - Keyboard navigation (acessibilidade)
  - Performance utilities (throttle, debounce)
  - Lazy loading

## 🔄 Como Adicionar Novos Estilos/Scripts

### Adicionar novo componente CSS
1. Adicionar classe em `design-system.css` se for um componente reutilizável
2. Ou adicionar em `layout.css` se for específico de layout
3. Nomear com convenção BEM quando apropriado

### Adicionar nova funcionalidade JavaScript
1. Criar nova função em `main.js`
2. Chamar a função dentro de `init()`
3. Adicionar documentação comentada

## 🌐 Importação em Templates

```html
{% load static %}

<!-- CSS -->
<link rel="stylesheet" href="{% static 'css/design-system.css' %}">
<link rel="stylesheet" href="{% static 'css/layout.css' %}">

<!-- JavaScript -->
<script src="{% static 'js/main.js' %}"></script>
```

## 📱 Responsive Breakpoints

- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

## ♿ Acessibilidade

- Todos os componentes suportam keyboard navigation
- Focus states visíveis em botões
- ARIA labels onde necessário
- Respeita `prefers-reduced-motion`
- Contraste de cores WCAG AA compliant

## 🚀 Performance

- CSS dividido logicamente para melhor manutenção
- JavaScript modular com IIFE
- Usa throttle/debounce para scroll events
- Lazy loading images support
- Estilos críticos inline (considerar no futuro)

## 🔐 Segurança

- Não há segredos em arquivos estáticos
- Todos os dados sensíveis ficam no backend
- JavaScript segue content security policy
- Sem eval() ou dynamic script injection

## 🔄 Manutenção Futura

- **Adicionar CSS**: Manter organização BEM
- **Adicionar funções JS**: Documentar bem com JSDoc
- **Atualizar design**: Definir novos tokens em `:root`
- **Testar responsivo**: Verificar em 3 breakpoints mínimo
