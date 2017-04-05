
from tld import get_tld

# Function to get top level domain
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name
