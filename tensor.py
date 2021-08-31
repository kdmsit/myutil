# Torch Tensor Copy
cluster_emb=x.clone() # x is a tensor


##***** Important Code used in Crystal Graph Work ***********
# Graph Embedding
z_G = torch.squeeze(torch.mean(atom_fea, dim=1, keepdim=True), 1)
# Contrastive Loss
loss_func = NTXentLoss(temperature=0.07)
info_nce_loss = loss_func(z_G, torch.Tensor(space_group))
# Atom Feature Matrix Transpose
atom_fea_t = torch.transpose(atom_fea, 1, 2)
# Reconstructed Edge Weight by ZZ^T
edge_prob = torch.bmm(atom_fea, atom_fea_t)
# Reconstructed Atom Feature
atom_feature=self.fc_atom_feature(atom_fea)
# Clone Atom Embedding
emb=torch.clone(atom_fea)