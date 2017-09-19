# driver.py
# Tests subcipher.py

from subcipher import *
import operator


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = "my coffee tastes like covfefe"
codebet = "QWERTYUIOPLKJHGFDSAZXCVBNM"
plaintext = plaintext.upper()
shift = 10
'''
print("\n---Testing substitution-------")
ciphertext = substitution_cipher_encode(plaintext, alphabet, codebet)
recovered_text = substitution_cipher_decode(ciphertext, alphabet, codebet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)

print("\n---Testing Caesar-------")
ciphertext = caesar_shift_encode(plaintext, shift, alphabet)
recovered_text = caesar_shift_decode(ciphertext, shift, alphabet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)

ciphertext_list = ["NYXDLOCYREWLVOIYEKBOXYDDRKDQBOKD", "QRWHYHUBWKLQJWKDWFDQEHFRXQWHGFRXQWVDQGQRWHYHUBWKLQJWKDWFRXQWVFDQEHFRXQWHG", "UFCYAYNMBUFZQUSULIOHXNBYQILFXVYZILYNBYNLONBBUMUWBUHWYNIAYNCNMJUHNMIH","XUXCSIWPIIWTWPGSTGXLDGZIWTBDGTAJRZXHTTBIDWPKT"]
for cipher_number in range(0,len(ciphertext_list)):
    ciphertext = ciphertext_list[cipher_number]
    for test_shift in range(1, 26):
        recovered_text = caesar_shift_decode(ciphertext, test_shift, alphabet)
        print("Text #"+ str(cipher_number+1) + ", Shift of " + str(test_shift) + ":   " + recovered_text)
    print("------------------------")
    print("\n")

#Text #1, Shift of 10:   DONTBESOHUMBLEYOUARENOTTHATGREAT
#Text #2, Shift of 3:   NOTEVERYTHINGTHATCANBECOUNTEDCOUNTSANDNOTEVERYTHINGTHATCOUNTSCANBECOUNTED
#Text #3, Shift of 19:   BMJFHFUTIBMGXBZBSPVOEUIFXPSMECFGPSFUIFUSVUIIBTBDIBODFUPHFUJUTQBOUTPO
#Text #4, Shift of 15:   IFINDTHATTHEHARDERIWORKTHEMORELUCKISEEMTOHAVE

punc_alphabet = " .,ABCDEFGHIJKLMNOPQRSTUVWXYZ"
substitution_ciphertext = "XKY PK WUKDN YS YJDY ZWWHK JKDI SV. YJKEK BZXX TK VS EKMKWWZSV ZV YJK HVZYKI WYDYKW SO DPKEZMD. UEZPDEZXA IHK YS SHE KVKECA MEZWZW, SHE KMSVSPA ZW UDWWZVC YJESHCJ D IZOOZMHXY UKEZSI. THY Z UXKICK YS ASH YSVZCJY YJDY YJK OHXX USBKEW SO YJZW CSFKEVPKVY BZXX TK HWKI YS NKKU DPKEZMDW KMSVSPA UESIHMZVC DVI YS UESYKMY YJK RSTW SO DPKEZMDW BSENKEW.BK DEK KVCDCKI ZV D XSVC DVI JDEI OZCJY DCDZVWY ZVOXDYZSV. YJKEK JDFK TKKV, DVI YJKEK BZXX TK ZV YJK OHYHEK, HUW DVI ISBVW ZV YJDY OZCJY. THY ZO YJZW MSVCEKWW MSSUKEDYKW ZV SHE KOOSEYW YS JSXI ISBV YJK MSWY SO CSFKEVPKVY, BK WJDXX BZV SHE OZCJY YS JSXI ISBV YJK"
alpha1 = punc_alphabet
alpha2 = " ."


substitution_ciphertext = "XKY PK WUKDN YS YJDY ZWWHK JKDI SV. YJKEK BZXX TK VS EKMKWWZSV ZV YJK HVZYKI WYDYKW SO DPKEZMD. UEZPDEZXA IHK YS SHE KVKECA MEZWZW, SHE KMSVSPA ZW UDWWZVC YJESHCJ D IZOOZMHXY UKEZSI. THY Z UXKICK YS ASH YSVZCJY YJDY YJK OHXX USBKEW SO YJZW CSFKEVPKVY BZXX TK HWKI YS NKKU DPKEZMDW KMSVSPA UESIHMZVC DVI YS UESYKMY YJK RSTW SO DPKEZMDW BSENKEW.BK DEK KVCDCKI ZV D XSVC DVI JDEI OZCJY DCDZVWY ZVOXDYZSV. YJKEK JDFK TKKV, DVI YJKEK BZXX TK ZV YJK OHYHEK, HUW DVI ISBVW ZV YJDY OZCJY. THY ZO YJZW MSVCEKWW MSSUKEDYKW ZV SHE KOOSEYW YS JSXI ISBV YJK MSWY SO CSFKEVPKVY, BK WJDXX BZV SHE OZCJY YS JSXI ISBV YJK MSWY SO XZFZVC OSE YJK DPKEZMDV UKSUXK.DW BK XSSN TDMN SFKE SHE JZWYSEA, YJK AKDEW YJDY WYDVI SHY DW YJK SVKW SO WZCVDX DMJZKFKPKVY DEK YJSWK ZV BJZMJ YJK DIPZVZWYEDYZSV DVI YJK MSVCEKWW, BJKYJKE SVK UDEYA SE YJK SYJKE, BSENZVC YSCKYJKE, JDI YJK BZWISP DVI YJK OSEKWZCJY YS WKXKMY YJSWK UDEYZMHXDE ZVZYZDYZFKW OSE BJZMJ YJK VDYZSV BDW EKDIA DVI YJK PSPKVY BDW EZCJYDVI ZV BJZMJ YJKA WKZGKI YJK PSPKVY DVI DMYKI."
alpha1 = " .,ABCDEFGHIJKLMNOPQRSTUVWXYZ" #coded
alpha2 = " .,YWGARVZUDHE_CKFM_JOBPNSLTI" #decoded/actual letter

#recovered_text = substitution_cipher_decode(substitution_ciphertext, alpha1, alpha2)
#print(recovered_text)
new_string = ""
for letter in substitution_ciphertext:
    new_string+=i2c(c2i(letter, alpha1),alpha2)
print(new_string)
'''


#print(keyword_substitution_cipher_encode("test", "yesterday", alphabet))
#print(keyword_substitution_cipher_decode("PROP", "yesterday", alphabet))

#print(letter_frequencies("Philippe Ricord was born on 10 December 1800 in Baltimore. His father had escaped the French Revolution in 1790 from Marseille. He met French naturalist Charles Alexandre Lesueur, who took him back to Paris in 1820. He worked for Lesueur as curator of his specimens, and at hospitals such as Val-de-Grâce and Hôtel-Dieu de Paris. He studied under Guillaume Dupuytren, but fell out with him when Ricord published an article pointing out a procedure Dupuytren claimed to have invented was already in use in America. He transferred to Pitié-Salpêtrière Hospital to study under Jacques Lisfranc de St. Martin. He graduated in medicine in 1826.[1] After practicing in the provinces he returned in 1828 to the capital, and worked there as a surgeon, specializing in venereal diseases. Doctor Ricord was surgeon in chief to the hospital for venereal diseases and to the Hôpital du Midi. He won a worldwide reputation in his special field. For his suggestions on the cure of varicocele and on the operation of urethroplasty he received in 1842 one of the Montyon prizes.",alphabet,10))
#print(digraph_frequencies("ATTACKATNOON",alphabet,3))
#print(double_letter_frequencies("ATTACKATNOON",alphabet, 2))

#1: BEFORE BILL CLINTON, THE ONLY PRESIDENT TO HAVE BEEN IMPEACHED WAS ANDREW JOHNSON. HE WAS ACQUITTED BY A SINGLE VOTE WHEN A BRAVE SENATOR FROM KANSAS REFUSED TO YIELD FROM PRESSURE TO CONVICT THE PRESIDENT. HAD JOHNSON BEEN CONVICTED, THE SPEAKER OF THE HOUSE WOULD HAVE BECOME PRESIDENT SINCE JOHNSON HAD NO VICEPRESIDENT. INCREDIBLY, IT WAS THIS SAME SPEAKER WHO LED THE IMPEACHMENT IN THE HOUSE OF REPRESENTATIVES. THUS, HAD THE SENATE CONVICTED THE PRESIDENT, THIS WOULD HAVE AMOUNTED TO A POLITICAL COUP
#2: MRANDMRSDURSLEYOFNUMBERFOURPRIVETDRIVEWEREPROUDTOSAYTHATTHEYWEREPERFECTLYNORMALTHANKYOUVERYMUCHTHEYWERETHELASTPEOPLEYOUDEXPECTTOBEINVOLVEDINANYTHINGSTRANGEORMYSTERIOUSBECAUSETHEYJUSTDIDNTHOLDWITHSUCHNONSENSE
print(all_frequencies("PQMJEBJTZFOFQZFKHEIMJPMBEQKIFHKJTAFCKOFQZFPFSOKVEFEPQOFFQPZFOFPQKKEIXEOFMIBJTQOFFAFHKVBQZFVKRHEPBQCKOZKROPMQMQBIFJKVLOKTOFPPQMGFPMVMXVZMQCKOFUFOQKKGQKCBJEJKVZFPCMHHBJTZMOEZFCFFHPQZFCMHHBJTEMOGZKVZFHKJTPQKAFAFJFMQZZBPEOFMIBJTQOFFSKJNRFOFECFMOQKSHBIAMIKIFJQCOKYFBJQBIFVZFJQZFTBOHVZKCBOPQZFGBPPFELOKIBPFEZBIPZFEAFZBPOFIFIAFOFEIKQZFOPVKOEPQZFOFAFJFMQZQZFQOFFJKIMQQFOVZMQQZFVKOHEXKRHHMHVMXPAFIXAMAXIKIIXSKIFNRBSGQZFEOFMIBJTQOFFZMPEBFEQZFMBOBPTOKVBJTQZBSGMCFMOZFSMJJKQZBEFQZFEOFMIBJTQOFFZMPEBFE", alphabet, 10))
substitution_ciphertext = "PQMJEBJTZFOFQZFKHEIMJPMBEQKIFHKJTAFCKOFQZFPFSOKVEFEPQOFFQPZFOFPQKKEIXEOFMIBJTQOFFAFHKVBQZFVKRHEPBQCKOZKROPMQMQBIFJKVLOKTOFPPQMGFPMVMXVZMQCKOFUFOQKKGQKCBJEJKVZFPCMHHBJTZMOEZFCFFHPQZFCMHHBJTEMOGZKVZFHKJTPQKAFAFJFMQZZBPEOFMIBJTQOFFSKJNRFOFECFMOQKSHBIAMIKIFJQCOKYFBJQBIFVZFJQZFTBOHVZKCBOPQZFGBPPFELOKIBPFEZBIPZFEAFZBPOFIFIAFOFEIKQZFOPVKOEPQZFOFAFJFMQZQZFQOFFJKIMQQFOVZMQQZFVKOHEXKRHHMHVMXPAFIXAMAXIKIIXSKIFNRBSGQZFEOFMIBJTQOFFZMPEBFEQZFMBOBPTOKVBJTQZBSGMCFMOZFSMJJKQZBEFQZFEOFMIBJTQOFFZMPEBFE"
alpha0 = " .,ABCDEFGHIJKLMNOPQRSTUVWXYZ" #coded
alpha1 = " .,MUONTSGC_LVB_AKYFIPEQWJRDH" #decoded/actual letter
alpha2 = " .,LOMHPU_IRAXEKCWFDBY_NJGTVS" #decoded



#week 3
alpha0 = " .,ABCDEFGHIJKLMNOPQRSTUVWXYZ" #coded
alpha1 = " .,B_F__E_L____UJRST__D_____H" #decoded




new_string = ""
for letter in substitution_ciphertext:
    new_string+=i2c(c2i(letter, alpha0),alpha1)
print(new_string)


#Digraphs: TH, HE, IN, ER, AN, RE, ND, AT, ON, NT, HA, ES, ST, EN, ED, TO, IT, OU, EA
#Trigraphs: THE, AND, THA, ENT, ION, TIO, FOR, NDE, HAS, NCE
#Double letters: LL, EE, SS, OO, FF, TT

# e most common
# ll most double






'''
freq_dict = {}
for letter in substitution_ciphertext:
    if letter in freq_dict:
        freq_dict[letter] += 1
    else:
        freq_dict[letter] = 1

del freq_dict[' ']
del freq_dict['.']
del freq_dict[',']
sorted_freq = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True)
english_freq = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

counter = 0
#print(freq_dict)
for key in sorted_freq:
    freq_dict[key[0]] = english_freq[counter]
    counter+=1
#print(freq_dict)
alpha1 = list(freq_dict.keys())
alpha2 = list(freq_dict.values())
alpha1.extend(['.',' ', ','])
alpha2.extend(['.',' ', ','])
recovered_text = substitution_cipher_decode(substitution_ciphertext, alpha1, alpha2)
print(recovered_text)
'''

