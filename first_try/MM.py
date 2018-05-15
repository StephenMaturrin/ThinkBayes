
from thinkbayes import Suite


class MM(Suite):
    """Map from hypothesis (A or B) to probability."""

    bag_94 = dict(brown=30,yellow=20,red=20,green=10,orange=10,tan=10)

    bag_96 = dict(blue=24,green=20,range=16,yellow=14,red=13,brown=13)

    hypothesis_A = dict(bag1=bag_94, bag2=bag_96)
    hypothesis_B = dict(bag1=bag_96, bag2=bag_94)

    H = dict(A=hypothesis_A, B=hypothesis_B)

    def Likelihood(self, data, hypo):

        bag, color = data
        mix = self.H[hypo][bag]
        like = mix[color]
        return like


class Monty(Suite):

    hypothesis_A = dict(door1=1, door2=0,door3=0)
    hypothesis_B = dict(door1=0, door2=1,door3=0)
    hypothesis_C = dict(door1=0, door2=0,door3=1)
    H = dict(A=hypothesis_A, B=hypothesis_B,C=hypothesis_C)

    def Likelihood(self, data, hypo):
        """Compute the likelihood of the data under the hypothesis.

        hypo: string name of the door where the prize is
        data: string name of the door Monty opened
        """
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

def main():
    suite = MM('AB')
    suite.Update(('bag1', 'yellow'))
    suite.Update(('bag2', 'green'))
    suite.Print()

    suite = Monty('ABC')
    suite.Update('B')
    suite.Print()

#############################################################
#Prior p(H)| Likehood P(D/H) | P(H)P(D/H)| Posteriori P(H/D)|
#____1/3___|_____1/2_________|____1/6____|_____1/3__________|
#____1/3___|_____0___________|____0______|_____0____________|
#____1/3___|_____1___________|____1/3____|_____2/3__________|

# P(D)*P(H/D) = P(H)*P(D/H)
#
#P(H/D) =  P(H)*P(D/H)/ P(D)
#1) P(H) -> chances to chose any door, there are tree so it is 1/3
#2) P(D/H) -> Chances that monty chooses B after I choose any door
#3) P(D) ->

# p(D) is the probability of the data under any hypothesis, called the
# normalizing constant

# In that case we can compute p(D) using the law of total probability, which
# says that if there are two exclusive ways that something might happen, you
# can add up the probabilities like this:
#     p(D) = p(B1) p(D/B1) + p(B2) p(D/B2)

from thinkbayes import Suite


class Dice(Suite):
    """Represents hypotheses about which die was rolled."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: integer number of sides on the die
        data: integer die roll
        """
        if hypo < data:
            return 0
        else:
            return 1.0/hypo


def main():
    suite = Dice([4, 6, 8, 12, 20])

    suite.Update(6)
    print ('After one 6')
    suite.Print()

    for roll in [4, 8, 7, 7, 2]:
        suite.Update(roll)

    print ('After more rolls')
    suite.Print()


if __name__ == '__main__':
    main()

