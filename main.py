def v(x):
	return (0.0000058507979*(x**8)) - (0.0005174910027*(x**7)) + (0.0189518261386*(x**6)) - (0.3718250800899*(x**5)) + (4.2187434830226*(x**4)) - (27.7949714347855*(x**3)) + (100.4868183300756*(x**2)) - (170.6688280668757*x) + 88.396194884242 - 3.6 # diminuindo 3.6 para forçar o resultado para o instante desejado

# Derivada de v (ou a propria aceleração)
def v_prime(x):
	return 0.000046806383512*x**7 - 0.003622437018991*x**6 + 0.113710956831447*x**5 - 1.859125400449306*x**4 + 16.874973932090384*x**3 - 83.38491430435634*x**2 + 200.97363666015121*x - 170.66882806687565


def newton_raphson(f, df, x0, tol):
    if abs(f(x0)) < tol:
        return x0
    else:
		# Recursão!!!
        return newton_raphson(f, df, x0 - f(x0)/df(x0), tol)

print(newton_raphson(v, v_prime, 1, 1e-6))