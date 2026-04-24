import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("gastos.csv")

# Estatísticas básicas
print("=" * 35)
print("       RESUMO DE GASTOS DO MÊS")
print("=" * 35)
print(f"Total gasto:   R$ {df['valor'].sum():.2f}")
print(f"Gasto médio:   R$ {df['valor'].mean():.2f}")
print(f"Gasto mínimo:  R$ {df['valor'].min():.2f}")
print(f"Gasto máximo:  R$ {df['valor'].max():.2f}")
print("-" * 35)

# Categoria com maior e menor gasto
categoria_maior = df.loc[df['valor'].idxmax(), 'categoria']
categoria_menor = df.loc[df['valor'].idxmin(), 'categoria']
print(f"Maior gasto:   {categoria_maior} (R$ {df['valor'].max():.2f})")
print(f"Menor gasto:   {categoria_menor} (R$ {df['valor'].min():.2f})")
print("=" * 35)

# Porcentagem de cada categoria
df['percentual'] = (df['valor'] / df['valor'].sum() * 100).round(1)
print("\nGastos por categoria:")
for _, linha in df.iterrows():
    print(f"  {linha['categoria']:<15} R$ {linha['valor']:>6.2f}  ({linha['percentual']}%)")

# Gráfico de barras 
resumo = df.groupby("categoria")["valor"].sum().sort_values(ascending=False)

cores = ["#2196F3", "#4CAF50", "#FF9800", "#E91E63", "#9C27B0", "#00BCD4", "#FF5722"]

fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(resumo.index, resumo.values, color=cores[:len(resumo)])


for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 10,
        f"R$ {altura:.0f}",
        ha="center", va="bottom", fontsize=10, fontweight="bold"
    )

ax.set_title("Gastos por Categoria", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Categoria", fontsize=11)
ax.set_ylabel("Valor (R$)", fontsize=11)
ax.set_ylim(0, resumo.max() * 1.2)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("grafico.png", dpi=150)
plt.show()
print("\nGráfico salvo como 'grafico.png'")