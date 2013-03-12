WebAPT
======

Webapt merupakan aplikasi berantarmuka web untuk mengakses sistem APT (Advanced Packaging Tool), yang biasa ada di Distro Linux berbasis Debian dan turunannya.

Webapt ditulis menggunakan beberapa bantuan tool, yang sudah tersedia opensource
- python-apt , http://anonscm.debian.org/loggerhead/apt/python-apt/debian-sid/files
- python-flask, Flask micro framework, http://flask.pocoo.org
- css
- html

Fitur :
-------
1. Autogenerated category untuk menunya;
2. Browse by category;
3. Pagination;
4. Statistik;
5. Search
6. Update

Install
-------

          $git clone https://github.com/blackshirt/webapt.git
          $cd webapt
          $python srv.py

atau, untuk memanfaatkan update, jalankan sebagai root::
         
          #python srv.py'


Copyright blackshirtmuslim@yahoo.com