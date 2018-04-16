BinaryString = input('enter binary string')
length = len(BinaryString)
DenaryValue = 0
for i in range (0,length):
    BinaryDigit = int(BinaryString[i])*(2**(length-(i+1)))
    DenaryValue = DenaryValue + BinaryDigit
print('Binary String = ', BinaryString,' Denary Value = ',DenaryValue)

ReverseBinaryString = ''
DenaryValue = 0
for i in range(0,length):
    ReverseBinaryString = ReverseBinaryString + BinaryString[length - (i+1)]
    DenaryValue = DenaryValue + 2**i*int(ReverseBinaryString[i])
print(DenaryValue)

    
