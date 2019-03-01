from one_hot import one_hot_encoded
from compute_slideshow import compute

one_hot_matrix, tags, orientations = one_hot_encoded('dataset/a_example.txt', verbose=True)

scores = compute(one_hot_matrix)

orientations = orientations.reshape(-1,1)
scores = np.hstack((orientations,scores))


