#tipe data dengan angka bulat (integer)
data_integer = 1
print("data bernilai:",data_integer, "dan data bertipe",type(data_integer))

#tipe data dengan angka desimal atau berkoma (float)
data_float = 1.78946
print("data bernilai:",data_float, "dan data bertipe",type(data_float))

#tipe data kumpulan karakter (string)
data_s = "gue cantik masya allah"
print("data bernilai:",data_s, "dan data bertipe",type(data_s))

#tipe data biner true/false (boolean)
data_b = True
print("data bernilai:",data_b, "dan data bertipe",type(data_b))

#tipe data khusus 

#bilangan kompleks
data_komplex = complex(1,2)
print("data bernilai:",data_komplex, "dan data bertipe",type(data_komplex))

#tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(12.3536627)
print("data bernilai:",data_c_double, "dan data bertipe",type(data_c_double))