<p align="center">
  <img src="corvidae-cropped.png">
</p>

# Azure Functions Example relating to the following Medium Post

link to the medium post
# Intro

Data collection at QueryClick is growing, as we build out our platform and move closer to completing our MVP we are looking to the future and revisiting the way we do things. 

Our goal of being able to provide insight to our users in the shortest possible timeframe is a driving force behind us looking at different ways we can manage our data. 

Excluding our clickstream data a lot of our data is "small", and comes in a semi-structured format via API's. Dealing with this data doesn't require a large amount of compute which means we have a couple of options to look into, one of those options is Azure Functions.

# "Basic ETL"

Depending on which part of our product offering you're looking at our ETL pipelines aren’t complex, lots of enrichment and getting a mixture of data sources to play nice. 

Its our simpler workflows where we utilise Azure Functions for ETL, this is mainly because of the size of the data (normally under 50mb) that we are dealing with and the short execution time for the process. 

As you can see from the below we can have a couple of functions do their thing before we get to a point where we are happy with the data.
Utilising Azure Functions allows us get into the meaty bits of the work almost instantly, this is mainly due to their pre-made triggers and the auto generate projects you get from VSCode, more on that to come. 

<p align="center">
  <img src="Example Of Data Collection Service.png">
</p>

# Summary
At the core of it, using Functions means we can spend more time where we can actually provide value, building pipelines that will be used to surface data via our platform, ingested into our models or used in conjunction with other data to feed individual bits of analysis. 

Yeah we may get hit by different problems in the future, like when we have thousands of micro-services doing all kinds off task or when we inevitability hit a workflow that lasts longer than the [standard timeout](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale) of the consumption plan which we currently use. 

For now the positives out-way the negatives for us in this space.
# Missing Files

You may have noticed that the <b>local.settings.json</b> file is missing from the files.
The below is a copy of the innerds of the file for you to copy and paste 

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=putYourValueHere,
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "examplesmalldata_STORAGE": "DefaultEndpointsProtocol=https;AccountName=putYourValueHere
  }
}
```