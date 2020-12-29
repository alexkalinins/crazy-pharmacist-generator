# Crazy Pharmacist Generator

Have you ever wondered how they come up with names for prescription drugs? 
They seldom describe the function of the medicine or the chemical structure.
They are seemingly pulled out of someone's... head.
    
In this project. I create a Markov chain model that generates fictitious 
medicine names based on real drug brand names gathered from the NDC
(National Drug Code) database. Another model generates descriptions from
text data gathered from Wikipedia.

After parsing drug brand names from NDC database, descriptions were gathered
by through the Wikipedia API. Many requests resulted in errors because the
API takes percise names; many names were duplicates. For all successful
requests, a sentence starting with "used" was extracted from the first
paragraph of the article. Almost all articles have this sentence that
describes the use of the drug.


## Webapp

I wrote a webapp that uses this API in React. You can check it out [here](https://alexkalinins.github.io/crazy-pharmacist/). The source code is also on [GitHub](https://github.com/alexkalinins/crazy-pharmacist).

## Data

Parsed data (both descriptions and drug names) are available in the `data` directory of the repo. For drug brand names, raw data was collected from the [NDC Database](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory). Description data was parsed from Wikipedia articles accessed with the Wikipedia API.


## Built With

- **Node.js** the runtime of the API.
- **Python** for getting data from Wikipedia, building the chain, and prototyping the generator.
- **Java** for parsing NDC database (because of streams API).
- **Serverless** for boostrapping the API
- **AWS Lambda** for hosting.
