DIM AS INTEGER T, M, N, X, Y, TMP, LCM_V, FOUND, A, B, C, D, i

FUNCTION GCD(A AS INTEGER, B AS INTEGER) AS INTEGER
    WHILE B <> 0
        DIM TEMP AS INTEGER = B
        B = A MOD B
        A = TEMP
    WEND
    RETURN A
End Function

Function LCM(C AS INTEGER, D AS INTEGER) AS INTEGER
    RETURN (C / GCD(C, D)) * D
End Function

INPUT T

FOR i = 1 TO T
    INPUT M, N, X, Y

    TMP = X
    LCM_V = LCM(M, N)
    FOUND = 0

    WHILE TMP <= LCM_V
        IF ( TMP - Y ) MOD N = 0 THEN
            PRINT STR(TMP)
            FOUND = 1
            EXIT WHILE
        ENDIF
        TMP += M
    WEND
    IF FOUND = 0 THEN
        PRINT "-1"
    ENDIF
NEXT