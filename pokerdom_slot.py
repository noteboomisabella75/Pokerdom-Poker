# Простой демо-слот для Покердом
import random

print("Добро пожаловать в демо-слот от Покердом!")
balance = 1000
while balance > 0:
    bet = 10
    balance -= bet
    spin = random.choice(["WIN", "LOSE"])
    if spin == "WIN":
        balance += 50
        print("Победа! Твой баланс:", balance)
    else:
        print("Проигрыш. Твой баланс:", balance)
    play_again = input("Крутить ещё? (да/нет): ")
    if play_again.lower() != "да":
        break
print("Игра окончена. Итоговый баланс:", balance)
