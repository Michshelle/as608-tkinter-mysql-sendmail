import as608_combo_lib as as608

session = as608.connect_serial_session("/dev/ttyUSB0")
if session:
	as608.get_templates_list(session)
	as608.get_templates_count(session)
	as608.get_device_size(session)
	
	# 在指模机内存里录入指纹
	#as608.enroll_finger_to_device(session, as608)

	# 在内存里匹配指纹可以使用
	print(as608.search_fingerprint_on_device(session, as608))

	# 同时在文件系统和装置里存入指纹
	#as608.enroll_to_file_and_device(session, as608, "database", "templ000000001")

	#as608.enroll_save_to_file(session, as608, "database", "templ1")
	#as608.enroll_save_to_file(session, as608, "database", "templ000000001")
	#as608.fingerprint_check_one_file(session, as608, "database", "templ1")
	#as608.fingerprint_check_one_file(session, as608, "database", "templ000000001")
	#as608.fingerprint_check_all_file(session, as608, "database")

	# 清空指模机内存的数据库
	#as608.empty_ram_library(session,as608)
else:
	print("EXIT")
