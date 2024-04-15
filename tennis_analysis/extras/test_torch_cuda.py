import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Print CUDA device count
    print(torch.cuda.device_count())
    # Print CUDA device name
    print(torch.cuda.get_device_name(0))
    # Print CUDA version
    print(torch.version.cuda)
else:
    print("CUDA is not available.")