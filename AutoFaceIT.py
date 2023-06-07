import time
import psutil
import subprocess
import os
import logging

# Configure logging
logging.basicConfig(filename='script.log', level=logging.INFO)

def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

def close_process(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.terminate()

def find_executable(executable_name):
    for path in os.environ["PATH"].split(os.pathsep):
        executable_path = os.path.join(path, executable_name)
        if os.path.isfile(executable_path):
            return executable_path
    return None

def launch_faceit_anticheat():
    faceit_anticheat_path = find_executable('faceit_anticheat.exe')
    if faceit_anticheat_path:
        try:
            subprocess.run(faceit_anticheat_path, shell=True)
            logging.info("FaceIT Anti-Cheat launched.")
        except Exception as e:
            logging.error("An error occurred while launching FaceIT Anti-Cheat: " + str(e))
    else:
        logging.error("FaceIT Anti-Cheat executable not found.")

def launch_csgo():
    csgo_path = find_executable('csgo.exe')
    if csgo_path:
        try:
            subprocess.run(csgo_path, shell=True)
            logging.info("CSGO launched.")
        except Exception as e:
            logging.error("An error occurred while launching CSGO: " + str(e))
    else:
        logging.error("CSGO executable not found.")

def monitor_csgo():
    csgo_running = False
    faceit_anticheat_running = False

    while True:
        csgo_process = None
        faceit_anticheat_process = None

        # Check CSGO process
        for process in psutil.process_iter(['name']):
            if process.info['name'] == 'csgo.exe':
                csgo_process = process
                break

        # Check FaceIT Anti-Cheat process
        for process in psutil.process_iter(['name']):
            if process.info['name'] == 'faceit_anticheat.exe':
                faceit_anticheat_process = process
                break

        if csgo_process:
            if csgo_running:
                logging.debug("CSGO already running. Skipping closure and anti-cheat launch.")
            else:
                logging.info("CSGO launched. Closing CSGO...")
                close_process('csgo.exe')
                time.sleep(5)  # Give time for CSGO to fully close
                csgo_running = True

        if faceit_anticheat_process:
            if faceit_anticheat_running:
                logging.debug("FaceIT Anti-Cheat already running.")
            else:
                logging.info("FaceIT Anti-Cheat launched.")
                faceit_anticheat_running = True

        if not csgo_running and not faceit_anticheat_running:
            logging.info("Launching CSGO...")
            launch_csgo()

        time.sleep(5)  # Check for CSGO and FaceIT Anti-Cheat every 5 seconds

def main():
    try:
        while True:
            steam_process = None

            # Check Steam process
            for process in psutil.process_iter(['name', 'exe']):
                if process.info['name'] == 'steam.exe' and 'steam' in process.info['exe'].lower():
                    steam_process = process
                    break

            if steam_process:
                cmdline = steam_process.cmdline()
                if 'csgo.exe' in cmdline:
                    logging.info("CSGO launched from Steam. Monitoring CSGO...")
                    monitor_csgo()

            time.sleep(5)  # Check for Steam and CSGO every 5 seconds
    except Exception as e:
        logging.error("An error occurred: " + str(e))

if __name__ == '__main__':
    main()
