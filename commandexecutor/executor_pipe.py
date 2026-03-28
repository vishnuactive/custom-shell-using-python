import subprocess

class PipeExecution:
    def execute_pipe_commands(self,commands):
        processes = []
        previous_process = None

        for index,command in enumerate(commands):
            stdin = previous_process.stdin if previous_process is not None else None
            stdout = subprocess.PIPE if index < len(commands) - 1 else None

            process = subprocess.Popen([command.name] + command.args,
                                        stdin=stdin,
                                        stdout=stdout)
            if previous_process:
                previous_process.stdout.close()
            processes.append(process)
            previous_process = process
        
        for process in processes:
            process.wait()