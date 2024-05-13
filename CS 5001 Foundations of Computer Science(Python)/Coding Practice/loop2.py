'''

'''

def main():
    counter = 1;
    while counter != -1:
        value = int(input("enter a integer:\n"))
        if value > 0:
            counter += 1
        if counter >10:
            counter -=1
    print("Done!")
        
main()
