from class_define import general_details
from class_define import batch_file_details
from class_define import ssh_connection_details
from class_define import job_submission_details

from start_macro_writer import start_macro_writer
from append_macro_writer import append_macro_writer
from submit_job_script import submit_job_script
from submit_job import submit_job

#Notes:
# - function: add specified scalars in batch spreadsheet into template then run the case on the cluster
# - input: one batch spreadsheet with as many scalars, but 1st column must be "case_name", one StarCCM+ template
# - python packages: pandas, paramiko

#Recommendations:
# - only scalars so if used in a unit needed application, default units are SI units (units specifier coming soon)
# - recommended to setup passwordless SSH for user experience

# SCRIPT FUNCTIONS
copy = False #True if you want to copy .sim file to cluster (.java files will always copy)
run = True #True if you want to submit jobs to the cluster

# MUST SPECIFY --> general details
batch_spreadsheet = "parameter.csv"
directory_path_local = "C:\\Users\\younj\\Downloads\\upRiver\\"
batch_file_path = "C:\\Users\\younj\\Downloads\\upRiver\\parameter.csv"
directory_path_cluster = "/storage/coda1/p-sm53/0/jyoun39/project/"
template = "onera-m6-sharp_airfoil" #don't add .sim afterwards

# # MUST SPECIFY --> ssh connection details
hostname = "login-phoenix.pace.gatech.edu"
port = 22
username = "jyoun39"
password = "96385207410yJ____"

# # MUST SPECIFY --> Job submission details
account = "gts-cperron7"
nodes = "1"
taskspernode = "12"
mempercpu = "7500M"
time = "0:05:00"
qos = "embers"
email = "jyoun39@gatech.edu"

#specify parameters to add (make sure they are the same as headers in .csv)
parameters_to_add = ["new1", "new2", "new3"]

#create objects
general = general_details(batch_file_path, directory_path_local, directory_path_cluster, run, copy, template) #could make this global, but it is easier this way imo
batch = batch_file_details(batch_file_path)
batch.read_batch_file()
ssh = ssh_connection_details(hostname, port, username, password) #could make this global, but it is easier this way imo
job = job_submission_details(account, nodes, taskspernode, mempercpu, time, qos, email) #could make this global, but it is easier this way imo

#main for loop to create .java, add parameters to .java, copy over .java and .sim files, then submit job on cluster
for row_index in range(batch.num_rows):
    start_macro_writer(row_index, parameters_to_add, batch, general) #this is good
    append_macro_writer(row_index, parameters_to_add, batch, general)
    print("\n")
    submit_job_script(row_index, general, batch, job) #creates job submission script
    submit_job(row_index, general, batch, ssh) #creates case directories, copies files, and submits job








