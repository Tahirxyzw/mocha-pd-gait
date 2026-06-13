from torch.utils.data import Dataset, DataLoader
from scipy.interpolate import interp1d
import pickle
import torch
import numpy as np

class CustomDataset(Dataset):

    def __init__(self, data_dir="./assets/datasets", target_fps=25):
       self.features = []
       self.labels = []
       all_datasets = ["PD-GaM", "BMCLab", "3DGait", "T-SDU-PD", "DNE", "E-LC", "KUL-DT-T", "T-SDU", "T-LTC"]
       for d in all_datasets:
        with open(f"{data_dir}/{d}.pkl", "rb") as f:
            data = pickle.load(f)
        for subject_id,walks in data.items():
            for walk in walks.values():
                pose = walk["pose"]
                trans = walk["trans"]
                fps = walk["fps"]

                if fps != target_fps:
                    duration = pose.shape[0] / fps
                    target_length = int(duration * target_fps)
                    original_times = np.linspace(0, duration, pose.shape[0])
                    target_times = np.linspace(0, duration, target_length)
                    pose = interp1d(original_times, pose, axis=0)(target_times)
                    trans = interp1d(original_times, trans, axis=0)(target_times)

                self.features.append({
                    "pose": pose,
                    "trans": trans,
                    "dataset": d,
                    "subject": f"{subject_id}_{d}"
                })
                self.labels.append(walk['UPDRS_GAIT'])

       


       
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, idx):
       pose = torch.tensor(self.features[idx]["pose"], dtype=torch.float32)
       trans = torch.tensor(self.features[idx]["trans"], dtype=torch.float32)
       label = torch.tensor(self.labels[idx], dtype=torch.long)
       return pose, trans, label

def collate_fn(batch):
   poses,trans,labels=zip(*batch)
   max_lenghth=max(p.shape[0] for p in poses)
   padded_poses=[]
   masks=[]
   padded_trans=[]
   
   for p,t in zip(poses,trans):
      original_length=p.shape[0]
      pad_length=max_lenghth-original_length
      if pad_length>0:
         p=torch.cat([p,torch.zeros(pad_length,p.shape[1])], dim=0)
         t=torch.cat([t,torch.zeros(pad_length,t.shape[1])], dim=0)
         mask=torch.cat([torch.ones(original_length), torch.zeros(pad_length)])
         
      else:
         mask=torch.ones(p.shape[0])
      padded_poses.append(p)
      padded_trans.append(t)
      masks.append(mask)
      
   padded_poses=torch.stack(padded_poses)
   padded_trans=torch.stack(padded_trans)
   return padded_poses, padded_trans,torch.stack(labels), torch.stack(masks)

def get_indices(dataset):
   indices={}
   for i,f in enumerate(dataset.features):
      s=f["subject"]
      if s not in indices:
         indices[s]=[]
      indices[s].append(i)
   return indices