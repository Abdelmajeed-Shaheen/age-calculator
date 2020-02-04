import datetime

def check_birthdate(year, month, day):
	date = datetime.date(int(year),int(month),int(day))
	if date <= datetime.date.today():
		return True
	else:
		return False


def calculate_age(year, month, day):
	yearint = int(year)
	age = 0
	thisyear = datetime.date.today().year
	if (int(month)>datetime.date.today().month):
		age = thisyear - yearint -1
	else:
		age = thisyear - yearint
	print ("You are "+str(age) +" years old.")

def main():
	year = input("Enter year of birth:")
	month = input("Enter month of birth:")
	day = input("Enter day of birth:")
	if check_birthdate(year,month,day):
		calculate_age(year,month,day)
	else:
		print("Date is invalid")




if __name__ == '__main__':
	main()
