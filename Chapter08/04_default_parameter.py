# Here in funtion define we are declaring default paramteres mean that if i pass the value for ending then print it and if there is no value pass for the ending then use the value that is default giving at the time of function declaration....

def goodDay(name, ending = "Thank You"):
    print(f"Good Day {name}")
    print(ending)

goodDay("Suhel", "Love You")