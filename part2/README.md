# Data Analysis of News Articles

This project involves analyzing news articles' descriptions using data fetched from the News API. The analysis focuses on the description lengths and their relationship with different features such as year, source, and month.

## Dataset

The dataset is retrieved from the News API and contains the following columns:

- **title**: Title of the news article
- **description**: Description of the news article
- **publishedAt**: Date the article was published
- **url**: URL of the article
- **source**: Source of the article (e.g., 'Business Insider', 'Fortune', etc.)
- **year**: Year the article was published
- **month**: Month the article was published
- **day_of_week**: Day of the week the article was published
- **description_length**: Length of the article's description

## Requirements

To run the code, the following libraries are required:
- `pandas`
- `numpy`
- `matplotlib`
- `statsmodels`
- `requests`

You can install these libraries using:

```bash
pip install pandas numpy matplotlib statsmodels requests