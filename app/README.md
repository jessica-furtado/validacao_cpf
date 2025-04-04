# 🧪 Validador de CPF em Python

Este projeto implementa uma função para validação de CPF brasileiro (Cadastro de Pessoa Física) com base nas regras dos dígitos verificadores, além de uma suíte de testes automatizados com **pytest**.

---

## 📁 Estrutura do Projeto

```
validacao_cpf/
├── app/
│   └── validacao.py           # Função principal de validação de CPF
│   └── test_validacao.py      # Testes automatizados com pytest
└── README.md                  # Instruções e explicações do projeto
```

---

## 🚀 Como executar os testes

1. **Clone ou baixe o projeto** em sua máquina.

2. No terminal, acesse a pasta do projeto:
```bash
cd validacao_cpf
```

3. Instale o `pytest`, caso ainda não tenha:
```bash
pip install pytest
```

4. Execute os testes com:
```bash
python -m pytest
```

Você verá algo como:
```
====== test session starts ======
collected 6 items

tests/test_validacao.py ......    [100%]

====== 6 passed in 0.06s ======
```

---

## 🔍 Sobre a função `validar_cpf`

A função `validar_cpf(cpf: str) -> bool`:

✔️ Remove todos os caracteres que **não são números**  
✔️ Verifica se o CPF tem **11 dígitos**  
✔️ Rejeita CPFs com **todos os dígitos iguais**  
✔️ Calcula os **dois dígitos verificadores** e compara com os fornecidos

### Exemplo:
```python
validar_cpf("529.982.247-25")  # Retorna: True
validar_cpf("111.111.111-11")  # Retorna: False
```

---

## ✅ Casos testados

Os testes cobrem os seguintes cenários:

- CPF válido
- CPF com dígitos verificadores incorretos
- CPF com todos os números iguais
- CPF com letras misturadas
- CPF com menos de 11 dígitos
- CPF vazio

---

## 💡 Tecnologias utilizadas

- Python 3.11+
- Pytest 8.x

---

## 📌 Autor(a)

Projeto criado por **Jéssica Furtado** 


