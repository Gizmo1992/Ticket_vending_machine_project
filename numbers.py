def ticketformat(function):

    def printing():
        print(f"Your number is:\n{next(function())}\nPlease wait and someone\nwill be there for you\nshortly.")

    return printing

perf_num=0
med_num=0
cos_num = 0
choice=str


@ticketformat
def perfumes():
    global perf_num
    while True:
        perf_num+=1
        yield f"    P-{perf_num}"


med_num=0
@ticketformat
def medicine():
    global med_num
    while True:
        med_num+=1
        yield f"    M-{med_num}"


@ticketformat
def cosmetics():
    global cos_num
    while True:
        cos_num+=1
        yield f"    C-{cos_num}"

def menu():
    choice=input("""
Please select one option below:
    1. Perfumes
    2. Cosmetics
    3. Medicine
    4. Cancel
    """)
    if choice == "1":
        perfumes()
    elif choice == "2":
        cosmetics()
    elif choice == "3":
        medicine()
    elif choice == "4":
        print("Goodbye! See you soon!")
        quit()






