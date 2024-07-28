import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdn.v20180606 import cdn_client, models
import os
try:
    secret_id = os.environ.get('SECRET_ID')
    secret_key = os.environ.get('SECRET_KEY')
    print(secret_key, secret_id)
    cred = credential.Credential(secret_id, secret_key)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "cdn.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cdn_client.CdnClient(cred, "", clientProfile)

    req = models.PurgePathCacheRequest()
    params = {
        "Paths": [ "https://www.aye.ink" ],
        "FlushType": "delete"
    }
    req.from_json_string(json.dumps(params))

    resp = client.PurgePathCache(req)

    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)