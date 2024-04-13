a=range(80,100)
b=range(70,79)
c=range(60,69)
d=range(50,59)
f=range(0,49)
score=int(input("Ingrese su puntuación:"))
if score >= 80 :
    print("Su puntuacion es A ya que esta en el 80-100%")
elif score in b:
    print("Su puntuación es B ya que esta en el 70-79%")
elif score in c:
    print("Su puntuación es C ya que esta en el 60-69%")
elif score in d:
    print("Su puntuación es D ya que esta en el 50-59%")
elif score in f:
    print("Su puntuación es F ya que esta en el 0-49%")