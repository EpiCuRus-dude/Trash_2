gpu_resources = faiss.StandardGpuResources()
vector_dim = 128
gpu_config = faiss.GpuIndexFlatConfig()
gpu_config.device = 0  # Use the first GPU
gpu_index = faiss.GpuIndexFlatL2(gpu_resources, vector_dim, gpu_config)
