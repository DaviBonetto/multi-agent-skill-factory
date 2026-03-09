# Saving Results to Hugging Face Hub
**⚠️ CRITICAL:** Job environments are ephemeral. ALL results are lost when a job completes unless persisted to the Hub or external storage.
...
## Key Takeaway
**Without `secrets={"HF_TOKEN": "$HF_TOKEN"}` and persistence code, all results are permanently lost.**
Always verify both are configured before submitting any job that produces results.