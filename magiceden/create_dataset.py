#ControlNet/training/fill50k/prompt.json
#ControlNet/training/fill50k/source/X.png
#ControlNet/training/fill50k/target/X.png
import os
import json
from typing import List, Dict
import urllib.request as request
from parse import Result, parse_request, Attributes
from canny import create_canny
from resize import resize_save


def create_prompt(source: str, target: str, root: str, attrs: List[Attributes]) -> Dict:
    return dict(
        source=source.replace(root, "")[1:],
        target=target.replace(root, "")[1:],
        prompt="NerdStyle"
        #prompt=" ".join([f"{attr.trait_type}_{attr.value}" for attr in attrs])
    )

def download_image(url: str, file_path, file_name) -> str:
    full_path = os.path.join(file_path, f"{file_name}.{'png'}")
    request.urlretrieve(url, full_path)
    return full_path


def create_dataset(dataset_name: str, request: Dict) -> None:
    root = f"./training/{dataset_name}"
    source_path = f"{root}/source"
    target_path = f"{root}/target"
    raw_path = f"{root}/raw"
    os.makedirs(root, exist_ok=True)
    os.makedirs(raw_path, exist_ok=True)
    os.makedirs(source_path, exist_ok=True)
    os.makedirs(target_path, exist_ok=True)
    with open(os.path.join(root, "prompt.json"), 'w') as f:
        for result in parse_request(request):
            raw_source = download_image(result.img, raw_path, result.title)
            source = resize_save(raw_source, raw_source.replace(raw_path, source_path), 5)
            target = create_canny(source, source.replace(source_path, target_path))
            prompt = create_prompt(target, source, root, result.attributes)
            f.write(json.dumps(prompt) + "\n")


if __name__ == "__main__":
    from crawler import get_nfts
    request_result = get_nfts(100)
    create_dataset("Entreprenerdz", request_result)
