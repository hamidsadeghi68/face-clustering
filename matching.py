import numpy as np

def match(template1, template2, metric='Euclidean'):
    # assert (template1.size == 512)
    # assert (template2.size == 512)
    assert (template1.size == template2.size)

    if metric == 'Euclidean':
        # Euclidean distance
        diff = np.subtract(template1, template2)
        return np.sqrt(np.sum(np.square(diff)))
    elif metric == 'Cosine':
        # Cosine Similarity
        return np.dot(template1, template2.T)
    else:
        raise Exception("input metric must be Euclidean or Cosine!")
