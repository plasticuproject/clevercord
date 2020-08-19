# added by plasticuproject@protonmail.com

import requests
from json.decoder import JSONDecodeError


class CVE:

    # The main app funtion
    @staticmethod
    def search(message):

        # API base address
        url = 'https://plasticuproject.pythonanywhere.com/nvd-api/v1/'

        # help banner
        show_help = '''
```
Search CVE records by ID, YEAR and/or KEYWORD. Prints ID and description only.
\nUSAGE:
$cve <CVE-ID>
$cve <year> (keyword)
$cve all (keyword)
$cve recent (keyword)
$cve modified (keyword)
```
'''

        # split message into arguments and initialize dictionary
        args = message.split(' ')
        cves = {}

        # Prints help/usage info
        if len(args) == 1 or args[1] == '-h' or args[1] == '--help' or args[1] == 'help' or args[1] == 'HELP':
            return (show_help)

        # Adds CVE ID and description to cves dictionary from results matching CVE-ID queried
        elif len(args) == 2 and args[1].startswith('cve') or args[1].startswith('CVE'):
            cve = args[1]
            res = requests.get(url + cve)
            cves[res.json()['cve']['CVE_data_meta']['ID']] = res.json()['cve']['description']['description_data'][0]['value']

        # Adds CVE ID/s and descriptions/s to cves dictionary from results list if CVEs are found matching criteria
        else:
            date = args[1]
            year = 'year/'
            keyword = ' '.join(args[2:])
            if date == 'all' or date == 'recent' or date == 'modified':
                year = date
                date = ''
            res = requests.get(url + year + date + '?keyword=' + keyword)
            for i in res.json():
                cves[i['cve']['CVE_data_meta']['ID']] = i['cve']['description']['description_data'][0]['value']

        # Prints if no results are found and cves dictionary is empty
        if len(cves) == 0:
            return ('No results found.')

        # Prints singe CVE ID and description from cves dictionary
        if len(cves) == 1:
            for ID, description in cves.items():
                result = ('\n**' + str(ID) + '**\n' + str(description) + '\n')
                return (result)
            
        # Prints IDs and number of results if many
        ids = []
        if len(cves) > 1:
            for ID, description in cves.items():
                ids.append(ID)
            num = len(ids)
            found = '\n**{} result found.**'.format(str(num))
            if num < 120:
                result = '\n'.join(ids) + found
                return (result)
            elif num > 120:
                result = '\n'.join(ids[:120]) + found + '\n*Some results omitted due to size limits.*'
                return (result)


    @staticmethod
    def cveSearch(message):

        # Run search function and catch all errors and exceptions
        try:
            return CVE.search(message)

        except (KeyError, TypeError):
            args = message.split(' ')
            user_in = ' '.join(args[1:])
            return ('**Did not understand your request for:** ' + user_in)

        except JSONDecodeError:
            return ('**NETWORK ERROR:** Please check your request or try again later.')

