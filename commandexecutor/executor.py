import subprocess

class Executor:
    def execute(self,command):
        try:
            process = subprocess.run([command.name] + command.args)
            return process.returncode
        except FileNotFoundError:
            print(f"{command.name}: Command not found")
        except Exception as ex:
            print(f"Error during command execution : {str(ex)}")