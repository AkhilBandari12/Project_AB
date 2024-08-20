from datetime import datetime


class OracleDBLogin:
    
    def __init__(self):
        data=read_config_data() # type: ignore
        now = datetime.now()
        self.report_generation_folder_name=data['ReportGeneratorFolderPath']
        self.port_number=data['OraclePortNumber']
        self.hostname=data['OracleHostname']
        self.service_name=data['OracleServiceName']
        self.tnsnames_service_name=data['tnsNamesServiceName']
        #self.config_file_path=data['pythonConfigFilePath']
        self.log_folder_name=data['LogFolderName']
        self.log_file_name=data['LogFileName']
        self.username=data['OracleDBUsername']
        self.password=data['OracleDBPassword']
        self.encoding=data['EncodingValue']        
       

    def oracle_DB_login(self):     
        conn = cx_Oracle.connect(self.username,self.password,self.tnsnames_service_name,encoding=self.encoding) # type: ignore
        cursor = conn.cursor()
        return cursor,conn