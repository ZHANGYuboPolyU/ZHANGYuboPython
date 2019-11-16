def analyze(m):
    table={'a':0.0817,'b':0.0149,'c':0.0278,'d':0.0425,'e':0.127,'f':0.0223,'g':0.0202,'h':0.0609,'i':0.0697,'j':0.0015,'k':0.0077,'l':0.0403,'m':0.0241,'n':0.0675,'o':0.0751,'p':0.0193,'q':0.001,'r':0.0599,'s':0.0633,'t':0.0906,'u':0.0276,'v':0.0098,'w':0.0236,'x':0.0015,'y':0.0197,'z':0.0007}
    sort_table=sorted(table.items(),key=lambda d:d[1])
    i=97
    mtable=dict()
    while i<123:
        mtable[chr(i)]=(m.count(chr(i))+m.count(chr(i-32)))/len(m)
        i+=1
    sort_mtable=sorted(mtable.items(),key=lambda d:d[1])
    mapping=dict()
    difference=[]
    for i,j in zip(sort_table,sort_mtable):
        mapping[j[0]]=i[0]
        d=abs(i[1]-j[1])*100
        difference.append('%.2f%%'%d)
    print('map','          ','difference')
    for i,j in zip(mapping,difference):
        print(i,'<-',mapping[i],'       ',j)
    return mapping
def decrypt(m,mapping):
    m=list(m)
    for i in range(0,len(m)):
        if 64<ord(m[i])<91:
            m[i]=mapping[m[i].lower()].upper()
        elif 96<ord(m[i])<123:
            m[i]=mapping[m[i]]
    return ''.join(m)
m1 = "This text introduces students to programming and computational problem solving using the Python 3 programming language. \
It is intended primarily for a first-semester computer science (CS1) course, \
but is also appropriate for use in any course providing an introduction \
to computer programming and/or computational problem solving. The book \
provides a step-by-step,'hands on' pedagogical approach which, together \
with Python's clear and simple syntax, makes this book easy to teach and \
learn from."
m2 = "Ziol ztbz ofzkgrxetl lzxrtfzl zg hkgukqddofu qfr egdhxzqzogfqs hkgwstd \
lgscofu xlofu zit Hnzigf 3 hkgukqddofu sqfuxqut. \
Oz ol ofztfrtr hkodqkosn ygk q yoklz-ltdtlztk egdhxztk leotfet (EL1) egxklt, \
wxz ol qslg qhhkghkoqzt ygk xlt of qfn egxklt hkgcorofu qf ofzkgrxezogf \
zg egdhxztk hkgukqddofu qfr/gk egdhxzqzogfqs hkgwstd lgscofu. Zit wgga \
hkgcortl q lzth-wn-lzth,'iqfrl gf' htrquguoeqs qhhkgqei vioei, zgutzitk \
vozi Hnzigf'l estqk qfr lodhst lnfzqb, dqatl ziol wgga tqln zg ztqei qfr \
stqkf ykgd. \
Zit hkodqkn ugqs of zit rtctsghdtfz gy ziol ztbz vql zg ektqzt q htrquguoeqssn \
lgxfr qfr qeetllowst ztbzwgga ziqz tdhiqlomtl yxfrqdtfzqs hkgukqddofu \
qfr egdhxzqzogfqs hkgwstd-lgscofu egfethzl gctk zit dofxzoqt gy q hqkzoexsqk \
hkgukqddofu sqfuxqut. Hnzigf'l tqlt of zit ektqzogf qfr xlt gy wgzi ofrtbtr \
qfr qllgeoqzoct rqzq lzkxezxktl (of zit ygkd gy solzl/zxhstl qfr roezogfqkotl), \
Ql vtss ql ltzl, qssgvl ygk hkgukqddofu egfethzl zg wt rtdgflzkqztr vozigxz \
zit fttr ygk rtzqostr rolexllogf gy hkgukqddofu sqfuxqut lhteoyoel. \
Zqaofu qrcqfzqut gy Hnzigf'l lxhhgkz gy wgzi zit odhtkqzoct (o.t., hkgetrxkqs) \
qfr gwptezgkotfztr hqkqroudl, q 'wqea zg wqloel', 'gwptezl-sqzt' qhhkgqei \
ol zqatfzg egdhxztk hkgukqddofu. \
Oz ygssgvl zit wtsoty ziqz lgsor ukgxfrofu of odhtkqzoct hkgukqddofu \
ligxsr hktetrt zit sqkutk fxdwtk gy (qfr dgkt qwlzkqez) egfethzl gy zit \
gwptez-gkotfztr hqkqroud. Zitktygkt, gwptezl qkt fgz egctktr xfzos Eiqhztk 5, \
qfrgwptez-gkotfztr hkgukqddofu ol fgz ofzkgrxetr xfzos Eiqhztk 10. \
Ygk ziglt vig rg fgz voli zg ofzkgrxet gwptez-gkotfztr hkgukqddofu, \
Eiqhztk 10 eqf tqlosn wt laohhtr. Ziqfal."
mapping = analyze(m1)
print("Mapping dictionary:",mapping)
print("plaintext:",decrypt(m1,mapping))
print("plaintext:",decrypt(m1,{'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k','l':'l','m':'m','n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}))
mapping = analyze(m2)
print("Mapping dictionary:",mapping)
print("plaintext:",decrypt(m2,mapping))
print("plaintext:",decrypt(m2,{'e':'d', 'l':'s', 'w':'g', 'x':'f', 'q':'a','h':'r', 'i':'h', 'n':'p', 'g':'o', 'r':'l', 'z':'t','s':'m', 'p':'j', 'a':'v', 'u':'u', 'y':'y', 'j':'z','c':'b', 't':'e', 'd':'c', 'b':'x', 'o':'i', 'v':'k','f':'w', 'm':'q', 'k':'n'}))
print("plaintext:",decrypt(m2,{'e':'d', 'l':'s', 'w':'g', 'x':'f', 'q':'a','h':'p', 'i':'h', 'n':'y', 'g':'o', 'r':'l', 'z':'t','s':'m', 'p':'j', 'a':'v', 'u':'u', 'y':'r', 'j':'z','c':'b', 't':'e', 'd':'c', 'b':'x', 'o':'i', 'v':'k','f':'n', 'm':'q', 'k':'w'}))
