import sys
import logging
from src.exception import CustomException
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter




# initiatlizing logger
logger = logging.getLogger(__name__)


class MainUtils:

    def load_docs(self, data_directory: str) -> list:
        logger.info("Enetred the load_docs method of MainUtils class")
        try:
            loader = DirectoryLoader(data_directory)
            documents = loader.load()

            logger.info("Exited the load_docs method of MainUtils class")
            return documents
        
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def split_docs(self, data: list, chunk_size: int, chunk_overlap: int) -> list:
        logger.info("Enetred the split_docs method of MainUtils class")
        try:    
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            docs = text_splitter.split_documents(data)

            logger.info("Exited the split_docs method of MainUtils class")
            return docs
        
        except Exception as e:
            raise CustomException(e, sys) from e