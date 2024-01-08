def covert_to_alphabeltic(grade):
    if grade>= 8.5:
        return 'A'
    elif 7<= grade< 8.5:
        return 'B'
    elif 5.5<= grade< 7:
        return 'C'
    elif 4.0<= grade< 5.5:
        return 'D'
    else:
        return 'F'
def convert_to_4th_system(grade):
    if grade>= 8.5:
        return '4'
    elif 7<= grade< 8.5:
        return '3'
    elif 5.5<= grade< 7:
        return '2'
    elif 4.0<= grade< 5.5:
        return '1'
    else:
        return '0'
try:
    n=float(input(" Input the grade in decimal system: "))
    if n>0 and n<=10:
        alphabetic= covert_to_alphabeltic(n)
        fourth_system= convert_to_4th_system(n)
        print(f"the corresponding grade in alphabetic: {alphabetic}")
        print(f"the corresponding grade in four system: {fourth_system}")
    else:
        print("Grade must be from 0 to 10 !")
except ValueError:
    print("Please enter a valid grade !")
        
        
        
    
    