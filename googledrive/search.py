from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tabulate import tabulate

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_413772283174-ekldmn2ui6cblv3t4q4312tq1fp859vv.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)


        # Call the Drive v3 API
        # results = service.files().list(
        #     pageSize=1000, fields="nextPageToken, files(id, name)").execute()
        # items = results.get('files', [])

         # 폴더 찾기
        folder_name = 'machine_system_design'
        # folder_name = input("\n찾으실 디렉토리명을 입력해 주세요: ")

        folder_result = service.files().list(q="mimeType='application/vnd.google-apps.folder' and name='" + folder_name + "'",
                                            spaces='drive', pageSize=1000,
                                            fields='nextPageToken, files(id, name)').execute()
        folder = folder_result.get('files', [])
        if not folder:
            print('해당 디렉토리가 존재하지 않습니다.')
            return

        folder_id = folder[0]['id']
        print("\n" + folder_name + "의 ID는 " + folder_id + "입니다.\n")
        
        print("─────── " + folder_name + " 디렉토리 내 파일 목록 ───────\n")
        
        # 특정 폴더 내 파일 찾기
        results = service.files().list(q="parents='" + folder_id + "'",
                                        spaces='drive', pageSize=1000,
                                        fields='nextPageToken, files(id, name)').execute()      
        
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return

        rows = []
        for item in items:
            link = "https://drive.google.com/uc?export=view&id=" + item['id']
            rows.append((item['name'], item['id'], link))

        table = tabulate(rows, headers=["파일명", "아이디", "이미지 링크"])

        print(table)
            
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

    print("\n")

    return rows

if __name__ == '__main__':
    main()