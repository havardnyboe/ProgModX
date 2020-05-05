def regn_ut_celcius(fahrenheit):
	celcius = (fahrenheit-32)/(9/5)
	return celcius

grader = int(input("Skriv inn grader i farenheit: "))
print(grader, "grader Fahrenheit er lik", round(regn_ut_celcius(grader), 2), "grader Celcius")