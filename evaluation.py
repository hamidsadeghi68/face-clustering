from sklearn import metrics

def calculate_f_measure(labels_true, labels_pred, beta=1.0):
  [[tn, fp], [fn, tp]] = metrics.cluster.pair_confusion_matrix(labels_true, labels_pred)
  precision = tp/(tp + fp)
  recall = tp/(tp + fn)
  f_measure = (beta*beta + 1)*precision*recall/(beta*beta*precision + recall)
  return f_measure

def evaluate_clustering(labels, predictions, beta=1.0):
  rand_index = metrics.rand_score(labels, predictions)
  nmi = metrics.normalized_mutual_info_score(labels, predictions)
  f_measure = calculate_f_measure(labels, predictions, beta=beta)
  print('Rand Index: %f, NMI: %f, F-measure: %f' % (rand_index, nmi, f_measure))
  return