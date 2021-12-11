def match(template1, template2, metric='Euclidian'):
    #assert (template1.size == 512)
    #assert (template2.size == 512)
    assert (template1.size == template2.size)

    if metric='Euclidian':
		# Euclidian distance
	    diff = np.subtract(template1, template2)
	    return np.sqrt(np.sum(np.square(diff), 1))
	elif metric='Cosine'
		# Cosine Similarity
		return np.dot(template1, template2.T)
	else
		raise Exception("input metric must be Euclidian or Cosine!")