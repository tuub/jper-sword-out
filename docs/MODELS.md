# JPER SWORD OUT Core Models

## Repository Status

```json
{
    "id" : "<id of the repository account>",
    "last_updated" : "<date this record was last updated>",
    "created_date" : "<date this record was created>",
    
    "last_deposit_date" : "<date of analysed date of last deposited notification>",
    "status" : "<succeeding|problem|failing>",
    "retries" : <number of times we've retried against this repo>
    "last_tried" : "<date of last failed attempt to deposit>"
}
```


## Repository Deposit Records

```json
{
    "id" : "<opaque id of the deposit - also used as the local store id for the response content>",
    "last_updated" : "<date this record was last updated>",
    "created_date" : "<date this record was created>",
    
    "repository" : "<account id of the repository>",
    "deposit_date" : "<date of attempted deposit>",
    "metadata_status" : "<deposited|failed>",
    "content_status" : "<deposited|none|failed>",
    "completed_status" : "<deposited|none|failed>"
}
```