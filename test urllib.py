import urllib
from bs4 import BeautifulSoup
import re
import time
import requests
import HTMLParser
from requests_toolbelt.multipart.encoder import MultipartEncoder

# responce = urllib.urlopen(
#                 'http://nippm.natinst.com/itg/dashboard/app/portal/PageView.jsp')
# text = responce.read().decode('utf-8')
# print text

def CAR_login(username, password):
    1
    
m=MultipartEncoder({'REQUEST_ID':11111},encoding='multipart/form-data')
print m.to_string()
url = 'http://nippm.natinst.com/itg/web/knta/global/Logon.jsp'
payload = {
    'field-username': 'kawang',
    'field-password': '!Q2w3e4r',
    'nls_language': 'AMERICAN',
    'com.mercury.dashboard.arch.fieldtree.date.timeZone': '-480',
    'com.mercury.dashboard.arch.fieldtree.date.zeroTimeUser': str(int(time.time() * 1000)),
    'com.mercury.dashboard.screen_resolution_width': '1920',
    'PAGE_TYPE': 'LOGON_PAGE',
    'label-LOGON_SUBMIT_BUTTON_CAPTION': 'submit'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'nippm.natinst.com',
    'Origin': 'http://nippm.natinst.com',
    'Referer': 'http://nippm.natinst.com/itg/web/knta/global/Logon.jsp',
    'Cookie':'JSESSIONID=F6D033EB19E78E8206E3AB756E0C9367.kintana2; IS_WINDOID=N; JSESSIONID=F6D033EB19E78E8206E3AB756E0C9367.kintana2; KNTA_VERSION=9.3; httpCSSnippm.natinst.comSitgSLOGININFO=4.5|ENGLISH; NSC_ojqqn_IUUQ=ffffffff81ac102345525d5f4f58455e445a4a4229a0'
    
}
def refresh_cookie_in_header(new_cookie,old_cookie):
    for k,v in new_cookie.items():
        r=re.compile('%s=[^;]*;' % k)
        r.sub('%s=%s;'%(k,v),old_cookie)
    return old_cookie
s = requests.session()  # Tried 'session' and 'Session' following different advice
logon = s.get(url)

logonpage = logon.text
headers['Cookie']=refresh_cookie_in_header(logon.cookies.get_dict(),headers['Cookie'])
# print logonpage
soup = BeautifulSoup(logonpage, 'html.parser')
payload['WebSessionKey'] = soup.find('input', {'name': 'WebSessionKey'}).attrs['value']
print payload
print headers
print"----------------------------------------------------------------------------------------\n"

url = 'http://nippm.natinst.com/itg/dashboard/app/portal/PageView.jsp'
# headers['Cookie']=logon.cookies
home_page= s.post(url, data=payload, headers=headers)
print home_page.text[-1000:]
print"----------------------------------------------------------------------------------------\n"

# create_page = s.get('http://nippm.natinst.com/itg/web/knta/crt/RequestCreate.jsp',headers= headers,
#           params={'REQUEST_TYPE_CREATE': '5.31.30240.CAR - Corrective Action Request'})
# print create_page.text[-2000:]
headers['Content-Type'] =  'multipart/form-data; boundary=----WebKitFormBoundaryPV4HPeniEw15K5y1'
source_CAR_page = s.get('http://nippm.natinst.com/itg/web/knta/crt/RequestUpdate.jsp',headers= headers,)
          # params={'REQUEST_ID': '616715'})
print source_CAR_page.text

'''------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="VALIDATION_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="APPROVALS_REQUIRED_CODE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STEP_TYPE_CODE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STATUS"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STEP_NAME"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="RESULT_VALUE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="WORKFLOW_STEP_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="WORKFLOW_COMMAND_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="DESTINATION_PAGE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STEPS_MAX"

2
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TRANSITIONS_MAX_STEP_0"

9
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TRANSITIONS_MAX_STEP_1"

3
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_ID_CONTEXT"

616715
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_ID"

616715
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="ACTION"

SAVE
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CHANGE_TO_REQUEST_TYPE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="USER_ACTION"

SAVE
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="ID_CACHE_NAME"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="COPIED_FROM_ID"

616715
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="SAVE_DRAFT"

N
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TIMESTAMP"

1480121303520
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="WF_ACTION_TAKEN"

N
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="rule_form_input"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="DESCRIPTION"

testcar for automate autotest result reporting process 1
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="DESCRIPTIONHV"

54.54.testcar for automate autotest result reporting process.testcar for automate autotest result reporting process
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CH_1"

Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CH_1HV"

6.12.115022.Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CREATION_DATE"

2016年11月22日
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CREATION_DATEHV"

21.11.2016-11-22 10:26:42.0.2016年11月22日
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="ASSIGNED_TO_USER_ID"

Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="ASSIGNED_TO_USER_IDHV"

6.12.115022.Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STATUS_ID"

Open
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STATUS_IDHV"

2.4.72.Open
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_SUB_TYPE_ID"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="DEPARTMENT_CODE"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="WORKFLOW_ID"

5.31.30403.CAR - Corrective Action Request
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CH_3"

1.1.1.1
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CREATED_BY"

6.12.115022.Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_ID"

6.6.616715.616715
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_IDHV"

6.6.616715.616715
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_TYPE_ID"

5.31.30240.CAR - Corrective Action Request
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CONTACT_EMAIL"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CONTACT_PHONE_NUMBER"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CONTACT_NAME_ID"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="PERCENT_COMPLETE"

1.1.0.0
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="COMPANY"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CH_4"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQUEST_GROUP_CODE"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="ASSIGNED_TO_GROUP_ID"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="APPLICATION_CODE"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="PRIORITY_CODE"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REQ_TIMESTAMP"

1479832014000
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="WF_EVENT"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STEP_TRANSACTION_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_4"

Instrument Drivers/IVI
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_4HV"

3.22.118.Instrument Drivers/IVI
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_5"

N/A
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_5HV"

4.3.1513.N/A
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_23"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_23HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_7"

LabVIEW Plug and Play (project-style) Driver
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_7HV"

4.44.5952.LabVIEW Plug and Play (project-style) Driver
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_8"

Specified in Description
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_8HV"

3.24.383.Specified in Description
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_9"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_9HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_6"

2.15.13.1. Unnoticeable
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_10"

2.7.20.1. Task
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_2"

2.13.70.Configuration
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_3"

2.11.21.Dev: Manual
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_12"

All
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_12HV"

2.3.35.All
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_28"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_28HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_40"

Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_40HV"

6.12.115022.Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_38"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_38HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_16"

Unspecified
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_16HV"

4.11.7235.Unspecified
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_32"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_32HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_11"

3.11.288.Unspecified
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_21"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_21HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_30"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_30HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_31"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_31HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_19"

N
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_20"

13.13.NOT_EVALUATED.Not Evaluated
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_22"

13.13.NOT_EVALUATED.Not Evaluated
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_61"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_61HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_62"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_62HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_29"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_29HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_SHOW_RANGE_P_34"

5
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_34"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_EditableComponents_P_34_0HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_EditableComponents_P_34_1HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_EditableComponents_P_34_2HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_39"

6.6.616715.616715
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_36"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_49"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_91"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_54"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_53"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_55"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_56"

2.23.16.Related to this Request
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_51"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_33"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_48"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_17"

4.4.Open.Open
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_37"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_35"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_59"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_14"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_47"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_52"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_50"

6.12.115022.Kaijian Wang
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_18"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_1"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_41"

test
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_42"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_43"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_SHOW_RANGE_P_24"

5
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_24"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_EditableComponents_P_24_0HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TC_EditableComponents_P_24_1HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_44"

0.11..&lt;!--HTML--&gt;
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_93"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_93HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_94"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_92"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_58"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_58HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_57"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_57HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_46"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_25"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_25HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_26"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_26HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_27"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_27HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_60"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_60HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_13"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_13HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_15"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_15HV"

0.0..
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="HTMLNAME"

21.11.2016-11-22 10:26:49.0.2016年11月22日
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="NEW_NOTE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="NOTE_AUTHOR"

2.3.-1.ALL
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="CHANGE_FIELD"

2.3.-1.ALL
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="NEW_REFERENCE_ENTITY_TYPE"

10.10.ATTACHMENT.Attachment
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="DELETE_REFERENCE_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TARGET_TYPE_CODE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="TARGET_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REFERENCE_NAME"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REF_RELATIONSHIP_ID"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REF_BEHAVIOR_CODE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REFERENCE_DESCRIPTION"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="STORED_FILENAME"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REF_LINK"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="REFERENCE_TYPE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="RELATIONSHIP_NAME"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="UPDATED_BEHAVIOR_CODE"


------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_34_TBL_PARAMETER_SET_FIELD_ID"

40781
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_34_TBL_VALIDATION_ID"

31150
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_34_TBL_HAS_UPDATE"

N
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_24_TBL_PARAMETER_SET_FIELD_ID"

40777
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_24_TBL_VALIDATION_ID"

31143
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="P_24_TBL_HAS_UPDATE"

N
------WebKitFormBoundaryPV4HPeniEw15K5y1
Content-Disposition: form-data; name="IS_WINDOID"

N
------WebKitFormBoundaryPV4HPeniEw15K5y1--'''
# car_desc=
# {
#     'REQ.DESCRIPTION':'testcar',
#     'REQ.ASSIGNED_TO_USER_IDAC_TF':'Kaijian Wang'
# }
# print r.text

# soup = BeautifulSoup(text,"html.parser")
# tag=soup.span
# print(tag.string)
# print soup

#
#
# class LinksParser(HTMLParser.HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.recording = 0
#         self.data = []
#
#     def handle_starttag(self, tag, attributes):
#         if tag != 'span':
#             return
#         if self.recording:
#             self.recording += 1
#             return
#         for name, value in attributes:
#             if name == 'id' and value == 'lblxh':
#                 break
#         else:
#             return
#         self.recording = 1
#
#     def handle_endtag(self, tag):
#         if tag == 'span' and self.recording:
#             self.recording -= 1
#
#     def handle_data(self, data):
#         if self.recording:
#             self.data.append(data)
#
# p=LinksParser
# p.feed(text)
# p.close()
# print p.data
