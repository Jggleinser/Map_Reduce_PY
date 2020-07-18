from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from functools import reduce
import time
from math import log

def get_single():
    thislist = []
    with open("WarAndPeace.txt", encoding="utf8") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            thislist.append(c)
    return thislist       

def get_double():
    thislist = []
    with open("WarAndPeace.txt", encoding="utf8") as f:
        while True:
            c = f.read(2)
            if not c:
                break
            thislist.append(c)
    return thislist

def get_triple():
    thislist = []
    with open("WarAndPeace.txt", encoding="utf8") as f:
        while True:
            c = f.read(3)
            if not c:
                break
            thislist.append(c)
    return thislist

def countf(s):
    return {s : bookSingle.count(s)}

def countfDouble(s):
    return {s : bookDouble.count(s)}
    
def countfTriple(s):
    return {s : bookTriple.count(s)}

bookSingle = get_single()
bookDouble = get_double()
bookTriple = get_triple()

#PROCESSOR FORMAT
def multiply(s):
    return s * s
if __name__ == '__main__':
    dictOfWords = { i : 0 for i in bookSingle }
    start_time = time.time()
    p = Pool(6)
    result = p.map(countf, dictOfWords)
    resulta = p.map(print, result)
    p.close()
    p.join() 
    print (time.time() - start_time)

###1 10.3976 10.18545 10.250999689102173
###2 6.801 6.4809 6.5566 6.728395
###3 5.964 5.945369720458984 5.862793
###4 5.60399 5.5927 5.807999849319458
###5 6.00999 5.78599 5.777
###6 6.323677 6.44 6.401




##Thread FORMAT
'''
def main():
   start_time = time.time()
   dictOfWords = { i : 0 for i in bookSingle } 
   with ThreadPoolExecutor(max_workers = 1) as executor:  
        results = executor.map(countf, dictOfWords)
        for result in results:
            first = next(iter(result.values()))
            print(str(result) + " " + str((first / len(bookSingle))))

            
   print (time.time() - start_time)  

if __name__ == '__main__':
   main()

def main():
   start_time = time.time()
   dictOfWords = { i : 0 for i in bookDouble } 
   with ThreadPoolExecutor(max_workers = 16) as executor:  
        results = executor.map(countfDouble, dictOfWords)
        sig = 0
        for result in results:
            first = next(iter(result.values()))
            sig+=first * (-1 * first / len(bookDouble)) *(log(first / len(bookDouble), 2))
            print(str(result) + " " + str((first / len(bookDouble))) + " " + str(sig))
   print (time.time() - start_time)  
#2 84.01469564437866
#2 85.75299406051636
if __name__ == '__main__':
   main()

def main():
   start_time = time.time()
   dictOfWords = { i : 0 for i in bookTriple } 
   with ThreadPoolExecutor(max_workers = 1) as executor:  
        results = executor.map(countfTriple, dictOfWords)
        for result in results:
            first = next(iter(result.values()))
            print(str(result) + " " + str((first / len(bookTriple))))
   print (time.time() - start_time)  

if __name__ == '__main__':
   main(
'''           


#122.168412
#115.11187744140625
#116.48743152618408
#116.48743152618408

