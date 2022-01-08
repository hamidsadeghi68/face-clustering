# Clustering Algorithms and their Application to Facial Image Analysis



# Introduction

![img](https://user-images.githubusercontent.com/70681172/144739072-353912d2-0fc5-4180-a7ab-5355302a80a5.png)



# Syllabus

Contents of presentation file is as follows:

​	1- **Introduction**<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Machine Learning: Clustering vs Classification and Regression<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Face Clustering

​	2- **Clustering Algorithms**<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Introduction to Clustering Algorithms (Categorization)<br>
&nbsp;&nbsp;&nbsp;&nbsp; - K-means Clustering<br>
&nbsp;&nbsp;&nbsp;&nbsp; - DBSCAN Clustering<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Agglomerative Clustering<br>

​	3- **Evaluation Metrics**<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Purity<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Rand index<br>
&nbsp;&nbsp;&nbsp;&nbsp; - F-measure<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Normalized Mutual Information (NMI)

​	4- **Face Analysis**<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Face Detection<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Face Preprocessing<br>
&nbsp;&nbsp;&nbsp;&nbsp; - Face Recognition<br>
&nbsp;&nbsp;&nbsp;&nbsp; - A Complete Face Clustering System

- [ ] **Download**: Presentation (*coming soon*): [part-1](https://github.com/hamidsadeghi68/face-clustering/raw/main/presentation%20(clustering%20algorithms)-part1.pdf), [part-2](https://github.com/hamidsadeghi68/face-clustering/raw/main/presentation-part2.pdf), [part-3](https://github.com/hamidsadeghi68/face-clustering/raw/main/presentation-part3.pdf), videos (*coming soon*)

# Implementations

- [x] Clustering Algorithms ([K-means](https://github.com/hamidsadeghi68/face-clustering/blob/main/clustering_kmeans.ipynb), [DBSCAN](https://github.com/hamidsadeghi68/face-clustering/blob/main/clustering_dbscan.ipynb), [Agglomerative](https://github.com/hamidsadeghi68/face-clustering/blob/main/clustering_agglomerative.ipynb))

- [x] Evaluation Metrics ([Rand index, F-measure, and NMI](https://github.com/hamidsadeghi68/face-clustering/blob/main/evaluation.py))

- [x] Face Analysis ([MTCNN Face Detection](https://github.com/hamidsadeghi68/face-clustering/blob/main/face_detection_mtcnn.ipynb), [dlib Face Recognition](https://github.com/hamidsadeghi68/face-clustering/blob/main/face_recognition_using_dlib.ipynb), [ArcFace Face Recognition](https://github.com/hamidsadeghi68/face-clustering/blob/main/arcface.ipynb), [Face Clustering](https://github.com/hamidsadeghi68/face-clustering/blob/main/face_clustering_arcface.ipynb), [Face Clustering on FaceCup Sample Dataset](https://github.com/hamidsadeghi68/face-clustering/blob/main/face_clustering_arcface_facecup_samples.ipynb))




# FaceCup dataset

The test dataset is not published for [facecup](https://facecup.ir/) challenge purposes. Sample dataset published for participants contains 899 images. Identity label for each image can be obtained from image file name as follows:

![image](https://user-images.githubusercontent.com/70681172/144975617-a3bff6c2-8a16-48d6-86c1-ba252abf4128.png)



- [ ] **Download**: [Google Drive](https://github.com/hamidsadeghi68/face-clustering) (*coming soon*), [FaceCup](https://facecup.ir/news/cc622bd2-7765-4383-8c39-9e074a5e1286)



# Useful links

- https://github.com/becauseofAI/HelloFace
- https://github.com/ChanChiChoi/awesome-Face_Recognition
- https://github.com/zhoushengisnoob/DeepClustering
- https://github.com/polarisZhao/awesome-face
- https://github.com/RizhaoCai/Awesome-FAS
- https://github.com/clpeng/Awesome-Face-Forgery-Generation-and-Detection
- https://awesomeopensource.com/projects/face-detection
- https://gitlist.top/lists/face-recognition



# References

- C. M. Bishop, [Pattern Recognition and Machine Learning](http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf), Chapter 9: Mixture Models and EM
- Shobha, G., & Rangaswamy, S. (2018). [Chapter 8: Machine Learning](https://www.sciencedirect.com/science/article/abs/pii/S0169716118300191), In Handbook of statistics (Vol. 38, pp. 197-228). Elsevier.
- Rhys, H. [Machine Learning with R, the tidyverse, and mlr. Chapter 17: Hierarchical clustering](https://livebook.manning.com/book/machine-learning-for-mortals-mere-and-otherwise/chapter-17/1) , Simon and Schuster, 2020.
- Christopher, D. M., Prabhakar, R., & Hinrich, S. C. H. U. T. Z. E., "[Introduction to information retrieval](http://155.0.32.9:8080/jspui/bitstream/123456789/1127/1/Introduction%20to%20information%20retrieval%20%28%20PDFDrive%20%29%20-%20Copy.pdf).", Chapter 16: Flat clustering (2008).
- Zhang, Kaipeng, et al. "[Joint face detection and alignment using multitask cascaded convolutional networks.](https://arxiv.org/pdf/1604.02878)" IEEE Signal Processing Letters 23.10 (2016): 1499-1503.
- Viola, P., & Jones, M., [Rapid object detection using a boosted cascade of simple features](https://merl.com/publications/docs/TR2004-043.pdf). CVPR 2001. 
- F. Comaschi, et al. "[RASW: a run-time adaptive sliding window to improve viola-jones object detection](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.719.4174&rep=rep1&type=pdf)." *2013 Seventh International Conference on Distributed Smart Cameras (ICDSC)*. IEEE, 2013.
- Deng, J., et al. [Retinaface: Single-shot multi-level face localisation in the wild](https://openaccess.thecvf.com/content_CVPR_2020/papers/Deng_RetinaFace_Single-Shot_Multi-Level_Face_Localisation_in_the_Wild_CVPR_2020_paper.pdf). CVPR 2020 (pp. 5203-5212).
- Wang, M., & Deng, W. (2021). [Deep face recognition: A survey](https://arxiv.org/pdf/1804.06655.pdf?source=post_page---------------------------). Neurocomputing, *429*, 215-244.
- Taigman, Y., et al. [Deepface: Closing the gap to human-level performance in face verification](https://openaccess.thecvf.com/content_cvpr_2014/papers/Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf). CVPR 2014 (pp. 1701-1708).
- Schroff, F., et al. [Facenet: A unified embedding for face recognition and clustering](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Schroff_FaceNet_A_Unified_2015_CVPR_paper.pdf). CVPR 2015 (pp. 815-823).
- Deng, J., et al. [Arcface: Additive angular margin loss for deep face recognition](https://openaccess.thecvf.com/content_CVPR_2019/papers/Deng_ArcFace_Additive_Angular_Margin_Loss_for_Deep_Face_Recognition_CVPR_2019_paper.pdf). CVPR 2019 (pp. 4690-4699).
- Ester, M., et al. "[A density-based algorithm for discovering clusters in large spatial databases with noise](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf?source=post_page)." *kdd*. Vol. 96. No. 34. 1996.
- Schubert, E., et al. (2017). [DBSCAN revisited, revisited: why and how you should (still) use DBSCAN](http://www.ccs.neu.edu/home/vip/teach/DMcourse/2_cluster_EM_mixt/notes_slides/revisitofrevisitDBSCAN.pdf). ACM Transactions on Database Systems (TODS), *42*(3), 1-21.
- Silva, M., et al. "[Agglomerative concentric hypersphere clustering applied to structural damage detection](https://www.researchgate.net/profile/Moises-Silva-11/publication/313238175_Agglomerative_concentric_hypersphere_clustering_applied_to_structural_damage_detection/links/5b57403b0f7e9b240f0548df/Agglomerative-concentric-hypersphere-clustering-applied-to-structural-damage-detection.pdf)." Mechanical Systems and Signal Processing 92 (2017): 196-212.
- Canziani, A., et al. "[An analysis of deep neural network models for practical applications](https://arxiv.org/pdf/1605.07678.pdf?source=post_page---------------------------)." *arXiv preprint arXiv:1605.07678*, 2016.
- Bianco, S., et al. "[Benchmark analysis of representative deep neural network architectures](https://ieeexplore.ieee.org/iel7/6287639/6514899/08506339.pdf)." *IEEE Access*, *6*, 64270-64277, 2018.
- https://github.com/ipazc/mtcnn
- https://github.com/deepinsight/insightface
- https://en.wikipedia.org/wiki/Cluster_analysis
- https://scikit-learn.org/stable/modules/clustering.html
