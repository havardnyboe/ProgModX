def regn_ut_farenheit(celcius):
	farenheit = (9/5)*celcius + 32
	return farenheit

for grader in range(101):
	print(grader, "grader Celcius er lik", round(regn_ut_farenheit(grader), 2), "grader Farenheit")