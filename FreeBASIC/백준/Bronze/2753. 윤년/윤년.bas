dim A as integer
input A

if A mod 4 = 0 then
    if A mod 400 = 0 then
        print "1"
    elseif A mod 100 <> 0 then
        print "1"
    else
        print "0"
    end if

else
    print "0"
    
end if