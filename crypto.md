# CTF crypto刷题

## buu


## NSSCTF

### 黑盾杯2021 Factor
- 知识点：factordb素数分解，模不互素，中国剩余定理
- wp
```
from gmpy2 import *
from sympy.ntheory.modular import crt
from Crypto.Util.number import long_to_bytes
n = 3454083680130687060405946528826790951695785465926614724373
e = 3
c = 1347530713288996422676156069761604101177635382955634367208
p = 11761833764528579549
q = 17100682436035561357
r = 17172929050033177661
assert p * q * r == n
c1 = c % p
d1 = invert(e, p - 1)
c2 = c % q
# d2 = invert(e, q - 1)
c3 = c % r
d3 = invert(e, r - 1)
m1 = pow(c1, d1, p)
m3 = pow(c3, d3, r)
m2 = crt([p, r], [m1, m3])
print(m2)
m = m2[0]
flag = long_to_bytes(m)
print(flag)
```
### 鹤城杯 2021 Crazy_RSA_tech
- 知识点：中国剩余定理、sympy脚本编写
- wp
```
from sympy.ntheory.modular import crt
from gmpy2 import *
from Crypto.Util.number import long_to_bytes
n_list = [71189786319102608575263218254922479901008514616376166401353025325668690465852130559783959409002115897148828732231478529655075366072137059589917001875303598680931962384468363842379833044123189276199264340224973914079447846845897807085694711541719515881377391200011269924562049643835131619086349617062034608799, 92503831027754984321994282254005318198418454777812045042619263533423066848097985191386666241913483806726751133691867010696758828674382946375162423033994046273252417389169779506788545647848951018539441971140081528915876529645525880324658212147388232683347292192795975558548712504744297104487514691170935149949, 100993952830138414466948640139083231443558390127247779484027818354177479632421980458019929149817002579508423291678953554090956334137167905685261724759487245658147039684536216616744746196651390112540237050493468689520465897258378216693418610879245129435268327315158194612110422630337395790254881602124839071919, 59138293747457431012165762343997972673625934330232909935732464725128776212729547237438509546925172847581735769773563840639187946741161318153031173864953372796950422229629824699580131369991913883136821374596762214064774480548532035315344368010507644630655604478651898097886873485265848973185431559958627423847, 66827868958054485359731420968595906328820823695638132426084478524423658597714990545142120448668257273436546456116147999073797943388584861050133103137697812149742551913704341990467090049650721713913812069904136198912314243175309387952328961054617877059134151915723594900209641163321839502908705301293546584147, 120940513339890268554625391482989102665030083707530690312336379356969219966820079510946652021721814016286307318930536030308296265425674637215009052078834615196224917417698019787514831973471113022781129000531459800329018133248426080717653298100515701379374786486337920294380753805825328119757649844054966712377, 72186594495190221129349814154999705524005203343018940547856004977368023856950836974465616291478257156860734574686154136925776069045232149725101769594505766718123155028300703627531567850035682448632166309129911061492630709698934310123778699316856399909549674138453085885820110724923723830686564968967391721281, 69105037583161467265649176715175579387938714721653281201847973223975467813529036844308693237404592381480367515044829190066606146105800243199497182114398931410844901178842049915914390117503986044951461783780327749665912369177733246873697481544777183820939967036346862056795919812693669387731294595126647751951, 76194219445824867986050004226602973283400885106636660263597964027139613163638212828932901192009131346530898961165310615466747046710743013409318156266326090650584190382130795884514074647833949281109675170830565650006906028402714868781834693473191228256626654011772428115359653448111208831188721505467497494581]
c_list = [62580922178008480377006528793506649089253164524883696044759651305970802215270721223149734532870729533611357047595181907404222690394917605617029675103788705320032707977225447998111744887898039756375876685711148857676502670812333076878964148863713993853526715855758799502735753454247721711366497722251078739585, 46186240819076690248235492196228128599822002268014359444368898414937734806009161030424589993541799877081745454934484263188270879142125136786221625234555265815513136730416539407710862948861531339065039071959576035606192732936477944770308784472646015244527805057990939765708793705044236665364664490419874206900, 85756449024868529058704599481168414715291172247059370174556127800630896693021701121075838517372920466708826412897794900729896389468152213884232173410022054605870785910461728567377769960823103334874807744107855490558726013068890632637193410610478514663078901021307258078678427928255699031215654693270240640198, 14388767329946097216670270960679686032536707277732968784379505904021622612991917314721678940833050736745004078559116326396233622519356703639737886289595860359630019239654690312132039876082685046329079266785042428947147658321799501605837784127004536996628492065409017175037161261039765340032473048737319069656, 1143736792108232890306863524988028098730927600066491485326214420279375304665896453544100447027809433141790331191324806205845009336228331138326163746853197990596700523328423791764843694671580875538251166864957646807184041817863314204516355683663859246677105132100377322669627893863885482167305919925159944839, 2978800921927631161807562509445310353414810029862911925227583943849942080514132963605492727604495513988707849133045851539412276254555228149742924149242124724864770049898278052042163392380895275970574317984638058768854065506927848951716677514095183559625442889028813635385408810698294574175092159389388091981, 16200944263352278316040095503540249310705602580329203494665614035841657418101517016718103326928336623132935178377208651067093136976383774189554806135146237406248538919915426183225265103769259990252162411307338473817114996409705345401251435268136647166395894099897737607312110866874944619080871831772376466376, 31551601425575677138046998360378916515711528548963089502535903329268089950335615563205720969393649713416910860593823506545030969355111753902391336139384464585775439245735448030993755229554555004154084649002801255396359097917380427525820249562148313977941413268787799534165652742114031759562268691233834820996, 25288164985739570635307839193110091356864302148147148153228604718807817833935053919412276187989509493755136905193728864674684139319708358686431424793278248263545370628718355096523088238513079652226028236137381367215156975121794485995030822902933639803569133458328681148758392333073624280222354763268512333515]
print(len(n_list))
print(crt(n_list, c_list))
m9 = crt(n_list, c_list)[0]
m = iroot(int(m9), 9)[0]
print(m)
flag = long_to_bytes(m)
print(flag)

```

### RoarCTF 2019babyRSA
- 知识点：威尔逊定理、素数分解
- wp（因为跑整个代码好像时间较长，所以直接把flag贴在最后了）
```
import sympy
from gmpy2 import *
from Crypto.Util.number import long_to_bytes
e = int(0x1001)
c = 75700883021669577739329316795450706204502635802310731477156998834710820770245219468703245302009998932067080383977560299708060476222089630209972629755965140317526034680452483360917378812244365884527186056341888615564335560765053550155758362271622330017433403027261127561225585912484777829588501213961110690451987625502701331485141639684356427316905122995759825241133872734362716041819819948645662803292418802204430874521342108413623635150475963121220095236776428
A1 = 21856963452461630437348278434191434000066076750419027493852463513469865262064340836613831066602300959772632397773487317560339056658299954464169264467234407
B1 = 21856963452461630437348278434191434000066076750419027493852463513469865262064340836613831066602300959772632397773487317560339056658299954464169264467140596
A2 = 16466113115839228119767887899308820025749260933863446888224167169857612178664139545726340867406790754560227516013796269941438076818194617030304851858418927
B2 = 16466113115839228119767887899308820025749260933863446888224167169857612178664139545726340867406790754560227516013796269941438076818194617030304851858351026
n = 85492663786275292159831603391083876175149354309327673008716627650718160585639723100793347534649628330416631255660901307533909900431413447524262332232659153047067908693481947121069070451562822417357656432171870951184673132554213690123308042697361969986360375060954702920656364144154145812838558365334172935931441424096270206140691814662318562696925767991937369782627908408239087358033165410020690152067715711112732252038588432896758405898709010342467882264362733
s = 1
print(A1 - B1)
for i in range(B1+1, A1):
    s *= i
t = invert(s, A1)
p = sympy.nextprime(mod(-t, A1))
s1 = 1
print(A2 - B2)
for i in range(B2+1, A2):
    s1 = mod(s1 * i, A2)
t = invert(s1, A2)
q = sympy.nextprime(mod(-t, A2))
r = n // (p * q)
assert p * q * r == n
phi = (p - 1) * (q - 1) * (r - 1)
d = invert(e, phi)
m = pow(c, d, n)
flag = long_to_bytes(m)
print(flag)
# RoarCTF{wm-CongrAtu1ation4-1t4-ju4t-A-bAby-R4A}
```

### RoarCTF 2019 RSA
- 知识点：
- wp
```
import gmpy2
from Crypto.Util.number import long_to_bytes
A = 2683349182678714524247469512793476009861014781004924905484127480308161377768192868061561886577048646432382128960881487463427414176114486885830693959404989743229103516924432512724195654425703453612710310587164417035878308390676612592848750287387318129424195208623440294647817367740878211949147526287091298307480502897462279102572556822231669438279317474828479089719046386411971105448723910594710418093977044179949800373224354729179833393219827789389078869290217569511230868967647963089430594258815146362187250855166897553056073744582946148472068334167445499314471518357535261186318756327890016183228412253724
n = 117930806043507374325982291823027285148807239117987369609583515353889814856088099671454394340816761242974462268435911765045576377767711593100416932019831889059333166946263184861287975722954992219766493089630810876984781113645362450398009234556085330943125568377741065242183073882558834603430862598066786475299918395341014877416901185392905676043795425126968745185649565106322336954427505104906770493155723995382318346714944184577894150229037758434597242564815299174950147754426950251419204917376517360505024549691723683358170823416757973059354784142601436519500811159036795034676360028928301979780528294114933347127
c = 41971850275428383625653350824107291609587853887037624239544762751558838294718672159979929266922528917912189124713273673948051464226519605803745171340724343705832198554680196798623263806617998072496026019940476324971696928551159371970207365741517064295956376809297272541800647747885170905737868568000101029143923792003486793278197051326716680212726111099439262589341050943913401067673851885114314709706016622157285023272496793595281054074260451116213815934843317894898883215362289599366101018081513215120728297131352439066930452281829446586562062242527329672575620261776042653626411730955819001674118193293313612128
p = 842868045681390934539739959201847552284980179958879667933078453950968566151662147267006293571765463137270594151138695778986165111380428806545593588078365331313084230014618714412959584843421586674162688321942889369912392031882620994944241987153078156389470370195514285850736541078623854327959382156753458569
q = 139916095583110895133596833227506693679306709873174024876891023355860781981175916446323044732913066880786918629089023499311703408489151181886568535621008644997971982182426706592551291084007983387911006261442519635405457077292515085160744169867410973960652081452455371451222265819051559818441257438021073941183
phi = (p - 1) * (q - 1)
for e in range(100000):
    try:
        d = gmpy2.invert(e, phi)
        m = gmpy2.powmod(c, d, n)
        flag = long_to_bytes(m)
        if b'CTF' in flag:
            print(flag)
            break
    except:
        pass

# RoarCTF{wm-l1l1ll1l1l1l111ll}
```



## bugku CTF

### RSSSA
- 考点：中国剩余定理,sagemath
- wp
```
from Crypto.Util.number import long_to_bytes
import gmpy2
import libnum

e = 29
n = [
    30327806559308143170251580709344293187241377730282921872781575442079759214585250363018838833645033147048274099882927502135822532658361986843089038971809699440265951177983452623836631182131316783838858410002798162604085127069663694047960859197275399255233610031615817404372364349637055800705223698180870067436988096453852212302215116141417320041306889953482862584091194471138823690888819261753453934793173621702326066309884946089600954181869152898879815596750534117681142535676578782280108274188679221706983417414010745084946761574988283779791817969892384961589321416872995532377690950727835973399647956491090102555409,
    21201945432185822273274384690776217497058902883149769388717005633136179247488270702594230376181288768858812012728332675867062647184506694171059959523739358150427193785288862325490483145892589156285417654675409522395461778047750713685913892924628709666682898716590870448590373784915689173142592010032611604863227130433544024508077340982534157235155525782725897976772958969688875400789351919632303930452916408599309209320071861151825269791353531470198408880292345886431587538581009065968803858039954194364023302947597373427552936469472639511930960050054058074397349282354505376836608524919420271358644040625272611834141,
    22066722902445052583751020956045490471001229482392491124491605354676847417172264621341464938604744547196288089839857467414993454346487337649230414610787992018112868327537703873968574017809192037003789320466268844177192403612544118218277599434212247848173311593650429895564484864389688450385022488374534161927558878171030816097844863947341831453646609936063871558801826304657779664413322335636640541461530342335752307248094073705764721946570652851209785138013258495645549732438232440380725327458972312411697319199017195198686877941387699409525165884596929130086232751883272627080260637468553554114550895128931332556731,
    22201854184449819277142185267444382273897841368693102934683821764656962395743826157719287435432760269046740745554089225345079284556882054478011586504345324432037743900501514661174050074095054738909658615769021337525829263909874107830437595890817773992121956416657353703784722839247395770361048793369307710079965231303120658766595423843609770605074056488132086912631857454296414163240447182566834479775710868231123976843543989150070863055009604342636257860806777650229259057896505901924417615469387152636729167180379751548900559610148369495057752373605259839922528981148145028120068953655171238962097381144518051147647,
    23083840233620992224264526611828536460163558999895002497626591923027006640369297896797243966752151170505775381864181314027021495993588967339108820520528972816379841269197877268187639445751437743759925034716110259215833511647315164717603384871571434294945499053929574035111488209616165563966647430661297795173473421242368063748311843339991310650516321423828411278303633083702771322000349673510635860126984256969661571754688788776209025080804889751723316765593984981235995307564443348633486717797511234178142487310778666548407208267425343907584339092352000989025888560813696453621147789642611872568202165905056714548393,
    23218822553600624275851570918327600443202628196986792799225558073420180848161120578874626283971398879263850567245985782927539083923897342980706479709569579629418591343916765139087666874177802508777776627037319228004136490718510415593236575453393195566284309655647871922536044561206875353630359295663312099218766232095780724182736486077598036512073334536846225792741359530446751954255489310204542643379502811042809497521182466190499994814904710462792494798490083908932248164953870969612782940162469775904944210724177461134898671189252356405455733124848794067548040801451291259009951270923040763880342053172756399581161,
    15537621716770448782502134748692657546482394987891814167799488723003580500457315182184780510271452262025473252065075152671351786862081823121704341999623090322622893909472600153140827895279392030437881151726836273881483138361166633444702898613389403354997826623821941237846412179222285546753657710048063757827302566538233983504273873252358216792306525072453406699162260561047287090285490165275142295462447156551127598082848917540871566229207376989948730655600666112133543582179171414297735210520886697976984424647098383547804465263579778326244367614695099540268893495474464880528394459062149362976029449912614166126761]
c = [
    6046094125227689870033870506917812276305436053796436442363822401342062726188042561670757795460948077415972706427946093618320717744079441259077874700893204459036501380012163686628771354515016380758564221578468509762354597066344146672996248499856111282865676568650895987550682149774776905594210993204175895358464315828610392955454920047755436033052407392579110231386427222684373442110938309074563238848319417352567379700597401198483471415807726938645013860932841996827926718400267742249916874079269259123794751964917045940979213140450626289795549071713337129466329394763935853156424248229732551544822323764365359825485,
    5845552286578226566598806127534836409831300694599972428266617271147189508983086233231766595846029052663890341733882461545982026551439575193608090205669127833427025577685774642780332691084053603909859869193052420285065348378657385164191605378649460509586471212644006322411828860570889277856429353408252263239239828396565949357208821626888694650997167695580553398057963048443171407094467284923234982142222808183498767632834628360161922076588397865384233638848062174627983119799111822718694488311274624762022407317556646065445367315918249540635444036633880194363965914260210883151429898423440605220973034396774973125632,
    15903392352203298605877945674465143966769721737532685945162112598239954843499500918942681985964024463454447115748161245918002002655617193080894539813344429249706695035313266913563071057661003650948948239324748886703222675088558181086755212852968181312257303494407773363350004731534848190264255069536036133029778028229221293469762527695954265711168400217935692988501544247020837424584759831204521029707454822146517072769268420888169838807185669690437151962231817248323732857623620673773191557407520247312964435867860663874242179929967218588152288202476576081222176785925045418916462303292404117304143574686336544149629,
    9669717038949021329020108540640237663067756966280810642417630134992373130879787768749181913381401511774773393506456589516952861294673561533008751071662723277608866325874519278507984666760149692092823573606053373801025601646795839172562607132726532904679698936251789947925155456255628127932509101557747423647220724762995217296493861282238350001729340519429193525028741636093329396359178973155083792632330011484299821599210312002159965537430090985352568581714148228760952230630659713444400585630168629530652207170759737992501963831886075598264013355139219445863531555822055994574891400262563108434859568651780227557975,
    7914090642636266923294026791261427849044695562739254282481166732020837928041454353817133871854948761397284836379753705671724947241779482598081203575216043223216563037754382992648875469848870865515423794755447621640988585802308628444956443228403796584499863761840901610073862093944795357445536465073500157568848798543720484354000858578319564737563857043549861785205215491288782410945294230845471220683129677585701046542907136512616807429274294758158965956146717352157078092334387660733724142855367118044193694310952976603009653011262032422467651663006916850935081716939520365535884320814471253649009945816472423048447,
    11988310991395265980081594718856590638441631362665678269045945813797124375621091172731397011814305000162712601455584541005431841875115788140698346738764417691906578333694503756521160780120138569779573589730959145320537390172280626510886154211649716255438845119004751973530199741765756641003306339421117668796100661313571568100843237996562080095649017634551873879219917272328238629844657368364890324594141674498942544827428056492747949043332622214494766621587698339619576784948756333563714427524714670635509179215190783959390410232309595570890592221268445440689742423642145049491551659385729937300897657450196112613804,
    13758385300968829470189169449584800778823082473607121434049610051116374924292341244419430157132107552964735632092568046439074559673147580828760077490267517852677562615547566840913903686439783964549498803731879665085652815249977620067028187162008373600851339874309707587214786555705953533197711132611955125553398328736012543728815790951625456481002420603689802771155816294782083229750332438335093308789359642911367376579780093093577929312234635979675059828551040384269343053231849182709709271027703443106568079145606579815607660891685636327906452992083196131013003312334278998794497774078191519059014857427818993752773]
'''
用SageMath求解中国剩余定理类RSA问题代码如下
import gmpy2
e = 29
n = [
    30327806559308143170251580709344293187241377730282921872781575442079759214585250363018838833645033147048274099882927502135822532658361986843089038971809699440265951177983452623836631182131316783838858410002798162604085127069663694047960859197275399255233610031615817404372364349637055800705223698180870067436988096453852212302215116141417320041306889953482862584091194471138823690888819261753453934793173621702326066309884946089600954181869152898879815596750534117681142535676578782280108274188679221706983417414010745084946761574988283779791817969892384961589321416872995532377690950727835973399647956491090102555409,
    21201945432185822273274384690776217497058902883149769388717005633136179247488270702594230376181288768858812012728332675867062647184506694171059959523739358150427193785288862325490483145892589156285417654675409522395461778047750713685913892924628709666682898716590870448590373784915689173142592010032611604863227130433544024508077340982534157235155525782725897976772958969688875400789351919632303930452916408599309209320071861151825269791353531470198408880292345886431587538581009065968803858039954194364023302947597373427552936469472639511930960050054058074397349282354505376836608524919420271358644040625272611834141,
    22066722902445052583751020956045490471001229482392491124491605354676847417172264621341464938604744547196288089839857467414993454346487337649230414610787992018112868327537703873968574017809192037003789320466268844177192403612544118218277599434212247848173311593650429895564484864389688450385022488374534161927558878171030816097844863947341831453646609936063871558801826304657779664413322335636640541461530342335752307248094073705764721946570652851209785138013258495645549732438232440380725327458972312411697319199017195198686877941387699409525165884596929130086232751883272627080260637468553554114550895128931332556731,
    22201854184449819277142185267444382273897841368693102934683821764656962395743826157719287435432760269046740745554089225345079284556882054478011586504345324432037743900501514661174050074095054738909658615769021337525829263909874107830437595890817773992121956416657353703784722839247395770361048793369307710079965231303120658766595423843609770605074056488132086912631857454296414163240447182566834479775710868231123976843543989150070863055009604342636257860806777650229259057896505901924417615469387152636729167180379751548900559610148369495057752373605259839922528981148145028120068953655171238962097381144518051147647,
    23083840233620992224264526611828536460163558999895002497626591923027006640369297896797243966752151170505775381864181314027021495993588967339108820520528972816379841269197877268187639445751437743759925034716110259215833511647315164717603384871571434294945499053929574035111488209616165563966647430661297795173473421242368063748311843339991310650516321423828411278303633083702771322000349673510635860126984256969661571754688788776209025080804889751723316765593984981235995307564443348633486717797511234178142487310778666548407208267425343907584339092352000989025888560813696453621147789642611872568202165905056714548393,
    23218822553600624275851570918327600443202628196986792799225558073420180848161120578874626283971398879263850567245985782927539083923897342980706479709569579629418591343916765139087666874177802508777776627037319228004136490718510415593236575453393195566284309655647871922536044561206875353630359295663312099218766232095780724182736486077598036512073334536846225792741359530446751954255489310204542643379502811042809497521182466190499994814904710462792494798490083908932248164953870969612782940162469775904944210724177461134898671189252356405455733124848794067548040801451291259009951270923040763880342053172756399581161,
    15537621716770448782502134748692657546482394987891814167799488723003580500457315182184780510271452262025473252065075152671351786862081823121704341999623090322622893909472600153140827895279392030437881151726836273881483138361166633444702898613389403354997826623821941237846412179222285546753657710048063757827302566538233983504273873252358216792306525072453406699162260561047287090285490165275142295462447156551127598082848917540871566229207376989948730655600666112133543582179171414297735210520886697976984424647098383547804465263579778326244367614695099540268893495474464880528394459062149362976029449912614166126761]
c = [
    6046094125227689870033870506917812276305436053796436442363822401342062726188042561670757795460948077415972706427946093618320717744079441259077874700893204459036501380012163686628771354515016380758564221578468509762354597066344146672996248499856111282865676568650895987550682149774776905594210993204175895358464315828610392955454920047755436033052407392579110231386427222684373442110938309074563238848319417352567379700597401198483471415807726938645013860932841996827926718400267742249916874079269259123794751964917045940979213140450626289795549071713337129466329394763935853156424248229732551544822323764365359825485,
    5845552286578226566598806127534836409831300694599972428266617271147189508983086233231766595846029052663890341733882461545982026551439575193608090205669127833427025577685774642780332691084053603909859869193052420285065348378657385164191605378649460509586471212644006322411828860570889277856429353408252263239239828396565949357208821626888694650997167695580553398057963048443171407094467284923234982142222808183498767632834628360161922076588397865384233638848062174627983119799111822718694488311274624762022407317556646065445367315918249540635444036633880194363965914260210883151429898423440605220973034396774973125632,
    15903392352203298605877945674465143966769721737532685945162112598239954843499500918942681985964024463454447115748161245918002002655617193080894539813344429249706695035313266913563071057661003650948948239324748886703222675088558181086755212852968181312257303494407773363350004731534848190264255069536036133029778028229221293469762527695954265711168400217935692988501544247020837424584759831204521029707454822146517072769268420888169838807185669690437151962231817248323732857623620673773191557407520247312964435867860663874242179929967218588152288202476576081222176785925045418916462303292404117304143574686336544149629,
    9669717038949021329020108540640237663067756966280810642417630134992373130879787768749181913381401511774773393506456589516952861294673561533008751071662723277608866325874519278507984666760149692092823573606053373801025601646795839172562607132726532904679698936251789947925155456255628127932509101557747423647220724762995217296493861282238350001729340519429193525028741636093329396359178973155083792632330011484299821599210312002159965537430090985352568581714148228760952230630659713444400585630168629530652207170759737992501963831886075598264013355139219445863531555822055994574891400262563108434859568651780227557975,
    7914090642636266923294026791261427849044695562739254282481166732020837928041454353817133871854948761397284836379753705671724947241779482598081203575216043223216563037754382992648875469848870865515423794755447621640988585802308628444956443228403796584499863761840901610073862093944795357445536465073500157568848798543720484354000858578319564737563857043549861785205215491288782410945294230845471220683129677585701046542907136512616807429274294758158965956146717352157078092334387660733724142855367118044193694310952976603009653011262032422467651663006916850935081716939520365535884320814471253649009945816472423048447,
    11988310991395265980081594718856590638441631362665678269045945813797124375621091172731397011814305000162712601455584541005431841875115788140698346738764417691906578333694503756521160780120138569779573589730959145320537390172280626510886154211649716255438845119004751973530199741765756641003306339421117668796100661313571568100843237996562080095649017634551873879219917272328238629844657368364890324594141674498942544827428056492747949043332622214494766621587698339619576784948756333563714427524714670635509179215190783959390410232309595570890592221268445440689742423642145049491551659385729937300897657450196112613804,
    13758385300968829470189169449584800778823082473607121434049610051116374924292341244419430157132107552964735632092568046439074559673147580828760077490267517852677562615547566840913903686439783964549498803731879665085652815249977620067028187162008373600851339874309707587214786555705953533197711132611955125553398328736012543728815790951625456481002420603689802771155816294782083229750332438335093308789359642911367376579780093093577929312234635979675059828551040384269343053231849182709709271027703443106568079145606579815607660891685636327906452992083196131013003312334278998794497774078191519059014857427818993752773]
m=crt(c,n)
print(gmpy2.iroot(m,e))
求解结果如下
(mpz(56006392793427932363904888802080919147021465251212119978037492467678175693655632715991384875030569597), True)
'''
m = 56006392793427932363904888802080919147021465251212119978037492467678175693655632715991384875030569597
flag = long_to_bytes(m)
print(flag)

```

## 其他平台刷题

### 看雪CTF pellRSA
- 考点：pell方程、sagemath脚本编写
```
# sage脚本
from Crypto.Util.number import *
from gmpy2 import iroot


def solve_pell(N, numTry=100):
    cf = continued_fraction(sqrt(N))
    for i in range(numTry):
        denom = cf.denominator(i)
        numer = cf.numerator(i)
        if numer ^ 2 - N * denom ^ 2 == 1:
            return numer, denom
    return None, None


def gen_pell(D):
    x, y = solve_pell(D)
    xs = [x]
    ys = [y]
    while True:
        yield xs[-1], ys[-1]
        x_i = xs[0] * xs[-1] + D * ys[0] * ys[-1]
        y_i = xs[0] * ys[-1] + ys[0] * xs[-1]
        xs.append(x_i)
        ys.append(y_i)


c = 3005210900274062028245064763681985171865732477888576575723787090796927451576980061053851866237955581217514145765632113368490115032450199985758227732632048361191007646408276913089831906329971437230559530448171301727266374997545370123383402726558627115715475862029561278423823518444820977264751303044302265493708799121168143462311965945091467240934532001260635332451496021570344953585558566967953242376305314361254897583062914601586502797581537297696760063459202795730665696764263768365841709190449166538288878080889669665026312901303009296451551464554389754163788816398944455459009524861984572615424670639254030151054
n = 15718757517521251374958179320446142283106866234677555962716669310992898890185071974665307763506272733881181355624859739900598443787336490077978994566789053663418590696159044391330241067187081512182824631894647418510875405615745967831095900926071879310908555025126167350062806600612989286959517901360623166342258230751843299825036857599702420000410748900477339859195343125679909303239140523015164436167732911014179093209512745136065705348000005927264077855404829601870427156494640300513831498305781704787224695635843906200844830814368296185775476464094439535093160507307060825299000779102353898638521855718963250126411
hint = 25554225946418820739932963199267565143249197331792582934680530259781352338033809894486636299663276720660161274600116944243562621815071872332713982731906833226185925332402882590577780931343494988584492568662132160373007142250538311414299314391751747130332966573464023483628487169137147382668830758422851921134062566813674606680584569364070329996014784761466853704469300230627289640396078029124024721492689780252172435786800400687554721418435802505512555196774950296179670031042084572223128748401
e = 0x10001
N = 0x1337

for (x, y) in gen_pell(N):
    z = var('z')
    delta = hint ** 2 - 4 * x * y * n
    if iroot(delta, 2)[1] == True:
        sol = solve(z ** 2 - hint * z + x * y * n == 0, z, solution_dict=True)
        a, b = int(z.subs(sol[0])), int(z.subs(sol[1]))
        a, b = [a, b] if a > b else [b, a]
        p, q = a // x, b // y
        break
assert p * q == n

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = int(pow(c, d, n))
print(long_to_bytes(m))
```