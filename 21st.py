def CardValues(card):
    arr = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    return arr.index(card)


file = open("input.txt")

myCount, enemyCount, trump = file.readline().split()
myCount = int(myCount)
enemyCount = int(enemyCount)
myCards = file.readline().split()
enemyCards = file.readline().split()

myCardsSuit = {"S": [], "C": [], "D": [], "H": []}
enemyCardsSuit = {"S": [], "C": [], "D": [], "H": []}
#создаем массивы, в которых для каждой масти будут записанны карты, которые есть в наборах
for card in myCards:
    myCardsSuit[card[1]].append(card[0])
for card in enemyCards:
    enemyCardsSuit[card[1]].append(card[0])
#сортируем карты по их старшинству
cardSuit = ["S", "C", "D", "H"]
for suit in cardSuit:
    myCardsSuit[suit] = sorted(myCardsSuit[suit], key=lambda x: CardValues(x))
    enemyCardsSuit[suit] = sorted(enemyCardsSuit[suit], key=lambda x: CardValues(x), reverse=True)
cardSuit.remove(trump)


def Winner():
    for enemyCard in enemyCardsSuit[trump]:
        beaten = False
        for myCard in myCardsSuit[trump]:
            if CardValues(myCard) > CardValues(enemyCard):
                myCardsSuit[trump].remove(myCard)
                beaten = True
                break
        if not beaten:
            return False

    for suit in cardSuit:
        for enemyCard in enemyCardsSuit[suit]:
            beaten = False
            for myCard in myCardsSuit[suit]:
                if CardValues(myCard) > CardValues(enemyCard):
                    myCardsSuit[suit].remove(myCard)
                    beaten = True
                    break
            if not beaten:
                for myTrump in myCardsSuit[trump]:
                    beaten = True
                    myCardsSuit[trump].remove(myTrump)
                    break
                if not beaten:
                    return False
    return True


result = Winner()

out = open("output.txt", "w")
if result:
    out.write("YES")
else:
    out.write("NO")
out.close()
