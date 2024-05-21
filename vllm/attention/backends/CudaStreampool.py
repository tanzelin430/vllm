import torch
from vllm.logger import init_logger
logger = init_logger(__name__)
class stream_pool:
    _instance = None

    def __new__(cls, num_streams=2):
        if cls._instance is None:
            cls._instance = super(stream_pool, cls).__new__(cls)
            cls._instance.streams = [torch.cuda.Stream() for _ in range(num_streams)]
            logger.info(f"Created {num_streams} CUDA streams")
        return cls._instance

    def get_stream(self, index):
        if index < 0 or index >= len(self.streams):
            raise ValueError("Invalid stream index")
        return self.streams[index]
