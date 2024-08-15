import paramiko
import subprocess

def submit_job(row_index, general, batch, ssh):

    # Define the PowerShell command
    ps_command = f"scp -r {general.directory_path_local}{batch.column_data['case_name'][row_index]} {ssh.username}@{ssh.hostname}:{general.directory_path_cluster}"

    if row_index == 0:
        ps_command += f"\nscp {general.batch_file_path} {ssh.username}@{ssh.hostname}:{general.directory_path_cluster}"
    if general.copy == True and row_index == 0:
        ps_command += f"\nscp {general.directory_path_local}{general.template}.sim {ssh.username}@{ssh.hostname}:{general.directory_path_cluster}"
    
    ps_command = ps_command + "\nscp "+general.directory_path_local+"run.java "+ssh.username+"@"+ssh.hostname+":"+general.directory_path_cluster+batch.column_data['case_name'][row_index]

    #Execute the PowerShell command
    subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
    if row_index == 0:
        print(f"Copying batch_file to {general.directory_path_cluster}")
    if general.copy == True and row_index == 0:
        print(f"\nCopying {general.template}.sim file to cluster at {general.directory_path_cluster}")
    print(f"Copying {batch.column_data['case_name'][row_index]} folder to cluster at {general.directory_path_cluster}")
   
    import paramiko

    if general.run == True:
        ssh_command = [
            f'ln -sf {general.directory_path_cluster}{general.template}.sim {general.directory_path_cluster}{batch.column_data["case_name"][row_index]}',
            f'cd {general.directory_path_cluster}{batch.column_data["case_name"][row_index]}',
            f'dos2unix submit_{batch.column_data["case_name"][row_index]}.sbatch',
            f'sbatch submit_{batch.column_data["case_name"][row_index]}.sbatch'
        ]

        try:
            # Create an SSH client
            client = paramiko.SSHClient()

            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Connect to the remote host
            client.connect(hostname=ssh.hostname, port=ssh.port, username=ssh.username, password=ssh.password)
            
            # Combine ssh_command into a single string separated by semicolons
            command_string = ' && '.join(ssh_command)

            # Execute the combined command string
            stdin, stdout, stderr = client.exec_command(command_string)

            # Read and print output and errors
            output = stdout.read().decode()
            errors = stderr.read().decode()
            
            print("Cluster command line outputs:")
            if output:
                output = output.replace('\n', '   ')
                print(f"{output}")
            if errors:
                errors = errors.replace('\n', '   ')
                print(f"{errors}")
                
            print(f'{batch.column_data['case_name'][row_index]} has been submitted to the cluster (unless errors in "Cluster command line outputs")')

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the connection
            client.close()

   