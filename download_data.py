from huggingface_hub import snapshot_download
import os


save_path = "./assets/datasets"
os.makedirs(save_path,exist_ok=True)

print('dowloading data')
snapshot_download(
    repo_id="vida-adl/CARE-PD",
    repo_type="dataset",
    local_dir=save_path
)

print('data downloaded')
