CodigoMorse = {
    'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
    'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
    'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',".":'.-.-.- ',",":"-.-.-- "," ":"/ "
}

output = []
requestNum = int(input())


for i in range(requestNum):
    strMorse = ""
    requestStr = input()
    for j in requestStr:
        upperStr = j.upper()
        strMorse += CodigoMorse[upperStr]
    output.append(strMorse)

for i in output:
    print(i,"\n")

