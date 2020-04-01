#PYTHON TEMELLERI
9+2
9
9.2
5 / 3
5 // 3
"Hello AI"
print("hello AI area")
i = 9
f = 9.2
type(i)
type(f)
string = "Hello 1"
string2 = 'hello 2'
type(string)
type(string2)
?print # document is shown in the console
dir(string2) # show all methdors for type of string2

#STRINGLER DETAY
#concatenation
"a" + "b"
"a" "b"
"a" " " "b"
#multiply
"a"*3
"a""b"*3
"a"*3+"b"
3*"a"+"b"
3*"a""b"
#length fonksiyonu: len()
str1 = "Bu bir string!"
str2 = str1
len(str2)
#delete an variable use # for deleted object 
del str1

# METHODS AND STRINGS
#.upper() ve .lower()
str2.upper()
str2.lower()
str2 #string doesn't change
#.islower() ve .isupper()
str2.islower()
str2.isupper()
strB = str2.upper()
strB.isupper()
#del str2, strB, str1 ,str3
#.replace()
str_long = "    al şu taka tukaları taka tukacıya götür"
str_long.replace("a",".") 
str_long #no update
#.strip() en sağdan ve en soldan temizleme yapar
str_long = "al şu taka tukaları "
str_long.strip() #varsa solunada sağında boşlukları siler
str_long.strip("a") 
str_long.strip("r")
# Show All Methods of a Class
str_exp = "Bu bir cümle"
str_exp.capitalize()
str_exp.title()
#Sub String
main_string = "bu string alt stringlerine parçalanacak"
main_string[0] # b
main_string[1] # u
main_string[100] # out of range
main_string[-1] # reverse index
main_string[0:2] #sol taraf dahil sağ taraf hariç
main_string[3:9]

#VARIABLES
type(100)
type(100.2)
type(100+3j)
c = 100 + 3j  #c = 100 + 3i error j is fixed

#TYPE TRANSFORMATION
toplanan1 = input()
toplanan2 = input()
toplam = toplanan1 + toplanan2
toplam
type(toplam)

toplanan1 = input()
toplanan2 = input()
toplam = int(toplanan1) + int(toplanan2)
toplam
type(toplam)

number = 3.1415
int(number)
number = 4.9999
int(number)         #don't round
float(3)
str(number)

#PRINT()
print("Hello","World")
print("Hello","World",sep="++") # sep gibi belirteçlere argüman denir
print("Hello","World","!!!",sep="++") 
?print










