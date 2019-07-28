import hou

def execute(enable_output):
	# get all inputs
	input_lst = hou.pwd().inputAncestors()

	# check if there is a rop_geo node
	rop_abc_type = hou.nodeType(hou.sopNodeTypeCategory(), "rop_alembic")
	rop_abc_nodes = rop_abc_type.instances()
	rop_vdb_type = hou.nodeType(hou.sopNodeTypeCategory(), "rop_geometry")
	rop_vdb_nodes = rop_vdb_type.instances()

	# set parms and output
	for i in input_lst:
		node_name = i.name()
		range_x = node_name.split("_")[0]
		range_y = node_name.split("_")[1]
		for rop_abc in rop_abc_nodes:
			file_path = "$HIP/assets_" + node_name + "/abc_output/$OS.abc"
			rop_abc.setParms({"trange":1, "f1":range_x, "f2":range_y, "f3":1, "filename": file_path})
			print file_path
			if enable_output:
				rop_abc.parm('execute').pressButton()
				print "Processing" + file_path + "..."
		for rop_vdb in rop_vdb_nodes:
			file_path = "$HIP/assets_" + node_name + "/smk_output/$OS/$OS.$F4.vdb"
			rop_vdb.setParms({"trange":1, "f1":range_x, "f2":range_y, "f3":1, "sopoutput": file_path})
			print file_path
			if enable_output:
				rop_vdb.parm('execute').pressButton()
				print "Processing" + file_path + "..."




