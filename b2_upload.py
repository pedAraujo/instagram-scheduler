import os
from dotenv import load_dotenv
from b2sdk.v2 import InMemoryAccountInfo, B2Api

load_dotenv()

info = InMemoryAccountInfo()
b2_api = B2Api(info)

application_key_id = os.environ.get('B2_APP_KEY_ID')
application_key = os.environ.get('B2_APP_KEY')
b2_api.authorize_account("production", application_key_id, application_key)

bucket = b2_api.get_bucket_by_name('instagram-scheduler-app')

local_file_path = '/Users/pedro/Documents/Code-Learning/instagram-scheduler/photo-test.jpg'
b2_file_name = 'dummy_photo-test.jpg'
file_info = {'how': 'good-file'}

bucket.upload_local_file(
    local_file=local_file_path,
    file_name=b2_file_name,
    file_infos=file_info,
)
