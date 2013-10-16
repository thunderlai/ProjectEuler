class Untitled:

    def answer(self):
        return 42

    def factorize(self, n):
        # take a number n and return a list of its factors.
        # how to prime factorize?
        primefactors = []
        # don't include 1
        limit = n+1
        for x in range(2, limit):
            if n % x == 0:
                # add x to the primefactors
                primefactors.append(x)
                primefactors.extend(self.factorize(n/x))
                break  
        return primefactors

    # can we use a list comprehension?
    # primefactors = [factorize(x) for x in range(2, n/2)]