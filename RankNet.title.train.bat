java -jar RankLib-2.15.jar -train MQ2007/Fold1/train.txt  -validate MQ2007/Fold1/vali.txt -ranker 1 -feature MQ2007/Fold1/titlefeatures.txt  -metric2t NDCG@10  -save titlemodels/f1.RankNet.title.txt 
java -jar RankLib-2.15.jar -train MQ2007/Fold2/train.txt  -validate MQ2007/Fold2/vali.txt -ranker 1 -feature MQ2007/Fold2/titlefeatures.txt  -metric2t NDCG@10  -save titlemodels/f2.RankNet.title.txt 
java -jar RankLib-2.15.jar -train MQ2007/Fold3/train.txt  -validate MQ2007/Fold3/vali.txt -ranker 1 -feature MQ2007/Fold3/titlefeatures.txt  -metric2t NDCG@10  -save titlemodels/f3.RankNet.title.txt 
java -jar RankLib-2.15.jar -train MQ2007/Fold4/train.txt  -validate MQ2007/Fold4/vali.txt -ranker 1 -feature MQ2007/Fold4/titlefeatures.txt  -metric2t NDCG@10  -save titlemodels/f4.RankNet.title.txt
java -jar RankLib-2.15.jar -train MQ2007/Fold5/train.txt  -validate MQ2007/Fold5/vali.txt -ranker 1 -feature MQ2007/Fold5/titlefeatures.txt  -metric2t NDCG@10  -save titlemodels/f5.RankNet.title.txt 

