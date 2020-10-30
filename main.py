a=["0","1","2","3","4","5","6","7","8","9"]

for x in range(0,len(a)):
    test1=a[x]
    for y in range(0,len(a)):
      if(a[y] != a[x] ):
        test2=a[y]
        for z in range(0,len(a)):
          if(a[z]!=a[y]  and a[z]!=a[x]):
            test3=a[z]
            num1 = "7" + (test1)+(test2)  #needs to be string
            num2= "4" +(test3)

            bignum= int(num1)*int(num2)

            bigarray = [int(x) for x in str(bignum)]


            biggerarray = (str(a[x]) + str(a[y]) + str(a[z]) + str(bigarray))
            freq0= biggerarray.count("0")
            freq1= biggerarray.count("1")
            freq2= biggerarray.count("2")
            freq5= biggerarray.count("5")
            freq6= biggerarray.count("6")
            freq8= biggerarray.count("8")
            freq9= biggerarray.count("9")


            if (freq0==1 and freq1==1 and freq2==1 and freq5==1 and freq6==1  and freq8==1 and freq9==1):
                print("These are the values for 7xx, 4X and XXXXX \n", biggerarray)