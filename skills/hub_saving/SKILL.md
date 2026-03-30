# Saving Training Results to Hugging Face Hub
**⚠️ CRITICAL:** Training environments are ephemeral. ALL results are lost when a job completes unless pushed to the Hub.
...
## Key Takeaway
**Without `push_to_hub=True` and `secrets={"HF_TOKEN": "$HF_TOKEN"}`, all training results are permanently lost.**

Always verify both are configured before submitting any training job.