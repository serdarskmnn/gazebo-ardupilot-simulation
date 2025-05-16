from pymavlink import mavutil  

# Since the Gazebo/ArduPilot simulation is running on this machine, the localhost IP is used
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

print("Waiting for heartbeat...")
master.wait_heartbeat()
print("Connected!")

# When the heartbeat message is received, it indicates the system is running
# This message shows the system status and confirms that the connection is established
