import subprocess

def launch_camera_instance(num_instances):
    """
    Method to launch x camera players
    """    
    command = "python main.py"
    for v in range(num_instances):
        subprocess.Popen(command, shell=True, executable='/bin/bash', start_new_session=True)

if __name__ == "__main__":
    launch_camera_instance(3)