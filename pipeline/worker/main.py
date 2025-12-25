import json
import time
from worker.redis_client import RedisClient
from pipeline_runner import Pipeline

def main():
    client = RedisClient()
    
    # while True:
    print("OASKDPASOKDPOSADK")
    job = client.dequeue_blocking("repo_jobs", 5)
    print("FUCK")
    if job is None:
        return
        # continue
    
    payload = json.loads(job.decode("utf-8"))
    repo_path = payload["repo_path"]
    pipeline = Pipeline()
    
    try:
        pipeline.run(repo_path)
        print("FAGGITO")
    except Exception as e:
        print(f"worker pipeline failed for {repo_path}: {e}")
        client.lpush("repo_jobs", json.dumps(payload))
        time.sleep(1)
        
if __name__ == "__main__":
    main()