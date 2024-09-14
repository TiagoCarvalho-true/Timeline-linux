import matplotlib.pyplot as plt

# Dados das distribuições e suas datas de lançamento
distribuicoes = ["Debian", "Slackware", "Red Hat"]
datas_lancamento = ["1993-08-16", "1993-07-17", "1994-11-03"]

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(datas_lancamento, distribuicoes, marker="o", color="b", linestyle="--")
plt.xlabel("Data de Lançamento")
plt.ylabel("Distribuição Linux")
plt.title("Linux Distribution Timeline", fontsize=16, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.5)

# Rotacionar os rótulos do eixo x (opcional)
plt.xticks(rotation=45)

# Adicionar anotações com as versões (opcional)
for i, distro in enumerate(distribuicoes):
    plt.annotate(f"{distro} ({datas_lancamento[i]})", xy=(datas_lancamento[i], distro), xytext=(10, 5), textcoords="offset points", fontsize=10)

# Salvar o gráfico em um arquivo (opcional)
plt.savefig("linux_timeline.png", dpi=300, bbox_inches="tight")

# Mostrar o gráfico na tela
plt.show()
