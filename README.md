# 🔁 Loops em Programação: `for` e `while`

> Um guia rápido e prático sobre as estruturas de repetição mais usadas na programação!

---

## 📋 Índice

- [O que são loops?](#-o-que-são-loops)
- [Loop for](#-loop-for)
- [Loop while](#-loop-while)
- [Quando usar cada um?](#-quando-usar-cada-um)
- [Comparação rápida](#-comparação-rápida)

---

## 🤔 O que são loops?

Loops (ou laços de repetição) são estruturas que permitem **executar um bloco de código várias vezes**, evitando repetição desnecessária. São fundamentais em qualquer linguagem de programação!

---

## 🔢 Loop `for`

O `for` é usado quando você **sabe de antemão quantas vezes** quer repetir algo.

### Sintaxe geral
```python
for variavel in sequencia:
    # bloco de código
```

### Exemplo em Python 🐍
```python
for i in range(5):
    print(f"Iteração número {i}")

# Saída:
# Iteração número 0
# Iteração número 1
# Iteração número 2
# Iteração número 3
# Iteração número 4
```

### Exemplo em JavaScript 🌐
```javascript
for (let i = 0; i < 5; i++) {
    console.log(`Iteração número ${i}`);
}
```

### ✅ Use `for` quando:
- Souber o número exato de repetições
- Quiser percorrer listas, arrays ou coleções
- Precisar de um contador bem definido

---

## 🔄 Loop `while`

O `while` repete um bloco de código **enquanto uma condição for verdadeira**. Ideal quando não se sabe exatamente quantas iterações serão necessárias.

### Sintaxe geral
```python
while condicao:
    # bloco de código
```

### Exemplo em Python 🐍
```python
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Saída:
# Contador: 0
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
```

### Exemplo em JavaScript 🌐
```javascript
let contador = 0;

while (contador < 5) {
    console.log(`Contador: ${contador}`);
    contador++;
}
```

### ✅ Use `while` quando:
- Não souber quantas repetições serão necessárias
- Quiser repetir até que uma condição mude
- Trabalhar com entradas do usuário ou eventos externos

---

## ⚠️ Cuidado com loops infinitos!

Um erro comum é criar um loop que **nunca termina**. Sempre garanta que a condição de parada será atingida!

```python
# ❌ Loop infinito — EVITE!
while True:
    print("Isso nunca para!")

# ✅ Com condição de saída
while True:
    entrada = input("Digite 'sair' para encerrar: ")
    if entrada == "sair":
        break  # Interrompe o loop
```

---

## 🆚 Quando usar cada um?

| Situação | Recomendado |
|---|---|
| Percorrer uma lista | 🔢 `for` |
| Número fixo de repetições | 🔢 `for` |
| Condição dinâmica | 🔄 `while` |
| Aguardar entrada do usuário | 🔄 `while` |
| Iterar sobre dicionários/mapas | 🔢 `for` |
| Repetir até evento ocorrer | 🔄 `while` |

---

## 📊 Comparação rápida

```
FOR                          WHILE
───────────────────          ─────────────────────
✔ Nº de iterações fixo       ✔ Condição variável
✔ Mais legível               ✔ Mais flexível
✔ Menos propenso a bug       ⚠ Risco de loop infinito
✔ Ideal para coleções        ✔ Ideal para eventos
```

---

## 🚀 Conclusão

Tanto o `for` quanto o `while` são poderosos — escolher o certo torna o código mais **limpo**, **eficiente** e **fácil de entender**. 💡

> 💬 *"Todo bom programador sabe quando usar cada ferramenta."*

---

## 📚 Referências

- [Python Docs — Loops](https://docs.python.org/3/tutorial/controlflow.html)
- [MDN Web Docs — JavaScript Loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)

---

⭐ **Gostou? Deixe uma estrela no repositório!**
