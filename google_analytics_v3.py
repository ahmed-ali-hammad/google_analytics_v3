# from future import print_function

import argparse
import sys
import csv

import time
from retrying import retry

import pandas as pd

from googleapiclient.errors import HttpError
from googleapiclient import sample_tools
from oauth2client.client import AccessTokenRefreshError

print(sys.argv)

def main(argv):
    service, flags = sample_tools.init(argv, 'analytics', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/analytics.manage.users.readonly')

    try:
        webpropertyuser(service)
    except TypeError as error:
        print(('There was an error in constructing your query : %s' % error))
    except HttpError as error:
        print(('Arg, there was an API error : %s : %s' %(error.resp.status, error._get_reason())))
    except AccessTokenRefreshError as error:
        print ('The credentials have been revoked or expired, please re-run the application to re-authorize')


def webpropertyuser(service):
    print(service.management().webpropertyUserLinks())
    accounts = service.management().webpropertyUserLinks().list(accountId="add_id" ,webPropertyId='~all',max_results=2000, start_index=2).execute()
    print(accounts)

    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]

    for propertyUserLink in accounts.get('items', []):
        entity = propertyUserLink.get('entity', {})
        propertyRef = entity.get('webPropertyRef', {})
        userRef = propertyUserLink.get('userRef', {})
        permissions = propertyUserLink.get('permissions', {})

        a=propertyUserLink.get('id')
        b=userRef.get('email')
        c=permissions.get('effective')
        d=propertyRef.get('id')
        e=propertyRef.get('kind')
        f=propertyRef.get('name')
        g=permissions.get('local')

        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
        E.append(e)
        F.append(f)
        G.append(g)

        data = {'Property_User_Link_Id':A,
            'User_Email':B,
            'Permissions_effective':C,
            'Property Id ':D,
            'Property Kind':E,
            'Property Name':F,
            'Permission Local':G}

main(sys.argv)