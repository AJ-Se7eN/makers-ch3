def foo(a):
    cont = text.read()
    new_cont=cont.replace("\n"," ")
    num_words=new_cont.split(" ")
    num_strok=cont.split("\n")
    num_letters=new_cont.replace(" ","")
    stroka=len(num_strok)
    letters=len(num_letters)
    word = len(list(filter(bool, num_words)))
    print(stroka,"строк",word,"слов",letters,"букв")
text = open('/home/jetigen/Desktop/HomeWork/week1/text.txt', "r")
foo(text)