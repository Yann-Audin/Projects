from projectLibraries import importer
from Anthalgo import anthalgo

def main():
    # List of libraries to be imported
    
    lib = ["requests", "time", "json"]
    sub_lib = []
    lib_as = []
    
    importer.import_all_libraries(lib, sub_lib, lib_as)
    
    # Import the data from the endpoint
    
    url = "https://anthologiagraeca.org/api/passages/?format=json&page="
    anthalgo.fetch_data(url)