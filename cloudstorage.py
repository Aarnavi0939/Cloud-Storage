import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGdXwNnxnH2T6DWpHkY_quWxoLHw9WdsgBGQzdpMQINaRvYjIOAnkzrXz_oDrM-y_nMuC6T-11g7pi8IMabwj5hCGEZjfoUOf-alr8CsbEJ3_lfoMesf8KUAdYHEBEH5HLSrliAXk3Q'
    ta = TransferData(access_token)
    file_from = input("Enter the file path to transfer")
    file_to = input('Enter the full path to upload to dropbox')
    ta.upload_file(file_from, file_to)
    print("File has been moved succesfully")

main()