BAHASA
======

Modul stemmer yang digunakan merupakan hasil _porting_ dari [Sastrawi](https://github.com/sastrawi/sastrawi) dengan beberapa perubahan.

INSTALASI
---------

Kita dapat menginstal bahasa dengan cara sebagai berikut:
```bash
pip install bahasa
```


PENGGUNAAN
----------

```python
from bahasa.stemmer import Stemmer

stemmer = Stemmer()

hasil = stemmer.stem("Saat ini pemerintah sedang memilih untuk menentukan rel yang digunakan.")
print(hasil)
saat ini perintah sedang pilih untuk tentu rel yang guna

hasil = stemmer.stem("membuang-buang waktu")
print(hasil)
buang waktu

# Menambahkan kata ke dalam kamus
stemmer.add_words("lauk", "nasi", "piring")

# Menghapus kata dalam kamus
stemmer.remove_words("ikan", "kucing")
```

TEST
----
```bash
python -m unittest discover
```
