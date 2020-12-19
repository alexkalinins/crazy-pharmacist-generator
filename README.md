# Crazy Pharmacist

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
