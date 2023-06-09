# Ipar_beadando
# Ipar 4.0 Beadandó Real-Time Face recognition
## Készítette: Nyeste Réka (GKE37T)
### Forrás: https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348

# Jelenleg két python file található a programban, amiket főleg eszközeim teszteléséhez készítetem. Hibátlan működés érdekében sorban kell az összes programot (elsőtől a hetedikig) lefuttatni!
## Első program: test.py -> ezzel ellenőriztem, hogy működik-e az importált opencv verziója. A python nyelvnél nagyon fontos, hogy a megfelelő verziójú csomagokat és programokat teleptítsük.
## Második program: cameraTesting.py -> a számítógép vagy laptop kamerájának a tesztelésére elkészített program. Érdemes lefuttatni, hogy minden rendben van-e mielőtt hozzálátunk a többi feladathoz. Csak simán futtassuk le a programot, majd ha látjuk, hogy működik a kamera 'ESC' billentyűvel kiléphetünk belőle.

# Arc detektálás kiegészítve szemek felismerésével:
## Harmadik program: faceDetection.py -> Az arcunkat ismeri fel a kamerában. Egyelőre csak felismeri azt és nem társítja névhez, csak megismeri, hogy a kamerában egy arc található.
## Negyedik program: eyeDetection.py -> ugyanaz, mint a harmadik program, csak itt az emberi szemeket ismeri fel (a tree eyeglasses cascade-dal már csak a szemeket ismeri fel, ez egy pontosabb script mint a sima eye cascade, ami gyakran az orrlyukat is szemekként ismeri fel)
### A faceDetection program tartalmazza az eyeDetection funkciót is!
### Az eyeglasses "kaszkád" sokkal jobban felismeri a szemeket szemüvegben, mint a sima eyeCascade, ezért én ezt preferálom.

# Arc felismerés megtanult képek alapján:
## Ötödik program: FaceRecognition01.py -> Elment 15 db szürkeárnyalatos képet a kiválasztott mappába, miután inputba írtunk egy ID-t és detektálta a kamerában lévő arcot. Ez a program egy lépése annak, hogy a saját arcunkat ismerje fel a végén a programunk.
## Hatodik program: FaceRecognition02.py -> A legfontosabb rész. Ez a program tanulja meg az előző programból elmentett képek alapján felismerni a kamerába néző személynek az arcát. Miután lefutott, egy yaml kiterjesztésű fájlt készít a trainer mappába, ez tartalmazza azokat az adatokat, amik a következő lépéshez, vagyis egy arc megismeréséhez szükségesek. Ergo, ha belenézünk a kamerába felismer.
## Hetedik program: FaceRecognition03.py -> utolsó lépésben a kamera felismeri az arcot az előző két programból megtanult képekkel. Nagyon fontos, hogy sorban futtassuk le őket (01 -> 02 -> 03) mert enélkül nem fog működni.