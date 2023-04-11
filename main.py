from ogrenci import Ogrenci
from ogretmen import Ogretmen
ogrenciList=[]
ogretmentList=[]
def ogrenci_ekle(ad,soyad):
    ogrenci=Ogrenci(ad,soyad)
    ogrenciList.append(ogrenci)
def ogretmen_ekle(ad,soyad):
    ogretmen=Ogretmen(ad,soyad)
    ogretmentList.append(ogretmen)

ogrenci_ekle("Volkan","Erdoğuş")
ogrenci_ekle("Duygu","Yılmaz")
ogretmen_ekle("Elif","Aksoy")
ogretmen_ekle("Hande","Oral")

for ogrenci in ogrenciList:
    ogrenci.goster()
for ogretmen in ogretmentList:
    ogretmen.goster()

   
