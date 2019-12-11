
test_out_filename = "../model/ubuntu_test_out-29000.txt"

with open(test_out_filename, 'r') as f:
	cur_q_id = None
	num_query = 0
	recall = {"recall@1": 0,
			  "recall@2": 0,
			  "recall@5": 0}

	lines = f.readlines()
	for line in lines[1:]:
		line = line.strip().split('\t')
		line = [float(ele) for ele in line]

		if cur_q_id is None:
			cur_q_id = line[0]
			num_query += 1
		elif line[0] != cur_q_id:
			cur_q_id = line[0]
			num_query += 1

		if line[4] == 1.0:
			rank = line[3]

			if rank <= 1:
				recall["recall@1"] += 1
			if rank <= 2:
				recall["recall@2"] += 1
			if rank <= 5:
				recall["recall@5"] += 1

	recall["recall@1"] = recall["recall@1"] / float(num_query)
	recall["recall@2"] = recall["recall@2"] / float(num_query)
	recall["recall@5"] = recall["recall@5"] / float(num_query)
	print("num_query = {}".format(num_query))
	print("recall@1 = {}".format(recall["recall@1"]))
	print("recall@2 = {}".format(recall["recall@2"]))
	print("recall@5 = {}".format(recall["recall@5"]))

'''
#-----------41000----------
Accuracy: 0.8483771505333693, Precision: 0.3859952756273827  Recall: 0.8723044397463002  F1: 0.5351751868601549 Loss: 0.35136242262608064
MAP (mean average precision: 0.8419946348870913	MRR (mean reciprocal rank): 0.8419946348870913	Top-1 precision: 0.7484672304439747	Num_query: 18920

num_query = 18920
recall@1 = 0.7484672304439747
recall@2 = 0.8676532769556026
recall@5 = 0.973784355179704

#-----------29000----------
num_query = 18920
recall@1 = 0.7457188160676532
recall@2 = 0.8633720930232558
recall@5 = 0.9729915433403805
'''
