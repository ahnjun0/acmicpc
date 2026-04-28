Dim xa As Double, ya As Double, xb As Double, yb As Double, xc As Double, yc As Double
Dim ab As Double, ac As Double, bc As Double
Dim maxLength As Double, minLength As Double
Dim result As Double

Input xa, ya, xb, yb, xc, yc

If ((xa - xb) * (ya - yc) = (ya - yb) * (xa - xc)) Then
    Print str(-1.0)
    End
End If

ab = Sqr((xa - xb) ^ 2 + (ya - yb) ^ 2)
ac = Sqr((xa - xc) ^ 2 + (ya - yc) ^ 2)
bc = Sqr((xb - xc) ^ 2 + (yb - yc) ^ 2)

maxLength = ab
If ac > maxLength Then maxLength = ac
If bc > maxLength Then maxLength = bc

minLength = ab
If ac < minLength Then minLength = ac
If bc < minLength Then minLength = bc

result = 2 * (maxLength - minLength)
Print result
