# your code for function average goes here
def average(list):
    if len(list) > 0:
        return sum(list)/len(list)
    else:
        return 0

if __name__ == "__main__":
    list = [10, 20, 30, 40, 50]
    # and here