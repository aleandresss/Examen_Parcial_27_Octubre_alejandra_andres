print("Ingrese los valores:")
print("|M00 M01 M02 M03 M04|")
print("|M10 M11 M12 M13 M14|")
print("|M20 M21 M22 M23 M24|")
print("|M30 M21 M32 M33 M34|")
print("|M40 M41 M42 M43 M44|")



M00 = float(input('Ingrese el valor M00: '))
M01 = float(input('Ingrese el valor M01: '))
M02 = float(input('Ingrese el valor M02: '))
M03 = float(input('Ingrese el valor M03: '))
M04 = float(input('Ingrese el valor M04: '))
M10 = float(input('Ingrese el valor M10: '))
M11 = float(input('Ingrese el valor M11: '))
M12 = float(input('Ingrese el valor M12: '))
M13 = float(input('Ingrese el valor M13: '))
M14 = float(input('Ingrese el valor M14: '))
M20 = float(input('Ingrese el valor M20: '))
M21 = float(input('Ingrese el valor M21: '))
M22 = float(input('Ingrese el valor M22: '))
M23 = float(input('Ingrese el valor M23: '))
M24 = float(input('Ingrese el valor M24: '))
M30 = float(input('Ingrese el valor M02: '))
M31 = float(input('Ingrese el valor M02: '))
M32 = float(input('Ingrese el valor M02: '))
M33 = float(input('Ingrese el valor M02: '))
M34 = float(input('Ingrese el valor M02: '))
M40 = float(input('Ingrese el valor M02: '))
M41 = float(input('Ingrese el valor M02: '))
M42 = float(input('Ingrese el valor M02: '))
M43 = float(input('Ingrese el valor M02: '))
M44 = float(input('Ingrese el valor M02: '))



det= (M00*M11*M22*M33*M44) + (M10*M21*M02) + (M20*M01*M12) - (M02*M11*M20) - (M12*M21*M00) - (M22*M01*M10)

if det!=0:
   print ("El determinante de esta matriz es: ",det)

else:
    print ("El determinante de esta matriz es cero")