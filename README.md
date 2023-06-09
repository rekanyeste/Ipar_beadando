# Ipar_beadando
# Ipar 4.0 Beadandó Real-Time Face recognition
## Készítette: Nyeste Réka (GKE37T)
### Források: 
- https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348
- https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
- https://github.com/opencv/opencv/tree/master/data/haarcascades
- https://github.com/Mjrovai/OpenCV-Face-Recognition/tree/master


# Az első két programot az eszközeim teszteléséhez készítettem. Hibátlan működés érdekében sorban kell az összes programot (elsőtől a hetedikig is) lefuttatni!
## Első program: test.py -> ezzel ellenőriztem, hogy működik-e az importált opencv verziója. A python nyelvnél nagyon fontos, hogy a megfelelő verziójú csomagokat és programokat teleptítsük, különben semmi nem fog működni. Érdemes utána járni, hogy milyen verziójú python mivel működik együtt.
## Második program: cameraTesting.py -> a számítógép vagy laptop kamerájának a tesztelésére készített program. Érdemes lefuttatni, hogy minden rendben van-e mielőtt hozzálátunk a többi feladathoz. Csak simán futtassuk le a programot, majd ha látjuk, hogy működik a kamera 'ESC' billentyűvel kiléphetünk belőle.

# Arc detektálás kiegészítve szemek felismerésével:
## Harmadik program: faceDetection01.py -> Az arcunkat ismeri fel a kamerában. Egyelőre csak felismeri azt és nem társítja névhez, csak megismeri, hogy a kamerában egy arc található.
-  A faceDetection program tartalmazza az eyeDetection funkciót is!
## Negyedik program: eyeDetection.py -> ugyanaz, mint a harmadik program, csak itt az emberi szemeket ismeri fel.
- Az eyeglasses "kaszkád" sokkal jobban felismeri a szemeket szemüvegben, mint a sima eye cascade, ezért én ezt preferálom.

# Real-Time arc felismerés megtanult képek alapján:
## Ötödik program: FaceRecognition01.py -> Elment 15 db szürkeárnyalatos képet a dataset mappába, miután inputba írtunk egy ID-t és detektálta a kamerában lévő arcot. Ez a program egy lépése annak, hogy a saját arcunkat ismerje fel a végén a programunk.
## Hatodik program: FaceRecognition02.py -> A legfontosabb rész. Ez a program tanulja meg az előző programból elmentett képek alapján felismerni a kamerába néző személynek az arcát. Miután lefutott, egy yaml kiterjesztésű fájlt készít a trainer mappába, ez tartalmazza azokat az adatokat, amik a következő lépéshez, vagyis egy arc megismeréséhez szükségesek. Ergo, ha belenézünk a kamerába felismer.
## Hetedik program: FaceRecognition03.py -> utolsó lépésben a kamera felismeri az arcot az előző két programból megtanult képekkel. Nagyon fontos, hogy sorban futtassuk le őket (01 -> 02 -> 03) mert enélkül nem fog működni.