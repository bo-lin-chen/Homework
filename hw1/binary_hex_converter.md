# 十進位轉二進位跟十六進位 #
### Decimal to binary ###
```mermaid
flowchart TD
    input --> id1{{for i in range 0-8}} --> id2[/如果大於2^7-i/] --yes--> binary第i項=1 --> id3(重複迴圈)
    id2 -.no.-> binary第i項=0 --> id3(重複迴圈)

```
### Decimal to hex ###
```mermaid
flowchart TD
    input --> id1{{for i in range 0-2}} --> id2[/如果大於16^1-i/] --yes--> id3{{for j in 0-16}} --> id4[/如果減16^1-i*j<16且大於零/] ----> id6[/i==0/]--yes--> hex_i=hex_number_j --> id5(重複迴圈)
    id2 --no--> hex_i=0 -->id5
    id6 --no--> hex_i=hex_number_number2 --> id5
```
### Binary to hex ###
```mermaid
flowchart TD
    input --> id1{{for k in range 0-8 }} --> id2[/k<4/] --> hex=binary四項總和 --> id3(重複迴圈)
    id1 --> id4[/k>3/] --> hex=binary四項總和 --> id3(重複迴圈)
