import pickle
import numpy as np

all_datasets = ["PD-GaM", "BMCLab", "3DGait", "T-SDU-PD", "DNE", "E-LC", "KUL-DT-T", "T-SDU", "T-LTC"]

for ds in all_datasets:
    with open(f"./assets/datasets/{ds}.pkl","rb") as f:
        data = pickle.load(f)


    total_walks=0
    labels=[]
    durations=[]
    pose_shapes=[]

    for subject in data.values():
        for walk in subject.values():
            total_walks+=1
            labels.append(walk.get("UPDRS_GAIT"))
            durations.append(walk["pose"].shape[0]/ walk["fps"])
            pose_shapes.append(walk["pose"].shape)

    label_counts= {}
    for l in labels:
        label_counts[l]= label_counts.get(l,0)+1

    print(f"\n {'='*50}")
    print(f"Dataset: {ds}")
    print(f"n {'='*50}")
    print(f" subjects:{len(data)}")
    print(f" walks: {total_walks}")
    print(f" FPS: {walk['fps']}")
    print(f" Duration: {np.mean(durations):.1f}s avg, {np.min(durations):.1f}s min, {np.max(durations):.1f}s max")
    print(f" UPDRS labels: {label_counts}")
    
    