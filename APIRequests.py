import urllib2 #import the package to allow us to make HTTP requests
import json #import the package to allow us to decode json
import xml.etree.ElementTree as ET #import the package to allow us to parse xml

def getSiteData(apikey,siteList=''):
    if len(siteList) == 0:
        request = urllib2.urlopen('https://sentinel.whitehatsec.com/api/site/?key=' + apikey + '&display_entry_points_content=0&display_scan_status=1&display_scans=1&display_organization=0&display_host_links=0&display_entry_points=0&display_site_credentials=0&display_allowed_hosts=1&display_scan_schedule=0&display_service_type=1&display_description=1&display_groups=0&display_vuln_stats=1&display_min=0&order_by=id&accept_fmt=json')
    else:
        request = urllib2.urlopen('https://sentinel.whitehatsec.com/api/site/' + siteList + '?key=' + apikey + '&display_service_type=1&accept_fmt=json')
    data = json.loads(request.read())
    return data

def getVulnData(apikey,vulnStatus,site,severityAPI=['1','2','3','4','5']):
    if vulnStatus == 'open' or vulnStatus == 'closed,certified' or vulnStatus == 'open,closed,certified':
        url = 'https://sentinel.whitehatsec.com/api/vuln/?key=' + apikey + '&query_status=' + vulnStatus + '&query_site=' + str(site) + '&query_severity=' + ','.join(severityAPI)
        request = urllib2.urlopen(url)
    data = ET.fromstring(request.read())
    return list(data)

#Insert API key
#TODO use secrete mgmt
api = ''
#Enter site ID
site = ''

#print getVulnData(api,'open',site)[0].attrib['class']
print getSiteData(api)

