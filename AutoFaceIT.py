  import time
import psutil
import subprocess
import os
import logging

def create_logs_folder():
    script_path = os.path.dirname(os.path.abspath(__file__))
    logs_folder = os.path.join(script_path, "Logs")
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)
    return logs_folder

def create_logger(logs_folder):
    current_time = time.strftime("%H%M%S")
    current_date = time.strftime("%Y%m%d")
    log_filename = f"{current_time}_{current_date}_errorlog.log"
    log_filepath = os.path.join(logs_folder, log_filename)

    logger = logging.getLogger("AutoFaceIT")
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(log_filepath)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def check_process_running(process_name):
    for process in psutil.process_iter(["name"]):
        if process.info["name"] == process_name:
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
    faceit_anticheat_path = find_executable("faceit_anticheat.exe")
    if faceit_anticheat_path:
        try:
            subprocess.run(faceit_anticheat_path, shell=True)
            logger.info("FaceIT Anti-Cheat launched.")
        except Exception as e:
            logger.error("An error occurred while launching FaceIT Anti-Cheat: " + str(e))
    else:
        logger.error("FaceIT Anti-Cheat executable not found.")

def launch_csgo():
    csgo_path = find_executable("csgo.exe")
    if csgo_path:
        try:
            subprocess.run(csgo_path, shell=True)
            logger.info("CSGO launched.")
        except Exception as e:
            logger.error("An error occurred while launching CSGO: " + str(e))
    else:
        logger.error("CSGO executable not found.")

def monitor_csgo():
    csgo_running = False
    faceit_anticheat_running = False

    while True:
        csgo_process = None
        faceit_anticheat_process = None

        # Check CSGO process
        for process in psutil.process_iter(["name"]):
            if process.info["name"] == "csgo.exe":
                csgo_process = process
                break

        # Check FaceIT Anti-Cheat process
        for process in psutil.process_iter(["name"]):
            if process.info["name"] == "faceit_anticheat.exe":
                faceit_anticheat_process = process
                break

        if csgo_process:
            if csgo_running:
                logger.debug("CSGO already running. Skipping closure and anti-cheat launch.")
            else:
                logger.info("CSGO launched. Closing CSGO...")
                close_process("csgo.exe")
                time.sleep(5)  # Give time for CSGO to fully close
                csgo_running = True

        if faceit_anticheat_process:
            if faceit_anticheat_running:
                logger.debug("FaceIT Anti-Cheat already running.")
            else:
                logger.info("FaceIT Anti-Cheat launched.")
                faceit_anticheat_running = True

        if not csgo_running and not faceit_anticheat_running:
            logger.info("Launching CSGO...")
            launch_csgo()

        time.sleep(5)  # Check for CSGO and FaceIT Anti-Cheat every 5 seconds

def main():
    logs_folder = create_logs_folder()
    logger = create_logger(logs_folder)

    try:
        while True:
            steam_process = None

            # Check Steam process
            for process in psutil.process_iter(["name", "exe"]):
                if process.info["name"] == "steam.exe" and "steam" in process.info["exe"].lower():
                    steam_process = process
                    break

            if steam_process:
                cmdline = steam_process.cmdline()
                if "csgo.exe" in cmdline:
                    logger.info("CSGO launched from Steam. Monitoring CSGO...")
                    monitor_csgo()

            time.sleep(5)  # Check for Steam and CSGO every 5 seconds
    except Exception as e:
        logger.error("An error occurred: " + str(e))

if __name__ == "__main__":
    main()
