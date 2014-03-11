from mRMR import mrmr
import numpy as np

if __name__=='__main__':
    # Make some data
    N = 100
    data = np.c_[ np.r_[np.random.randn(N,5)+2, np.random.randn(N,5)-2], np.random.randn(N*2,30) ]
    c = [1]*N+[-1]*N
    fn = ['F%d' % n for n in range(5)] + ['f%d' % n for n in range(30)]
    assert data.shape==(len(c),len(fn))

    mrmrout = mrmr(data,fn,c,threshold=0.5)

    R = mrmrout['mRMR']
    print 'Order \t Fea \t Name \t Score'
    for i in range(len(R['Fea'])):
        print '%d \t %d \t %s \t %f' % \
              (i, R['Fea'][i], fn[R['Fea'][i]], R['Score'][i])

    print data.shape
    print len(c)
    