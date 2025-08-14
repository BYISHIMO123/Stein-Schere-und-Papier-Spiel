"""Stein,Schere und Papier Spiel"""
import random

Wähle_zwischen=["Stein","Schere","Papier"]
while True: 
    Spieler1 = input("Wähle Stein, Schere oder Papier oder q as Quit: ")
    if Spieler1=="q":
        print("Spiel beendet.")
        break
    if Spieler1 not in Wähle_zwischen:
        print("Unglutigr Eingabe, versuche es erneut.")
        continue

    Spieler2_computer=random.choice(Wähle_zwischen)
    print(f"Spieler1:{Spieler1} und Spieler2_Computer:{Spieler2_computer}")

    if Spieler1==Spieler2_computer:
       print("niemand hat gewinnt, versuche erneut!!")
    elif (Spieler1=="Stein" and Spieler2_computer=="Sphere") or \
        (Spieler1=="Schere"and Spieler2_computer=="Papier") or \
        (Spieler1=="Papier" and Spieler2_computer=="Stein"):
       print("Spieler1 hat gewinnt")
    else:
       print("Spieler2_Computer hat gewinnt")
