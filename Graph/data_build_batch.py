'''
Prepare data in batches

'''
for batch_idx, data in enumerate(unsup_data_loader):
    print(' time: {:.4f}s'.format(time.time() - t))
    t = time.time()
    batch_adj_norm = []
    batch_adj_label = []
    batch_feature = []
    batch_node = []
    batch_mask_list = []

    adj_list, feature, space_grp, node, target = data[0], data[1], data[2], data[3], np.asarray(data[4])
    max_node = max(node)
    bs = np.shape(target)[0]
    print("Max_Node", max_node)
    print("Batch_size", bs)
    for i in range(len(adj_list)):
        # Padded Adjacency
        adj = np.asarray(adj_list[i])
        feat = np.asarray(feature[i])
        length = adj.shape[0]
        pad_len = max_node - length
        adj_p = np.pad(adj, ((0, pad_len), (0, pad_len)), mode='constant')
        adj_n = preprocess_graph(adj_p)
        adj_l = adj_p + np.eye(adj_p.shape[0])
        batch_adj_norm.append(adj_n)
        batch_adj_label.append(adj_l)

        feat_p = np.pad(feat, ((0, pad_len), (0, 0)), mode='constant')
        feat_p = preprocess_features(feat_p)
        batch_feature.append(feat_p)

        mask = np.zeros(max_node)
        mask[:length] = 1
        batch_mask_list.append(mask)

        batch_node.append(length)

    batch_adj_norm = torch.from_numpy(np.stack(batch_adj_norm, 0)).float()
    batch_adj_label = torch.from_numpy(np.stack(batch_adj_label, 0)).float()
    batch_feature = torch.from_numpy(np.stack(batch_feature, 0)).float()
    batch_mask_list = torch.from_numpy(np.stack(batch_mask_list, 0)).float()
    batch_node = torch.from_numpy(np.stack(batch_node, 0)).long()