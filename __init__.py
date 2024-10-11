import multiprocessing

def calc_square(numbers,q):
    pass

if __name__ == "__main__":
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=calc_square,args = (numbers,q))
    pass

