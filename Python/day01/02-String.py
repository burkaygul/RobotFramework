text = "Hello World";

newText = text.split();

print(text.upper())

print(text.replace("H","Y"));

print(newText);
print(type(newText));


print(text[0])

#text(start:finish:kac)
print(text[0:5:2]); #Hlo
print(text[5:]); # World
print(text[:5]); # Hello

print(len(text))

# lastElement = len(text)-1;

print(text[-1]);

print(text[::-1])