import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from , "rb")
        dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'JYD-BBbP3ZEAAAAAAAAAAf-0LaqdxcUyHF9jKpSulwqO8AN-b-fmw4HnMADA1Drj'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :-")
    file_to = input("enter the path to upload to the dropbox:-")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()