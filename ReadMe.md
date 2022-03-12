# NDA Website Crawler

This crawler helps extract information from the [official website of the National Drug Authority](https://www.nda.or.ug/) in Uganda. 


## Examples 
### Get list of  [licensed drugs](https://www.nda.or.ug/drug-register/)
    
```python
from ndacrawler import get_drugs
drugs = get_drugs()

herbal_human_drugs = drugs["Herbal Human"]

print(herbal_human_drugs.headers)
print(herbal_human_drugs.data)
```
 - [Registered and Licensed Pharmacies](https://www.nda.or.ug/licensed-outlets/)
 - [Registered and Licensed Drug Shops](https://www.nda.or.ug/drug-shops-licensed-in-2020/)
