from crypto4 import CryptoFormatter
input_string = "3:13PM, 5"
c=CryptoFormatter()
message, padding = c.parse_input_string(input_string)
padded_message = c.cformat(message, padding)
#print ("message ", message, "padding: ", padding)
#print(c.cformat(input_string))
print (padded_message)
