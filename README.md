# 📊 Analisador de Gastos Pessoais

Este projeto em **Python** tem como objetivo realizar a **análise de gastos mensais** a partir de um arquivo **CSV** contendo informações sobre despesas pessoais. O script **calcula as estatísticas** e gera um **gráfico de barras** para visualizar os gastos por categoria.

---

## 📌 Funcionalidades

- **Leitura de dados** a partir de um arquivo **CSV** com a biblioteca **pandas**.
- **Cálculo de estatísticas básicas**:
  - Total gasto
  - Gasto médio
  - Gasto mínimo
  - Gasto máximo
- **Identificação da categoria com maior e menor gasto**.
- **Cálculo do percentual de cada categoria** sobre o total.
- **Geração de gráfico de barras** com a biblioteca **matplotlib**, salvo como **imagem**.

---

## 🚀 Como Rodar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/analisador-gastos.git
cd analisador-gastos
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o script**
```bash
python analise.py
```
## 📊 Exemplo de saída

```
===================================
       RESUMO DE GASTOS DO MÊS
===================================
Total gasto:   R$ 1790.00
Gasto médio:   R$ 223.75
Gasto mínimo:  R$ 65.00
Gasto máximo:  R$ 620.00
-----------------------------------
Maior gasto:   Mercado (R$ 620.00)
Menor gasto:   Streaming (R$ 65.00)
===================================

Gastos por categoria:
  Internet        R$ 120.00  (6.7%)
  Energia         R$ 210.00  (11.7%)
  Agua            R$  85.00  (4.7%)
  Mercado         R$ 620.00  (34.6%)
  Academia        R$ 100.00  (5.6%)
  Faculdade       R$ 450.00  (25.1%)
  Streaming       R$  65.00  (3.6%)
  Farmacia        R$ 140.00  (7.8%)
```


## 🛠️ Tecnologias

- Python 3
- pandas
- matplotlib

## 📝 Como Personalizar

Para personalizar o script, basta seguir as instruções abaixo:

1. **Altere o arquivo `gastos.csv`** com suas próprias categorias e valores.
2. O script se adapta automaticamente a qualquer número de linhas, desde que o arquivo siga a mesma estrutura:
   - **Colunas**: `categoria`, `valor`.
3. **Rodando o script novamente**, ele recalculará as estatísticas e gerará um novo gráfico.

---

## 🤝 Como Contribuir

Se você gostaria de contribuir para o projeto, siga as etapas abaixo:

1. **Fork** este repositório.
2. **Crie uma nova branch**: 
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. **Faça suas alterações e commit**:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. **Push para a branch**
  ```bash
   git push origin feature/nova-funcionalidade
   ```
5. ** Abra um Pull Request explicando as alterações feitas. **

  
