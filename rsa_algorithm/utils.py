from rsa_encryption import encrypt, decrypt
import math

# Selected primes p and q from:
# https://t5k.org/primes/page.php?id=132936
# https://t5k.org/primes/page.php?id=119628

p = 504047074759976118362547213552326856111518250282791249968689378546454471112442645866195532219135552041345389747204292449265409915836497721507952344009757242788240584063503764684489985460308742669359621071799174032348712734258157028016604992715699241697547658556542474798611154943983653568291994326093161944916801118384228787027551888897849623202058134960267950604222207288148566763784952327266881451439184277973203721222998115019155681702853870152476388072244695575506646328487221506854617829891183769572282612426996308723685764097537799414305379062161557822129126028420564531807037889375066435098010694340412681411620468492229703855456565360976603082550926713897839604660053993122379355583349153225954412299314963762214846663651864140760446652658216296494460851357087839373298574324234466322396158453195718040542531882095274210728103232799993257351380901672006208870950318361308281877014179905757590437230195560903759928270997297858251426307637993597502893892889229276228661051698247606403744945344626150437088999039
q = 1264906703566737711594719870801915218395598824601474232734807958732336012552378499047462656026382640022163914348448136367416698669468565477104491064348229568733731262810267149896072183825857178043349952209317172654570333505698901209079886179756891559076225153981649979810167529818859202728902988457985201964208812285819316012488850272614234876136900093285930195277515873749068733858970727099479039085374902383882386839728528730457834024698697123060814984224223675669957213407330366012083493906367409384366890041672336198023041732674641629938135233485228301660793907283061419228798581265312661443408917185736851908731245638167040696655786591636101464459846718260817679360853385800897430264581694694308045680275968366084861446971625209710068957091591194320388081066900784861833691907620960410184912924658608050639718167900354460594514247885657611768805762807261844856956972819115528803514238603317477410348248893502757967196544235778135870007633166897342528153629947198081776158055962852980340265874848100433465447
n = p * q

# print(isprime(n))
# print(isprime(p))
# print(isprime(q))

n_totient = (p - 1) * (q - 1)

e = pow(3, 1000)

# Base, exponent, modulus
d = pow(e, -1, n_totient)


def convert_to_hex(text_message):
    list_of_hex = []

    for i in range(len(text_message)):
        if ord(text_message[i]) > 255:
            raise ValueError("The message must be in ASCII format")

        list_of_hex.append(hex(ord(text_message[i]))[2:])

    return list_of_hex


def convert_hex_to_decimal(text_message_hex):
    list_of_decimal = []

    for i in range(len(text_message_hex)):
        list_of_decimal.append(int(text_message_hex[i], 16))

    return list_of_decimal


def compute_rsa(message):
    print("\nEncryption")

    message_hex = convert_to_hex(message)
    message_decimal = convert_hex_to_decimal(message_hex)
    encrypted_message = encrypt(message_decimal, e, n)
    print("\nEncrypted message:")

    for i in encrypted_message:
        print(i)

    print("\nDecryption")

    decrypted_message = decrypt(encrypted_message, d, n)
    print("\nDecrypted message:")

    for i in decrypted_message:
        print(i)

    print("\nDecrypted message in ASCII format:")
    print("".join([chr(i) for i in decrypted_message]))


def enter_menu():
    while True:
        print("\nRSA")
        print("1. Enter message")
        print("2. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print("\nEnter message:")
            message = input()
            compute_rsa(message)
        elif choice == 2:
            exit()
        else:
            print("\nInvalid choice")
