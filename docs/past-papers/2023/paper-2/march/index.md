---
title: 1. March
sidebar_position: 1
---

- Past Paper: https://pastpapers.papacambridge.com/viewer/caie/as-and-a-level-information-technology-9626-2023-march-9626-m23-qp-02-pdf
- Marking Scheme: https://pastpapers.papacambridge.com/viewer/caie/as-and-a-level-information-technology-9626-2023-march-9626-m23-ms-2-pdf
- Files: https://pastpapers.papacambridge.com/viewer/caie/as-and-a-level-information-technology-9626-2023-march-9626-m23-sf-02-zip
- Videos (in order)
    - Spreadsheet: https://youtu.be/BlAeB49YJ_A?si=1eG7zgMlYJ5vp5zm



- Question 6

```xlsx
=INDEX(
    'Tile Data'!$A$2:$C$24, 
    MATCH($B$7, 'Tile Data'!$C$2:$C$24, 0), 
    IFS(
        $B$8="Landscape", 1, 
        $B$8="Portrait", 2
    )
)
```

- Question 8

```xlsx
=ROUNDUP(
    (   
        ROUNDUP((B3*100)/B13, 0)
        *ROUNDUP((B4*100)/B14, 0)
    ) 
    - 
    (
        ROUNDDOWN((B10*100)/B13, 0)
        *ROUNDDOWN((B11*100)/B14, 0)
    )
    *1.1, 0
)
```