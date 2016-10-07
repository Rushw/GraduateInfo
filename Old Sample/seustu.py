# -*- coding: utf-8 -*-
import urllib
import re
import codecs
import sys

def find(pattern, text):
	"""RE find in text."""
	pat = re.compile(pattern, re.U)
	match = pat.search(text)
	if match:
		return match.group(1)
	else:
		return False


def get_all(filename, start, end):
	"""Print and Write all students info into file from start to end."""
	outfile = codecs.open(filename, 'w', 'utf-8')
	outfile.write(u'姓名\t学号\t一卡通号\t院系\t专业\n')

	for cardnum in range(start, end):
		params = urllib.urlencode({'queryStudentId': cardnum, 'queryAcademicYear':'12-13-1'})
		ufile = urllib.urlopen("http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action", params)
		text = ufile.read().decode('utf-8')

		if find(ur'(没有找到该学生信息)', text):
			continue	

		college = find(ur'院系:\[\w+\](\w+)', text) 
		major = find(ur'专业:\[\w+\](\w+)', text) 
		student_id = find(ur'学号:(\w+)', text) 
		card = find(ur'一卡通号:(\d+)', text) 
		name = find(ur'姓名:(\w+)', text) 
	
		print name, student_id, card, college, major
		outfile.write('%s\t%s\t%s\t%s\t%s\n' % (name, student_id, card, college, major))

	outfile.close()


def main():
	args = sys.argv[1:]
	if len(args) != 3:
		print 'usage: filename start end'
		sys.exit(1)
	
	get_all(args[0], int(args[1]), int(args[2]))


if __name__ == '__main__':
	main()

