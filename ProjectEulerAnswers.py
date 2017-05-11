"""
Module that contains functions that solve Project Euler propblems.
"""

# The import of print_function can be removed if running on Python 2.4.
from __future__ import print_function  # Python 2.6 or 2.7 required

from sys import version_info
import time


def sum_of_divs(num):
    if num == 1:
        return 0
    t = 1

    if num % 2 != 0:
        initial = 3
        step = 2
    else:
        initial = 2
        step = 1

    if int(num ** 0.5) ** 2 == num:
        t += int(num ** 0.5)
        end = int(num ** 0.5)
    else:
        end = int(num ** 0.5) + 1

    for i in xrange(initial, end, step):
        if num % i == 0:
            t += i + num / i

    return t


def prob1(limit=1000):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    a = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            a += i
    return a


def prob2(limit=4000000):
    """
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    """
    a = 0
    n1 = 1
    n2 = 2
    while True:
        t = n1 + n2
        n1 = n2
        n2 = t
        if n2 > limit:
            break
        if n2 % 2 == 0:
            a += n2
    return a + 2


def prob3(num=600851475143):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    a = []
    b = 1
    i = 3

    while True:
        if b == num:
            break
        elif num % i == 0:
            b *= i
            a.append(i)
        i += 1

    return max(a)


def prob4(dig=3):
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    limit = 10 ** dig - 1

    a = []

    for i in range(limit, 0, -1):

        for j in range(limit, i - 1, -1):
            prod = str(i * j)

            #if len(prod) % 2 == 0:
            half = len(prod) / 2
            palin = [0] * half
            for k in range(half):
                if prod[k] == prod[-k - 1]:
                    palin[k] = 1
                    #print range(half), prod, k, k-1
                    #print palin
            if 0 not in palin:
                a.append(int(prod))

    return max(a)


def prob5(limit=20):
    """
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    """
    a = 2

    for i in range(2, limit + 1):
        if a % i != 0:
            if i % (a % i) != 0:
                a *= i
            else:
                a *= i / (a % i)
    return a


def prob6(limit=100):
    """
    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 552 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    """
    a = 0
    b = 0

    for i in range(1, limit + 1):
        a += i ** 2
        b += i
    return b ** 2 - a


def prob7(num=10001):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?
    """
    a = 2       # Number to test for primality
    #ith = 1     # Ordinality of prime
    primes = []
    add = 4

    while len(primes) < num:
        #print a
        if a == 2:
            primes.append(a)
            a += 1
            continue
        elif a == 3:
            primes.append(a)
            a += 2
            continue
        else:
            if add == 4:
                add = 2
            else:
                add = 4
            for i in primes:
                #print add
                if a % i == 0:
                    a += add
                    break
                elif i > a ** 0.5:    # If no factors below a's root then prime
                    primes.append(a)
                    a += add
                    break
    return primes[-1]


def prob8(consec=5):
    """
    Find the greatest product of five consecutive digits from the 1000-digit
    number below.
    """
    num = ('73167176531330624919225119674426574742355349194934'
           '96983520312774506326239578318016984801869478851843'
           '85861560789112949495459501737958331952853208805511'
           '12540698747158523863050715693290963295227443043557'
           '66896648950445244523161731856403098711121722383113'
           '62229893423380308135336276614282806444486645238749'
           '30358907296290491560440772390713810515859307960866'
           '70172427121883998797908792274921901699720888093776'
           '65727333001053367881220235421809751254540594752243'
           '52584907711670556013604839586446706324415722155397'
           '53697817977846174064955149290862569321978468622482'
           '83972241375657056057490261407972968652414535100474'
           '82166370484403199890008895243450658541227588666881'
           '16427171479924442928230863465674813919123162824586'
           '17866458359124566529476545682848912883142607690042'
           '24219022671055626321111109370544217506941658960408'
           '07198403850962455444362981230987879927244284909188'
           '84580156166097919133875499200524063689912560717606'
           '05886116467109405077541002256983155200055935729725'
           '71636269561882670428252483600823257530420752963450')

    i = 0
    biggest = 0

    while i + consec <= len(num):
        digits = num[i:i + consec]
        #print digits
        temp = reduce(lambda x, y: int(x) * int(y), digits)
        #print a2
        if temp > biggest:
            biggest = temp
        i += 1

    return biggest


def prob9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which, a**2 + b**2 = c**2

    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    a = 1

    while True:
        for i in range(2, 1000):
            b = i
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
        a += 1


def prob10(limit=2000000):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    #a = 2       # Number to test for primality
    #primes = []
    #add = 4
    #
    #while a < limit:
    #    #print a
    #    if a == 2:
    #        primes.append(a)
    #        a += 1
    #        continue
    #    elif a == 3:
    #        primes.append(a)
    #        a += 2
    #        continue
    #    else:
    #        if add == 4:
    #            add = 2
    #        else:
    #            add = 4
    #        for i in primes:
    #            #print add
    #            if a % i == 0:
    #                a += add
    #                break
    #            elif i > a**0.5:    # If no factors below a's root then prime
    #                primes.append(a)
    #                a += add
    #                break
    #return reduce(lambda x,y: x+y, primes)

    sieve = range(limit)
    #print sieve
    sieve[1] = 0
    for n in xrange(4, limit, 2):
        sieve[n] = 0
    for n in xrange(3, int(limit ** 0.5), 2):
        if sieve[n]:
            for m in xrange(n ** 2, limit, 2 * n):
                sieve[m] = 0
    return sum(sieve)


def prob11(num=4):
    """
    In the 20*20 grid below, four numbers along a diagonal line have been
    marked in red.

    The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

    What is the greatest product of four adjacent numbers in any direction
    (down, right, or diagonally) in the 20*20 grid?
    """
    grid = ['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08',
            '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00',
            '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65',
            '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91',
            '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',
            '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',
            '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',
            '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',
            '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',
            '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',
            '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',
            '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',
            '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',
            '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',
            '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',
            '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',
            '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36',
            '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16',
            '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54',
            '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48']

    for i, row in enumerate(grid):
        #grid[i] = grid[i].split()
        #grid[i] = map(lambda x: int(x), grid[i])
        grid[i] = [int(x) for x in row.split()]

    #print grid[18][19]

    biggest = 0
    i = 0
    #print range(20-num)

    # Verticle
    for r in range(20 - num + 1):
        for c in range(20):
            prod = 1
            for i in range(num):
                prod *= grid[r + i][c]
            if prod > biggest:
                biggest = prod

    # Horizontal
    for r in range(20):
        for c in range(20 - num + 1):
            prod = 1
            for i in range(num):
                prod *= grid[r][c + i]
            if prod > biggest:
                biggest = prod

    # Left Diagonal
    for r in range(20 - num + 1):
        for c in range(20 - num + 1):
            prod = 1
            for i in range(num):
                prod *= grid[r + i][c + i]
            if prod > biggest:
                biggest = prod

    # Right Diagonal
    for r in range(20 - num + 1):
        for c in range(num - 1, 20):
            prod = 1
            for i in range(num):
                prod *= grid[r + i][c - i]
            if prod > biggest:
                biggest = prod

    return biggest


def prob12(limit=500):
    """The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred
    divisors?
    """
    tri = 0     # triangle number
    add = 0
    divs = 0
    while divs <= limit:
        #print
        divs = 0
        add += 1
        tri += add
        # each divisor below rt has one above
        for i in range(1, int(tri ** 0.5) + 1):
            if tri % i == 0:
                divs += 2
        if tri == (int(tri ** 0.5) ** 2):   # if perfect square only one divisor
            divs -= 1                   # so correct
        #print 'divs', divs
        #print tri
    return tri


def prob13():
    """
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.
    """
    nums = [37107287533902102798797998220837590246510135740250,
            46376937677490009712648124896970078050417018260538,
            74324986199524741059474233309513058123726617309629,
            91942213363574161572522430563301811072406154908250,
            23067588207539346171171980310421047513778063246676,
            89261670696623633820136378418383684178734361726757,
            28112879812849979408065481931592621691275889832738,
            44274228917432520321923589422876796487670272189318,
            47451445736001306439091167216856844588711603153276,
            70386486105843025439939619828917593665686757934951,
            62176457141856560629502157223196586755079324193331,
            64906352462741904929101432445813822663347944758178,
            92575867718337217661963751590579239728245598838407,
            58203565325359399008402633568948830189458628227828,
            80181199384826282014278194139940567587151170094390,
            35398664372827112653829987240784473053190104293586,
            86515506006295864861532075273371959191420517255829,
            71693888707715466499115593487603532921714970056938,
            54370070576826684624621495650076471787294438377604,
            53282654108756828443191190634694037855217779295145,
            36123272525000296071075082563815656710885258350721,
            45876576172410976447339110607218265236877223636045,
            17423706905851860660448207621209813287860733969412,
            81142660418086830619328460811191061556940512689692,
            51934325451728388641918047049293215058642563049483,
            62467221648435076201727918039944693004732956340691,
            15732444386908125794514089057706229429197107928209,
            55037687525678773091862540744969844508330393682126,
            18336384825330154686196124348767681297534375946515,
            80386287592878490201521685554828717201219257766954,
            78182833757993103614740356856449095527097864797581,
            16726320100436897842553539920931837441497806860984,
            48403098129077791799088218795327364475675590848030,
            87086987551392711854517078544161852424320693150332,
            59959406895756536782107074926966537676326235447210,
            69793950679652694742597709739166693763042633987085,
            41052684708299085211399427365734116182760315001271,
            65378607361501080857009149939512557028198746004375,
            35829035317434717326932123578154982629742552737307,
            94953759765105305946966067683156574377167401875275,
            88902802571733229619176668713819931811048770190271,
            25267680276078003013678680992525463401061632866526,
            36270218540497705585629946580636237993140746255962,
            24074486908231174977792365466257246923322810917141,
            91430288197103288597806669760892938638285025333403,
            34413065578016127815921815005561868836468420090470,
            23053081172816430487623791969842487255036638784583,
            11487696932154902810424020138335124462181441773470,
            63783299490636259666498587618221225225512486764533,
            67720186971698544312419572409913959008952310058822,
            95548255300263520781532296796249481641953868218774,
            76085327132285723110424803456124867697064507995236,
            37774242535411291684276865538926205024910326572967,
            23701913275725675285653248258265463092207058596522,
            29798860272258331913126375147341994889534765745501,
            18495701454879288984856827726077713721403798879715,
            38298203783031473527721580348144513491373226651381,
            34829543829199918180278916522431027392251122869539,
            40957953066405232632538044100059654939159879593635,
            29746152185502371307642255121183693803580388584903,
            41698116222072977186158236678424689157993532961922,
            62467957194401269043877107275048102390895523597457,
            23189706772547915061505504953922979530901129967519,
            86188088225875314529584099251203829009407770775672,
            11306739708304724483816533873502340845647058077308,
            82959174767140363198008187129011875491310547126581,
            97623331044818386269515456334926366572897563400500,
            42846280183517070527831839425882145521227251250327,
            55121603546981200581762165212827652751691296897789,
            32238195734329339946437501907836945765883352399886,
            75506164965184775180738168837861091527357929701337,
            62177842752192623401942399639168044983993173312731,
            32924185707147349566916674687634660915035914677504,
            99518671430235219628894890102423325116913619626622,
            73267460800591547471830798392868535206946944540724,
            76841822524674417161514036427982273348055556214818,
            97142617910342598647204516893989422179826088076852,
            87783646182799346313767754307809363333018982642090,
            10848802521674670883215120185883543223812876952786,
            71329612474782464538636993009049310363619763878039,
            62184073572399794223406235393808339651327408011116,
            66627891981488087797941876876144230030984490851411,
            60661826293682836764744779239180335110989069790714,
            85786944089552990653640447425576083659976645795096,
            66024396409905389607120198219976047599490197230297,
            64913982680032973156037120041377903785566085089252,
            16730939319872750275468906903707539413042652315011,
            94809377245048795150954100921645863754710598436791,
            78639167021187492431995700641917969777599028300699,
            15368713711936614952811305876380278410754449733078,
            40789923115535562561142322423255033685442488917353,
            44889911501440648020369068063960672322193204149535,
            41503128880339536053299340368006977710650566631954,
            81234880673210146739058568557934581403627822703280,
            82616570773948327592232845941706525094512325230608,
            22918802058777319719839450180888072429661980811197,
            77158542502016545090413245809786882778948721859617,
            72107838435069186155435662884062257473692284509516,
            20849603980134001723930671666823555245252804609722,
            53503534226472524250874054075591789781264330331690]

    return str(reduce(lambda x, y: x + y, nums))[0:10]


def prob14(limit=1000000):
    """
    The following iterative sequence is defined for the set of positive
    integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    dic = {}
    for i in range(1, limit):
        num = i
        count = 1
        while True:
            if num == 1:
                dic[i] = count
                break
            elif num in dic:
                # if the count for num is already in dic, add that
                dic[i] = count + dic[num]
                break
            elif num % 2 == 0:
                num /= 2
            else:
                num = 3 * num + 1
            count += 1
    #print dic

    if version_info >= (2, 5):
        return max(dic, key=dic.get)
    else:  # Python 2.4 compatible
        chain = max(dic.values())
        for key in dic:
            if dic[key] == chain:
                return key


def prob15(size=20):
    """
    Starting in the top left corner of a 2*2 grid, there are 6 routes (without
    backtracking) to the bottom right corner.

    How many routes are there through a 20*20 grid?
    """
    a = 1
    for i in range(1, size + 1):
        #print a
        a = a * (size + i) / i
    return a


def prob16(power=1000):
    """
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2**1000?
    """
    prod = list(str(2 ** power))
    return reduce(lambda x, y: int(x) + int(y), prod)


def prob17(limit=1000):
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance with
    British usage.
    """
    digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    exceptions = {10: 'ten', 11: 'eleven', 12: 'twelve', 14: 'fourteen'}

    bases = {2: 'twen', 3: 'thir', 4: 'for', 5: 'fif',
             6: 'six', 7: 'seven', 8: 'eigh', 9: 'nine'}

    powers = {1: 'teen', 10: 'ty', 100: 'hundred', 1000: 'thousand'}

    count = 0

    for num in range(1, limit + 1):
        right = str(num)[-2:]
        #print right
        if int(right) == 0:
            pass
        elif int(right) in exceptions:
            count += len(exceptions[int(right)])
        elif 10 < int(right) < 20:
            count += len(bases[int(right[1])]) + len(powers[1])
        else:
            if right[-1] != '0':
                count += len(digits[int(right[-1])])
            if len(right) == 2 and right[0] != '0':
                count += len(bases[int(right[0])]) + len(powers[10])

        if len(str(num)) > 2:
            left = str(num)[:-2]
            #print left
            if right != '00':
                count += 3
            if left[-1] != '0':
                count += len(digits[int(left[-1])]) + len(powers[100])
            if len(left) == 2 and left[0] != '0':
                count += len(digits[int(left[0])]) + len(powers[1000])

    return count


def prob18(triangle='triangle3.txt'):
    """
    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

    triangle1.txt

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    triangle2.txt

    NOTE: As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, Problem 67, is the same challenge with a
    triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)
    """
    a = open(triangle)
    tri = []
    i = 0

    for line in a:
        tri.append([int(x) for x in line.split()])
        i += 1

    a.close()

    for row in reversed(range(len(tri) - 1)):
        for i in range(len(tri[row])):
            #print tri
            if tri[row + 1][i] > tri[row + 1][i + 1]:
                tri[row][i] += tri[row + 1][i]
            else:
                tri[row][i] += tri[row + 1][i + 1]

    return tri[0][0]


def prob19():
    """
    You are given the following information, but you may prefer to do some
    research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
    """
    d_in_m = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
              8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    count = 0
    d_in_w = -1  # Day in week with Mon = 0
    day = 0    # Starting Monday 1900-01-01

    for yr in xrange(1900, 2001):
        for mn in xrange(1, 13):
            #print "{0}-{1:02}".format(yr, mn)
            if (day - d_in_w) % 7 == 0:
                #print "Day!"
                if yr != 1900:
                    count += 1

            if mn == 2:         # February calculation
                if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
                    day += 29
                else:
                    day += 28
            else:
                day += d_in_m[mn]
            #print day
    return count


def prob20(num=100):
    """
    n! means n * (n - 1) * ... * 3 * 2 * 1

    For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the
    digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """
    fact = reduce(lambda x, y: int(x) * int(y), range(1, num + 1))
    return reduce(lambda x, y: int(x) + int(y), list(str(fact)))


def prob21(limit=10000):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).
    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """

    total = 0

    for a in xrange(2, limit):
        sum_a = sum_of_divs(a)

        b = sum_a

        if b > a:
            sum_b = sum_of_divs(sum_a)

            if a == sum_b and a != b:
                #print a, b
                total += a + b
    return total


def prob22(f='names.txt'):
    """
    Using names.txt, a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical
    position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So,COLIN would obtain a score of 938 * 53 = 49714.

    What is the total of all the name scores in the file?
    """
    namefile = open(f)
    names = namefile.readlines()[0].split('","')
    namefile.close()
    names[0] = names[0].strip('"')
    names[-1] = names[-1].strip('"')

    names.sort()
    #print range(ord('A'), ord('Z') + 1)
    #ab = map(chr, range(ord('A'), ord('Z') + 1))
    #print ab
    ab = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    ab = dict(zip(ab, range(1, 27)))

    index = 0
    ans = 0

    for name in names:
        index += 1
        name_t = 0

        for l in name:
            name_t += ab[l]

        ans += name_t * index

    return ans


def prob23():
    """
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper
    limit cannot be reduced any further by analysis even though it is known
    that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    """

    abuns = []

    for i in xrange(12, 28123 - 12 + 1):
        if sum_of_divs(i) > i:
            abuns.append(i)

    #print len(abuns)

    tests = range(28123 + 1)

    for i in xrange(len(abuns)):
        j = i

        try:
            while j < len(abuns) and abuns[i] + abuns[j] < len(tests):
                tests[abuns[i] + abuns[j]] = 0
                j += 1
        except IndexError:
            print(i, j)
            print(abuns[i] + abuns[j])
            raise

    #print tests
    return sum(tests)


if __name__ == '__main__':

    time_all = 1        # Flag for whether all problems will be timed
    prob = 22
    value = None

    if time_all == 1:
        if version_info >= (2, 7):
            print("{:7}  {:8}  {}".format('Problem', 'Time (s)', 'Solution'))
        elif version_info == (2, 6):  # Python 2.6 requires field names
            print("{0:7}  {1:8}  {2}".format('Problem', 'Time (s)', 'Solution'))
        else:  # Python 2.4 compatible
            print("%7s  %8s  %s" % ('Problem', 'Time (s)', 'Solution'))

        for problem in range(1, 24):
            start = time.clock()

            solution = globals()['prob' + str(problem)]()

            stop = time.clock()
            elapsed = stop - start

            if version_info >= (2, 7):
                print("{:7}  {:8.3f}  {}".format(problem, elapsed, solution))
            elif version_info == (2, 6):  # Python 2.6 requires field names
                print("{0:7}  {1:8.3f}  {2}".format(problem, elapsed, solution))
            else:  # Python 2.4 compatible
                print("%7i  %8.3f  %s" % (problem, elapsed, solution))

    elif time_all == 0:
        start = time.clock()

        if value is None:
            solution = globals()['prob' + str(prob)]()
        else:
            solution = globals()['prob' + str(prob)](value)

        stop = time.clock()
        elapsed = stop - start

        print("Problem:", prob)
        print("Solution:", solution)
        print("Time to find solution: %.3f s" % elapsed)
        print()
