import numpy as np

def get_indices(N, n_batches, split_ratio):
    j = ((N-1) / (n_batches*split_ratio+1))
    inds = np.array([0, j, (j*(1+split_ratio))])
    for i in range(n_batches):
        yield np.array(inds, dtype=int)
        inds += [(j*split_ratio)]*3

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()
