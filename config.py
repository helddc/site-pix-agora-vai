import os

# Lê as chaves do ambiente seguro do Render
ANUBIS_PUBLIC_KEY = os.getenv("ANUBIS_PUBLIC_KEY")
ANUBIS_PRIVATE_KEY = os.getenv("ANUBIS_PRIVATE_KEY")

# Regras de negócio
FIXED_FEE = 2.50
PERCENTAGE_COMMISSION = 0.15
MINIMUM_VALUE = 20.00

# API URL
ANUBIS_API_URL = "https://api.anubis.gg/api"
