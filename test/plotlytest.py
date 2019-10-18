import pandas as pd
import numpy as np
import unittest

# Working on a proposed fix for https://github.com/santosjorge/cufflinks/blob/master/cufflinks/plotlytools.py
#
# Replace the following lines with the code from create_spread below
#
# trace = self.apply(lambda x: x[0] - x[1], axis=1)
# positive = trace.apply(lambda x: x if x >= 0 else pd.np.nan)
# negative = trace.apply(lambda x: x if x < 0 else pd.np.nan)
# trace=pd.DataFrame({'positive':positive,'negative':negative})


def create_spread(self):

    index = []
    positive = []
    negative = []

    previousX = 0
    previousY = 0
    isFirst = True

    diff = self.apply(lambda row: row[0] - row[1], axis=1)
    for (x, y) in diff.iteritems():

        if isFirst:
            isFirst = False
        elif y * previousY < 0:
            slope = (y - previousY) / (x - previousX)
            intersect = y - (slope * x)
            root = -intersect / slope
            index.append(root)
            positive.append(0)
            negative.append(0)

        index.append(x)
        if y > 0:
            positive.append(y)
            negative.append(0)
        elif y < 0:
            positive.append(0)
            negative.append(y)

        previousX = x
        previousY = y

    trace = pd.DataFrame({'positive': positive, 'negative': negative}, index=index)

    return trace


class PlotlyTest(unittest.TestCase):

    def test_spread(self):
        df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
        trace = create_spread(df)
        print(trace)


if __name__ == '__main__':
    unittest.main()
