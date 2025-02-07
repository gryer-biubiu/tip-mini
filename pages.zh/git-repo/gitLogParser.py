#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import re
import xlsxwriter
import argparse

# array to store dict of commit data
commits = []

def parseCommit(commitLines):
    # dict to store commit data
    commit = {}
    # iterate lines and save
    for nextLine in commitLines:
        # print(nextLine)
        if nextLine == '' or nextLine == '\n':
            # ignore empty lines
            pass
        elif bool(re.match('commit', nextLine, re.IGNORECASE)):
            # commit xxxx
            if len(commit) != 0:        ## new commit, so re-initialize
                if 'product' not in commit:
                    commit['product'] = 'N/A'
                elif len(commit['product']) > 17:
                    commit['product'] = commit['product'][:14].ljust(17, '.')
                if 'ticket' not in commit:
                    commit['ticket'] = 'N/A'
                elif len(commit['ticket']) > 23:
                    commit['ticket'] = commit['ticket'][:20].ljust(23, '.')
                if 'changeid' not in commit:
                    commit['changeid'] = 'N/A'
                if commit['product'].strip() and commit['ticket'].strip():
                    commits.append(commit)
                # print(commit)
                commit = {}
            commit = {'hash' : re.match('commit (.*)', nextLine, re.IGNORECASE).group(1) }
        elif bool(re.match('merge:', nextLine, re.IGNORECASE)):
            # Merge: xxxx xxxx
            pass
        elif bool(re.match('author:', nextLine, re.IGNORECASE)):
            # Author: xxxx <xxxx@xxxx.com>
            m = re.compile('Author: (.*) <(.*)>').match(nextLine)
            commit['author'] = m.group(1)
            commit['email'] = m.group(2)
        elif bool(re.match('date:', nextLine, re.IGNORECASE)):
            # Date: xxx
            pass
        elif bool(re.match('    ', nextLine, re.IGNORECASE)):
            # (4 empty spaces)
            if commit.get('message') is None:
                commit['message'] = nextLine.strip()

            #JIRA TICKET:
            m = re.compile('    JIRA TICKET:[\s]{0,}(.*)').match(nextLine)
            if m is not None:
                commit['ticket'] = m.group(1)
                continue
            m = re.compile('(.*)JIRA TICKET:[\s]{0,}(.*)"').match(nextLine)
            if m is not None:
                commit['ticket'] = m.group(2)
                continue

            #Reference:
            m = re.compile('    Reference:[\s]{0,}(.*)').match(nextLine)
            if m is not None:
                if 'ticket' in commit:
                    if commit['ticket'].count('/') == 0:
                        commit['ticket'] += '/'+m.group(1)
                    elif commit['ticket'].count('/') == 1:
                        commit['ticket'] += '/...'
                else:
                    commit['ticket'] = m.group(1)
                continue
            m = re.compile('(.*)Reference:[\s]{0,}(.*)').match(nextLine)
            if m is not None:
                if 'ticket' in commit:
                    if commit['ticket'].count('/') == 0:
                        commit['ticket'] += '/'+m.group(2)
                    elif commit['ticket'].count('/') == 1:
                        commit['ticket'] += '/...'
                else:
                    commit['ticket'] = m.group(2)
                continue

            #Change-Id:
            m = re.compile('    Change-Id:[\s]{0,}(.*)').match(nextLine)
            if m is not None:
                commit['changeid'] = m.group(1)
                continue

            m = re.compile('    Product:[\s]{0,}(.*)').match(nextLine)
            if m is not None:
                if 'product' in commit:
                    if commit['product'].count('/') == 0:
                        commit['product'] += '/'+m.group(1)
                    elif commit['product'].count('/') == 1:
                        commit['product'] += '/...'
                else:
                    commit['product'] = m.group(1)
                continue
            m = re.compile('(.*)Product:[\s]{0,}(.*)').match(nextLine)
            if m is not None:
                if 'product' in commit:
                    if commit['product'].count('/') == 0:
                        commit['product'] += '/'+m.group(2)
                    elif commit['product'].count('/') == 1:
                        commit['product'] += '/...'
                else:
                    commit['product'] = m.group(2)
                continue
        else:
            print ('ERROR: Unexpected Line: ' + nextLine)

    if len(commit) != 0:
        if 'product' not in commit:
            commit['product'] = 'N/A'
        elif len(commit['product']) > 17:
                    commit['product'] = commit['product'][:14].ljust(17, '.')
        if 'ticket' not in commit:
            commit['ticket'] = 'N/A'
        elif len(commit['ticket']) > 23:
                    commit['ticket'] = commit['ticket'][:20].ljust(23, '.')
        if 'changeid' not in commit:
            commit['changeid'] = 'N/A'
        if commit['product'].strip() and commit['ticket'].strip():
            commits.append(commit)

def write_xlsx(commits, filename, sheet_name):
    if filename is None:
        return

    workbook = xlsxwriter.Workbook(filename)
    if sheet_name is None:
        worksheet = workbook.add_worksheet()
    else:
        worksheet = workbook.add_worksheet(sheet_name)
    header = [u'问题编号', u'提交者', u'Hash', u'说明']
    worksheet.write_row(0, 0, header)
    row = 1
    for commit in commits:
        worksheet.write(row, 0, commit['ticket'])
        worksheet.write(row, 1, commit['author'])
        worksheet.write(row, 2, commit['hash'])
        worksheet.write(row, 3, commit['message'])
        row += 1
    workbook.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='git log parser')

    parser.add_argument('-xlsx_name', default=None, help='xlsx file name to write to')
    parser.add_argument('-sheet_name', default=None, help='xlsx sheet name')
    parser.add_argument('-project_name', default=None, help='project name')
    args = parser.parse_args()

    parseCommit(sys.stdin.readlines())
    if len(commits) is 0:
        exit(0)

    # print commits
    print("\nProject %s" %(args.project_name))
    # for commit in commits:
    #     print(commit)
    print ('Ticket'.ljust(23) + '  ' + 'Product'.ljust(17) + '  ' + 'Author'.ljust(18) + '  ' + 'Hash'.ljust(8) + '  ' + 'Change-Id'.ljust(10) + '  ' + 'Message'.ljust(32))
    print ("=================================================================================")
    for commit in commits:
        print (commit['ticket'][:23].ljust(23) + '  ' + commit['product'][:17].ljust(17) + '  ' + commit['author'].ljust(18) + '  ' +  commit['hash'][:8].ljust(8) + '  ' + commit['changeid'][:10].ljust(10) + '  ' + commit['message'][:40])

    write_xlsx(commits, args.xlsx_name, args.sheet_name)
