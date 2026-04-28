DIM AS INTEGER t, five, remain

INPUT t

five = t \ 5
remain = t MOD 5

IF remain = 0 AND t >= 5 THEN
    PRINT str(five)
ELSEIF remain = 1 AND t > 5 THEN
    PRINT str(five + 1)
ELSEIF remain = 3 THEN
    PRINT str(five + 1)
ELSEIF (remain = 2 OR remain = 4) AND t > 5 AND t <> 7 THEN
    PRINT str(five + 2)
ELSEIF t = 7 THEN
    PRINT str(-1)
ELSE
    PRINT str(-1)
END IF