---
title: 2. June
sidebar_position: 2
---

- Past Paper: https://pastpapers.papacambridge.com/viewer/caie/as-and-a-level-information-technology-9626-2022-may-june-9626-s22-qp-02-pdf
- Marking Scheme: https://pastpapers.papacambridge.com/viewer/caie/as-and-a-level-information-technology-9626-2022-may-june-9626-s22-ms-2-pdf
- Videos (in order)
    - Spreadsheet: https://youtu.be/jDEoW8vqtw0?si=XSQ86auF8IV10Z63



- Question 4:

```xlsx
=IF(
    VLOOKUP(C9,j22port!$A$3:$C$12,3,FALSE)="",
    A9,
    IF(
        WEEKDAY(A9)=MATCH(
            VLOOKUP(C9,j22port!$A$3:$C$12,3,FALSE),
            j22port!A14:A20,
            0
        ),
        A9+1,
        A9
    )
)
```

- Question 5

```xlsx
=INDEX(
    j22port!D3:M12, 
    MATCH(Sheet1!C9, j22port!A3:A12, 0), 
    MATCH(Sheet1!C10, j22port!D2:M2, 0)
)
```

- Question 6

```xlsx
=ROUNDUP(
    E10 / VLOOKUP(
            B5, j22ship!A2:E27, 3, FALSE
          )
        /24, 
    0
)
```
