from pylab import *

n = 10000

terning  = zeros(n+1)
kast = linspace(1,n,n+1)
frekvens = zeros(n+1)
antseksere = 0

for i in range(1, n+1):
    terning[i] = randint(1,7)
    if terning[i] == 6:
        antseksere+=1
    frekvens[i] = antseksere/i

title("Terningkast")
plot(kast, array(frekvens)*100)
# plot(kast[-1], , ".")
xlabel("Ant Kast")
ylabel("Frekvens i %")
show()