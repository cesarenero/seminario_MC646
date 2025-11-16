# Demonstrações Práticas: Cypress e Pytest + Cobertura

Este repositório contém dois exemplos curtos para demonstrar automação de testes:

- Testes end-to-end com Cypress  
- Testes unitários com Pytest  
- Relatórios de cobertura de código em HTML

---

# 1. Demonstração – Cypress (E2E)

## Objetivo
Mostrar um fluxo básico de testes end-to-end utilizando o Cypress, executando no Test Runner e exibindo o passo a passo dos testes.

---

## Como executar

### Instalar dependências
```bash
npm install
```

### Abrir o Cypress
```bash
npx cypress open
```

Selecione:
- E2E Testing  
- Um navegador  
- Start E2E Testing

---

## Estrutura do exemplo

```
cypress/
  e2e/
    demo.cy.js
```

---
---


# 2. Demonstração – Pytest + Cobertura

## Objetivo
Demonstrar testes unitários em Python e geração de relatórios de cobertura.

---

## Estrutura do projeto

```
demo-pytest/
  calculadora.py
  test_calculadora.py
```
---

## Instalação das dependências

```bash
pip install pytest pytest-cov
```

ou no Windows:

```powershell
py -m pip install pytest pytest-cov
```

---

## Rodar os testes

```bash
pytest
```

ou:

```powershell
py -m pytest
```

---

## Gerar relatório de cobertura no terminal

```bash
pytest --cov=calculadora --cov-report=term-missing
```

---

## Gerar relatório de cobertura em HTML

```bash
pytest --cov=calculadora --cov-report=html
```

Isso criará a pasta:

```
htmlcov/
  index.html
```

Para abrir no Windows:

```powershell
start htmlcov/index.html
```


---
