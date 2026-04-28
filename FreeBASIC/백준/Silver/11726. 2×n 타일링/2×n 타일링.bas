DIM AS INTEGER n
INPUT n

DIM AS INTEGER arr(n - 1)
IF n < 3 THEN
    PRINT str(n)
    END
ELSE
    arr(0) = 1
    arr(1) = 2
    FOR i AS INTEGER = 2 TO n - 1
        arr(i) = (arr(i - 1) MOD 10007 + arr(i - 2) MOD 10007) MOD 10007
    NEXT i
    PRINT str(arr(n - 1) MOD 10007)
END IF