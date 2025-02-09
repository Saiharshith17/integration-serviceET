from setuptools import setup, find_packages

install_requires = [
   'confluent_kafka'=='2.8.0',
'Flask'=='3.1.0',
'langchain_core'=='0.3.34',
'langchain_mistralai'=='0.2.6',
'langchain_openai'=='0.3.4',
'pydantic'=='2.10.6',
'python-dotenv'=='1.0.1'

]

setup(
    name="ds_service",
    version="1.0",
    packages=find_packages(where="src"),  # Ensure it finds packages inside "src"
    package_dir={"": "src"},  # Maps package root to "src"
    include_package_data=True,  # Ensure extra data files are included
    install_requires=["flask",
                    "python-dotenv",
                    "confluent-kafka"],
)