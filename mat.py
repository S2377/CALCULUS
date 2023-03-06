if b**2 - 4*a*c > 0 :
  print('This is over damping.')
  x = []
  for i in t:
    lam1 = ((-b + math.sqrt(b**2-4*a*c))/2*a)
    lam2 = ((-b - math.sqrt(b**2-4*a*c))/2*a)
    d1 = (v_0 - lam2*x_0)/(lam1-lam2)
    d2 = (v_0 - lam1*x_0)/(lam2-lam1)
    y = d1*math.exp(lam1*t) + d2*math.exp(lam2*t)
    x.append(y)
 


 t=[]
for i in range(6):
  t.append(i/10)




# checkig tpye of damping 
if b**2 - 4*a*c > 0 :
  print('This is over damping.')
  x = []
  for i in t:
    lam1 = ((-b + math.sqrt(b**2-4*a*c))/2*a)
    lam2 = ((-b - math.sqrt(b**2-4*a*c))/2*a)
    d1 = (v_0 - lam2*x_0)/(lam1-lam2)
    d2 = (v_0 - lam1*x_0)/(lam2-lam1)
    y = d1*math.exp(lam1*t) + d2*math.exp(lam2*t)
    x.append(y)
 


if b**2 - 4*a*c == 0 :
  print('This is critical damping.')
  x = []
  for i in t:
    lam1 = (-b/2*a)
    m = v_0/lam1 
    y = m*math.exp(lam1*t)
    x.append(y)


if b**2 - 4*a*c < 0 :
  print('This is under damping.')
  x = []
  for i in t:
    alpha = -b/2*a
    beta = math.sqrt(abs((b**2/4*a**2)-(c/a))
    m = math.exp(alpha*t)*(math.cos(beta*t)*x_0 + (math.sin(beta*t)*(v_0 + x_0*alpha))/beta
    x.append(m)



