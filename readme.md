# 2048

Dokumentace zápočtové aplikace.

Téma: Hra 2048

Autor: Daniel Josef

# Ovládání

Primárním ovladačem celé aplikace je klávesnice. Myší lze pouze aplikaci ukončit, kliknutím na zavírací pole jako u běžných aplikací.

**Používané klávesy**
|možnost 1|možnost 2 | funkce |
|-|-|-|
| W | arrow_up | pohyb nahoru |
| A | arrow_left | pohyb vlevo |
| S | arrow_down | pohyb dolů |
| D | arrow_right | pohyb vpravo |
| enter | - | potvrzení |

## Menu

V každém aplikačím menu jsou podsebou zobrazené možnosti a aktuálně vybraná možnsot je označena kurzorem (X). Mezi jednotlivými možnostmi lze přepínat příslušnými klávesami pro pohyb nahoru a dolů. Zvolenou možnost lze potvrdit příslušnou klávesou pro potvrzení.

V hlavním menu si hráč volí obtížnost. (Hodnota, kterou je třeba získat k vítězství)

## Hra

Samotná hra probíhá spojováním políček se stejnými hodnotami, přesouváním vždy všech polí jedním směrem. Směr pohybu v každém kole lze zvolit pomocí příslušné klávesy pohybu.

Pokud se hráč dostane do situace, kdy již není možné s políčky dále manipulovat jakýmkoliv směrem, zobrazí se informace o prohře a hráč si může zvolit zda to chce zkusit znovu nebo aplikaci ukončit.

Pokud se hráč dostane do situace, kdy jendo z políček disponuje zvolenou výherní hodnout, zobrazí se informace o výhře a hráč si může zvolit zda to chce zkusit znovu nebo aplikaci ukončit.

# Architektura

Aplikace je rozdělena do tří hlavních částí

1.  Manager obrazovek aplikace
2.  Jednotlivé obrazovky aplikace
3.  Herní engine

## diagram architektury

![diagram](./architecture.png)

## setup

Definuje základní proměné okna aplikace a inicializuje modul PyGame.

## templates

Obsahuje základní třídy pro definování různých stavů aplikace.

- State()
  - základní třída
  - obsahuje proměné a metody, které využívají všechny stavy
- Menu(State)
  - odvozena od State()
  - rozšíření o další proměné a metody, které využivají všechny menu

## menu

Definuje tři různé menu. Všechny jsou odvozené od třídy Menu() z templates.

- MainMenu()
  - hlavní menu
  - umožňuje volbu obtížností
- WinMenu()
  - předává informaci o výhře
  - umožnňuje volbu mezi ukončením a restartem hry
- LoseMenu()
  - předává informaci o prohře
  - umožnňuje volbu mezi ukončením a restartem hry

## engine

Definuje třidu Engine(), která uchovává informace o stavu hry a metody, které mohou stavem manipulovat.

Stav hry je uložen pomocí vnořeného pole (self.board).

Manipulační metody:

- compress()
  - posune políčka směrem doleva tak, aby mezi nimi nebyly mezery
- merge()
  - směrem doleva spojí políčka, která se dotýkají a mají stejné hodnoty
- transpose()
  - transponuje mřížku herní plochy
- reverse()
  - zrcadlově otočí mřížku herní plochy (zleva doprava)

Pomocí kombinace těchto metod je následně možné simulovat spojení políček v libovolném ze čtyř směrů.

## game

Zajišťuje vykreslování a ovládání hry.

Zároveň inicializuje engine a stará se o spouštění metod enginu ve sprvánou chvíli.

## control

Zajišťuje vykreslování jednotlivých stavů hry a zároveň přepínání mezi nimi.

Definuje základní event handling a loop aplikace.

## main

Slouží jako obal a spouštěč celé aplikace.

- Vytvoří instanci Control
- Definuje názvy stavů
- Spustí hlavní loop
