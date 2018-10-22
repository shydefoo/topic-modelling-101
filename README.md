Topic modeling crash course.

Method: Latent Dirichlet Allocation
Corpus used: 100 thousand articles from WikiCorpus
Number of topics: 100

# Create conda environment:
` conda create --name lda101 python=3.6`

# Install requirements
` pip install -r requirements.txt `

### Use lda_model_driver.ipynb test topic modelling


# Things to change:
- repo_path `repo_path = ''` replace repo path with location repo was cloned
- Change url to a nytimes article and run cell to view topics scores and associated words.
- Note, scraper might be buggy. This is just a 101
