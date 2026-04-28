dim as integer N, index, tmp
dim as string buffer = ""
dim as integer chunkSize = 1000

input N

For index = 1 TO N
    tmp = index mod chunkSize

    if index mod chunkSize = 0 then
        buffer += str(index)
        print buffer
        buffer = ""
    
    else
        buffer += str(index) + chr(10)

    end if
Next

if len(buffer) > 0 then
    print buffer
end if