from art_and_data import day8challenge2_Art

logo=day8challenge2_Art.logo
print(logo)
restar=True
while restar == True:
        
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    store_num=[]
    store_sifer_num=[]
    sifered_txt=[]
    sifered_message=" "


    def encode(text,shift):
        for x in text:
            if x in alphabet:
                store_num.append(alphabet.index(x))
        for x in store_num:
            if x+shift > 25:
                z=(x+shift)-26
                store_sifer_num.append(z)
            else:
                z=x+shift
                store_sifer_num.append(z)
        for x in store_sifer_num:
            sifered_txt.append(alphabet[x])
            sifered_message="".join(sifered_txt)
        return sifered_message
                

        
    def decode(text,shift):
        for x in text:      
            if x in alphabet:
                store_num.append(alphabet.index(x))
        for x in store_num:
            if x-shift < 0:
                z=(x-shift)+26
                store_sifer_num.append(z)
            else:
                z=x-shift
                store_sifer_num.append(z)
        for x in store_sifer_num:
            sifered_txt.append(alphabet[x])
            sifered_message="".join(sifered_txt)
        return sifered_message



    if direction=='encode':
        print(f" the cipher is {encode(text,shift)}")
        restarter = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restarter == 'no':
            print("Goodbay")
            restar=False


    else:
        print(f" the orginal message is {decode(text,shift)}")
        restarter = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restarter == 'no':
            print("Goodbay")
            restar=False

        

            

