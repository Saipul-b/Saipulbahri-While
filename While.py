n = 20
  i = 0
  jumalah_ganjil = 0
  while i <= n:
      if i % 2 != 0:
          jumalah_ganjil += i
      i += 1
      print (f"jumlah deret bilangan ganjil dari 1 hingga {n} adalah {jumalah_ganjil}")
