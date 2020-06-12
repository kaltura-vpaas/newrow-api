from KalturaClient import *
from KalturaClient.Plugins.Core import *

# **** IMPORTANT! POPULATE THESE 4 VALUES PRIOR TO RUNNING ANY OF THE SCRIPTS!
partnerId          = "INSERT_VALID_PARTNER_ID"
userSecret         = "INSERT_VALID_USER_SECRET"
defaultResourceId  = "INSERT_VALID_RESOURCE_ID"
kafDomain          = "https://INSERT_VALID_KAF_DOMAIN.kaf.kaltura.com"

# Initialize the KalturaClient
config = KalturaConfiguration()
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)

# Get the request url for the particular API call
def getRequestURL(apiCall, resourceId):
    privileges = "resourceId:" + resourceId + ",role:viewerRole,api:" + apiCall
    ks = client.session.start(
        userSecret,
        "",
        KalturaSessionType.USER,
        partnerId,
        86400,
        privileges)
    requestUrl = kafDomain + "/newrowkaf/index/api?ks=" + ks

    return requestUrl
