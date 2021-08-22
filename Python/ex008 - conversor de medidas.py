# km(0.001), hm(0.01), dam(0.1), m(1), dm(10), cm(100), mm(1000)
print('{:-^60}'.format(" Conversor de Medidas "))
metros = float(input("Digite uma distancia em metros: "))

km = metros / 1000
hm = metros / 100
dam = metros / 10

dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('''A Distancia em metros {:.2f}M convertido será: 
km : {}km
hm : {}hm
dam : {}dam
dm : {:.2f}dm
cm : {:.2f}cm
mm : {:.2f}mm'''.format(metros, km, hm, dam, dm, cm, mm))
